"""
Daily practice REMINDER email (v2).

The old version pre-assigned problems from a date-pinned schedule and wrote
them back to the DB. That's been replaced by live, dynamic selection inside
the `/practice` skill (run in Claude). So this script no longer assigns
anything — it just sends a lean nightly nudge (read-only) to come practice.

Fires ~8:45pm IST so the reminder lands just before the 9pm-11pm block.

Required environment variables (already set as GitHub Actions secrets):
  EMAIL_ADDRESS         Gmail address used as SMTP login + From
  EMAIL_APP_PASSWORD    Gmail app password (16-char)
  RECIPIENT_EMAIL       Where the reminder is delivered
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


def read_state():
    """Read-only: streak + solved/total for the nudge. Never writes."""
    try:
        with DB_PATH.open("r", encoding="utf-8") as f:
            db = json.load(f)
        md = db.get("metadata", {})
        solved = sum(1 for p in db.get("problems", []) if p.get("status") == "solved")
        total = md.get("total_problems", len(db.get("problems", [])))
        streak = md.get("current_streak", 0)
        return streak, solved, total
    except Exception:
        return 0, 0, 0


def render_html(today_str, streak, solved, total):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:#f5f5f5;margin:0;padding:0;">
  <div style="max-width:600px;margin:0 auto;background:#ffffff;">
    <div style="background:#4f46e5;color:#fff;padding:22px 26px;">
      <h1 style="margin:0 0 4px 0;font-size:21px;">🧩 Time to practice — 9pm block</h1>
      <p style="margin:0;font-size:14px;opacity:0.9;">{today_str} &middot; keep the streak alive</p>
    </div>
    <div style="padding:22px 26px;color:#374151;">
      <p style="margin:0 0 16px 0;">Hi Saurabh — your <strong>9:00-11:00pm</strong> practice block is coming up.</p>
      <div style="padding:14px 18px;background:#eef2ff;border-radius:8px;color:#3730a3;font-size:15px;margin-bottom:16px;">
        Open Claude and run <code style="background:#fff;padding:2px 6px;border-radius:4px;">/practice</code><br>
        I'll pick today's 3 problems (progression + review + weak-area) and coach you through them.
      </div>
      <p style="margin:0;font-size:14px;color:#6b7280;">Streak: <strong>{streak}</strong> solve-days &middot; Solved: <strong>{solved}/{total}</strong></p>
      <p style="margin:14px 0 0 0;font-size:13px;color:#9ca3af;">Miss a day? Nothing breaks — the selector just runs next time. State-driven, not calendar-driven.</p>
    </div>
    <div style="padding:12px 26px;background:#f9fafb;border-top:1px solid #e5e7eb;color:#9ca3af;font-size:12px;text-align:center;">
      Nightly reminder &middot; problem selection happens live in /practice.
    </div>
  </div>
</body></html>"""


def render_text(today_str, streak, solved, total):
    return (
        f"Time to practice — 9pm block ({today_str})\n\n"
        f"Your 9:00-11:00pm practice block is coming up.\n"
        f"Open Claude and run  /practice  — I'll pick today's 3 problems "
        f"(progression + review + weak-area) and coach you through them.\n\n"
        f"Streak: {streak} solve-days | Solved: {solved}/{total}\n"
        f"Miss a day? Nothing breaks — the selector runs next time."
    )


def send_email(subject, html, text, sender, password, recipient):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Practice Reminder <{sender}>"
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
        "EMAIL_ADDRESS": sender, "EMAIL_APP_PASSWORD": password, "RECIPIENT_EMAIL": recipient,
    }.items() if not v]
    if missing:
        print(f"ERROR: missing env vars: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    today_str = datetime.now(IST).strftime("%Y-%m-%d")
    streak, solved, total = read_state()
    subject = "🧩 Practice time (9pm) — run /practice"
    html = render_html(today_str, streak, solved, total)
    text = render_text(today_str, streak, solved, total)
    send_email(subject, html, text, sender, password, recipient)
    print(f"Sent practice reminder to {recipient}")


if __name__ == "__main__":
    main()
