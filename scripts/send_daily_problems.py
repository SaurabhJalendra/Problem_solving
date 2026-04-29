"""
Daily Problem Solver email sender.

Reads problems/database.json, picks the next 2 pending problems
(unassigned), marks them assigned to today, sends an HTML email via
Gmail SMTP, then writes the updated database back.

Required environment variables:
  EMAIL_ADDRESS         Gmail address used as the SMTP login + From
  EMAIL_APP_PASSWORD    Gmail app password (16-char, no spaces)
  RECIPIENT_EMAIL       Where the daily problems should be delivered
"""

import json
import os
import smtplib
import sys
from datetime import datetime, timezone, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "problems" / "database.json"

IST = timezone(timedelta(hours=5, minutes=30))


def load_db():
    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_db(db):
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        f.write("\n")


def pick_next_problems(problems):
    """Return the next 2 pending problems with date_assigned == None,
    in order by (day, problem_number)."""
    pending = [
        p for p in problems
        if p.get("status") == "pending" and p.get("date_assigned") is None
    ]
    pending.sort(key=lambda p: (p["day"], p["problem_number"]))
    return pending[:2]


def render_html(today_problems, db, today_str):
    metadata = db.get("metadata", {})
    total = metadata.get("total_problems", len(db["problems"]))
    solved = sum(1 for p in db["problems"] if p.get("status") == "solved")
    streak = metadata.get("current_streak", 0)
    phase = metadata.get("phase", "")
    month = metadata.get("month", "?")
    day_label = today_problems[0]["day"] if today_problems else "?"

    def problem_block(p):
        url_or_note = (
            f'<a href="{p["url"]}" style="color:#0066cc;font-weight:600;">{p["title"]}</a>'
            if p.get("url")
            else f'<strong>{p["title"]}</strong> <em>(custom problem — see notes below)</em>'
        )
        notes_html = (
            f'<div style="margin-top:8px;padding:10px;background:#f9fafb;border-left:3px solid #94a3b8;color:#374151;font-size:14px;">{p["notes"]}</div>'
            if p.get("notes")
            else ""
        )
        return f"""
        <div style="background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:18px 20px;margin-bottom:14px;">
          <div style="font-size:13px;color:#6b7280;margin-bottom:6px;">[{p['source']}] &middot; {p['topic']} / {p['subtopic']} &middot; <strong style="color:#b45309;">{p['difficulty']}</strong></div>
          <div style="font-size:17px;color:#111827;">{url_or_note}</div>
          {notes_html}
        </div>
        """

    blocks = "\n".join(problem_block(p) for p in today_problems)

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:#f5f5f5;margin:0;padding:0;">
  <div style="max-width:640px;margin:0 auto;background:#ffffff;">
    <div style="background:#4f46e5;color:#fff;padding:24px 28px;">
      <h1 style="margin:0 0 4px 0;font-size:22px;">🧠 Daily Problem Solving</h1>
      <p style="margin:0;font-size:14px;opacity:0.9;">{today_str} &middot; Day {day_label} &middot; Month {month} ({phase})</p>
    </div>
    <div style="padding:24px 28px;">
      <p style="margin:0 0 18px 0;color:#374151;">Hi Saurabh, here are today's 2 problems:</p>
      {blocks}
      <div style="margin-top:20px;padding:14px 18px;background:#eef2ff;border-radius:8px;color:#3730a3;font-size:14px;">
        Progress: <strong>{solved}/{total}</strong> solved &middot; Current streak: <strong>{streak} days</strong>
      </div>
      <p style="margin-top:20px;color:#6b7280;font-size:14px;">Open Claude Code in the <code>Problem_solving</code> repo and tell it which problem you want to start with — it will tutor you through it.</p>
    </div>
    <div style="padding:14px 28px;background:#f9fafb;border-top:1px solid #e5e7eb;color:#9ca3af;font-size:12px;text-align:center;">
      Sent automatically by the Daily Problem Solver workflow.
    </div>
  </div>
</body>
</html>"""


def render_text(today_problems, db, today_str):
    lines = [
        f"Daily Problem Solving — {today_str}",
        f"Day {today_problems[0]['day']} | Month {db['metadata'].get('month')} ({db['metadata'].get('phase')})",
        "",
    ]
    for i, p in enumerate(today_problems, 1):
        lines.append(f"{i}. [{p['source']}] {p['title']}  ({p['difficulty']})")
        lines.append(f"   Topic: {p['topic']} / {p['subtopic']}")
        if p.get("url"):
            lines.append(f"   Link: {p['url']}")
        if p.get("notes"):
            lines.append(f"   Notes: {p['notes']}")
        lines.append("")
    solved = sum(1 for p in db["problems"] if p.get("status") == "solved")
    total = db["metadata"].get("total_problems", len(db["problems"]))
    streak = db["metadata"].get("current_streak", 0)
    lines.append(f"Progress: {solved}/{total} solved | Current streak: {streak} days")
    lines.append("")
    lines.append("Open Claude Code in the Problem_solving repo to start.")
    return "\n".join(lines)


def send_email(subject, html, text, sender, password, recipient):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Problem Solving Trainer <{sender}>"
    msg["To"] = recipient
    msg.attach(MIMEText(text, "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, [recipient], msg.as_string())


def main():
    sender = os.environ.get("EMAIL_ADDRESS")
    password = os.environ.get("EMAIL_APP_PASSWORD")
    recipient = os.environ.get("RECIPIENT_EMAIL")

    missing = [k for k, v in {
        "EMAIL_ADDRESS": sender,
        "EMAIL_APP_PASSWORD": password,
        "RECIPIENT_EMAIL": recipient,
    }.items() if not v]
    if missing:
        print(f"ERROR: missing env vars: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    db = load_db()
    today_problems = pick_next_problems(db["problems"])

    today_str = datetime.now(IST).strftime("%Y-%m-%d")

    if not today_problems:
        # Curriculum exhausted — send a heads-up email instead.
        subject = "Problem Solving — Curriculum complete!"
        html = f"""<p>Hi Saurabh,</p>
        <p>You've been assigned every problem in the database. Time for a self-assessment and to add the next month's problems.</p>
        <p>Date: {today_str}</p>"""
        text = f"You've completed all assigned problems as of {today_str}. Time for self-assessment."
        send_email(subject, html, text, sender, password, recipient)
        return

    today_iso = datetime.now(IST).strftime("%Y-%m-%d")
    for p in today_problems:
        p["date_assigned"] = today_iso

    db["metadata"]["last_updated"] = today_iso
    save_db(db)

    day = today_problems[0]["day"]
    primary_topic = today_problems[0]["topic"].title()
    subject = f"📚 Daily Problems — Day {day} | {primary_topic}"
    html = render_html(today_problems, db, today_str)
    text = render_text(today_problems, db, today_str)

    send_email(subject, html, text, sender, password, recipient)
    print(f"Sent day {day} problems to {recipient}")


if __name__ == "__main__":
    main()
