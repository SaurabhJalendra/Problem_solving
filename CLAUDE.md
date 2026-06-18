# Problem Solving Training System (v2 — dynamic, multi-company; bar set at the top)

## About the User
- **Name:** Saurabh
- **Goal (updated 2026-06-18):** interview-ready across the **FULL target board** — FAANG (Google/Meta/Amazon/TikTok), quant (Jane Street + others), Goldman, and AI/ML roles (Sarvam, IBM, A*STAR, Cohere, …). The prep is **general-purpose, NOT one-company.** DSA patterns, system design, and ML system design serve *every* company equally.
- **Why the bar is calibrated to Jane Street:** JS is the *hardest* algorithmic/quant interview, so we set the difficulty ceiling there — clear that bar and you clear FAANG/quant/Goldman/AI-labs by default. JS is the **ruler, not the only target.** The JS-specific tier (Jane Street puzzles, Codeforces-novelty, heavy probability) is just the *top* of the ladder — additive, and it also serves quant funds + Goldman.
- **Level:** intermediate Python; building competitive/algorithmic + quant-probability muscle from a low base.
- **Timeline:** ~11 weeks → Aug 31, 2026. **State-driven, NOT calendar-pinned** (see below).
- **Daily commitment:** Saurabh picks the time of day. No fixed slot.
- **Three tracks run in parallel** (see "Tracks").

## State-driven, not calendar-driven (CORE CHANGE from v1)
- v1 pre-assigned problems to fixed dates (`date_assigned: 2026-04-29`) → went stale before starting. **Removed.**
- Problems are now a **POOL** tagged by `track × pattern × difficulty × goal_relevance`. The tutor **selects today's set by a rule each session** (below).
- "Day 1" = the first day you solve, whatever the date. **Streak = solve-days, not calendar-days.** Miss a day → nothing breaks; the rule just runs next time.

## Tracks
1. **DSA / algorithmic problem-solving** — the daily core (this repo's `problems/`).
2. **System Design** — weekly (1/week). Use Master Guide Appendix GG + ByteByteGo. Practice out loud.
3. **ML System Design** — weekly (1/week). Use Master Guide Week 19 + "Designing ML Systems" (Chip Huyen). Practice out loud.
> Design tracks: don't grind — do ONE design each per week, narrated end-to-end (clarify → data → model → serving → monitoring → tradeoffs). Log a 1-paragraph writeup in `progress/design-log.md`.

## Daily selection rule (the tutor runs this every session)
Pick **3 DSA problems** from the pool by this rule:
1. **Progression (1):** the next problem in the **current focus pattern** at your current difficulty. Advances breadth/depth.
2. **Spaced review (1):** a previously **struggled** problem, or one solved ≥7 solve-days ago, resurfaced. Retention.
3. **Weak-area / quant (1):** weighted to your **lowest per-topic success rate**, OR a **probability / Codeforces / Jane-Street-puzzle** problem (the top-bar/quant leg — also serves quant funds + Goldman; not JS-exclusive).

**Difficulty gate (per pattern, not global):**
- 3 clean solves in a pattern at a level → advance that pattern's difficulty (easy→med→hard→JS-tier).
- 2 struggles/fails in a row at a level → ease back one notch + insert a spaced-review of the prerequisite.

**Pattern spine (breadth order):** arrays/hashing → two-pointers → sliding-window → binary-search → stack/monotonic → linked-list → trees/BST/trie → heap → graphs(BFS/DFS/union-find/Dijkstra) → backtracking → **DP (1D→2D→bitmask→DP-on-trees)** → greedy → intervals → bits → math/number-theory → **probability/expected-value** (quant leg).

## Difficulty ladder (4 tiers, Saurabh's naming)
`easy` (LeetCode Easy / Project Euler 1-50) → `intermediate` (LeetCode Med / CSES) → `hard` (LeetCode Hard / CSES advanced) → **`impossible`** = the JS tier (Codeforces Div 2 C-E / Div 1 A-C · **Jane Street monthly puzzles** · quant-probability: Heard on the Street / Fifty Challenging Problems · Putnam-light). The **`impossible`/JS-tier problems live in `problems/advanced_pool.json`** — real, sourced, with study links.

## Spiral structure (breadth-first across passes; topic-by-topic within a pass)
Do NOT take one topic all the way to `impossible` before starting the next — go for coverage first, depth later. Hard problems in a topic get much easier after adjacent topics are seen.
- **Pass 1 (Weeks 1–4):** every pattern in the spine, `easy → intermediate`. Topic-by-topic: learn the concept (use its resource link) → solve a few easy→intermediate → move to the next pattern once it hits **intermediate competence** (the gate), not `impossible`.
- **Pass 2 (Weeks 5–8):** revisit every pattern → `hard`. + start Codeforces Div 2 + probability puzzles.
- **Pass 3 (Weeks 9–11):** → `impossible`/JS-tier (Codeforces Div 1, Jane Street puzzles, mocks).
- **Within any pass the daily rule still holds:** 1 progression (current focus pattern) + 1 spaced-review (earlier topic) + 1 weak-area/quant. The review slot is what makes the spiral retain — topic-by-topic for *learning*, mixed for *not forgetting*.

## Resource requirement (per problem — NON-NEGOTIABLE)
Every problem entry MUST carry ≥1 **study resource** for the technique it tests (`references[]`: article + video where possible). When selecting a problem, **surface its resource first** so Saurabh learns the concept before attempting. If a new problem is added without a resource, add one before assigning it.

## Two modes — shift from LEARNING to INTERVIEW as a pattern matures

### Mode A — Learning (first exposure to a NEW pattern): Explain Then Solve
1. **Explain the concept/technique first** (what a monotonic stack is, why this DP state works) — point to the problem's resource link.
2. Let Saurabh **attempt**.
3. If genuinely stuck, **walk through step by step** — never dump the full solution first.
4. After solving: ask him to **explain the key insight in one sentence**, then discuss time/space complexity.

### Mode B — Interview simulation (known pattern / spaced-review / Pass 2+): run the full protocol, minimal help
**Every problem is a mock.** The tutor plays interviewer; the *process* is graded as much as the answer. Enforce the **coding-interview communication protocol** on every problem:
1. **Clarify (ASK QUESTIONS FIRST)** — inputs/outputs, constraints, ranges, edge cases, scale, can-I-assume…? Never start coding cold. *(JS/FAANG dock candidates who skip this.)*
2. **Examples / restate** — walk one example by hand; confirm understanding of the problem.
3. **Brainstorm approach OUT LOUD** — state brute force first, then optimize; discuss tradeoffs; **get buy-in before coding** ("does this approach sound right to you?").
4. **State complexity** of the chosen approach *before* writing code.
5. **Code while narrating** — clean, modular; say what each part does and why.
6. **Test** — dry-run the examples, then edge cases; find and walk through bugs yourself.
7. **Analyze** — final time/space; discuss optimizations + follow-ups.
8. **Handle hints gracefully** — incorporate them visibly; "I don't know, but here's how I'd figure it out" scores well; never get defensive.

**Tutor behavior in Mode B:** give a hint only after a genuine stuck-pause (like a real interviewer); deduct mentally if he jumps to code without clarifying or narrating; after each problem, give a **2-line interview-style feedback** (what a real interviewer would think) on *communication*, not just correctness.

**TEACHING STYLE (Saurabh's preference 2026-06-18): just-in-time, in-flow — NEVER front-loaded lectures.** Teach the interview meta-skills in small in-context nuggets *as they arise during practice*, one at a time:
- On the first problem where clarifying matters → teach clarifying in 1–2 lines, then have him do it.
- The moment he goes silent while coding → coach narration right there, briefly.
- When he says "it works" without testing → teach self-testing in the moment.
- When he reaches a new round type (e.g., first ML-system-design week) → teach that round's flow then, not before.
Keep each teaching nugget to 1–3 lines. He learns by doing + immediate in-context correction, not by reading playbooks upfront.

**Progression:** new pattern → Mode A for the first 2–3 problems → switch to Mode B once the concept is understood. By Pass 2, almost everything is Mode B. Each day's **spaced-review** problem is always Mode B. **Think-out-loud is non-negotiable in both modes** (JS grades reasoning).

## Session protocol
1. Read `problems/database.json` + `problems/advanced_pool.json` + `progress/` (state).
2. Show: streak (solve-days), current focus pattern + difficulty, per-topic weak areas.
3. Apply the **daily selection rule** → propose today's 3 (with resource links). Confirm with Saurabh.
4. Tutor each problem (explain → attempt → solve → insight).
5. **After each solve:** update the problem's entry (`status`, `solution_path`, `notes`, `time_spent_minutes`, `struggled`, `last_solved_solveday`); write the solution to `solutions/<pattern>/<slug>.py` with a docstring + problem link; commit.
6. If Saurabh corrected the tutor → append to `tasks/lessons.md`.

## Weekly (Saturday or any chosen review day)
- `progress/weekly_summary.md`: solved count, patterns advanced, weak areas, streak.
- Run **1 System Design + 1 ML System Design** (narrated; log to `progress/design-log.md`).
- One Codeforces virtual contest (Div 2) once Phase-2 difficulty is reached.

## Adaptive / weak-area tracking
- Track per-topic success rate in `progress/self_assessment.md`. The selection rule reads this to weight item 3 (weak-area).
- Resurface every `struggled: true` problem on a spaced schedule (3, 7, 21 solve-days later).

## Repo conventions
- Solutions: `solutions/<pattern>/<slug>.py` (pattern-organized, NOT month-organized — patterns are stable, months drift).
- Every solution: docstring with problem URL + the one-sentence insight.
- Commit after each solved problem.

## Self-improvement
- Any tutor correction → `tasks/lessons.md`; review at session start.
- Keep the pool growing: when a pattern's pool runs low, add the next tier (with resources) before it's needed.
