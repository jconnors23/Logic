# Recommended Maintenance Process

**Goal:** Weekly "gym trips" — supplement daily software engineering with one core LeetCode problem where you truly learn the *essence*: why the problem exists, the brute-force logic, and the golden solution pattern.

---

## Problem Directory Structure

Each problem lives in its own directory (e.g. `twosum/`, `validparen/`) with these files:

| File | Purpose |
|------|---------|
| `brute_force.py` | Your initial attempt; the working brute-force solution. |
| `{problem_snake_case}.py` | The golden/optimal solution. E.g. `two_sum.py` for Two Sum, `valid_paren.py` for Valid Parentheses. |
| `intuition.txt` | Notes on the core logic and why the solution works. |
| `psuedo.txt` | Problem prompt, algorithm notes, pattern name, and 2–3 line "gotcha" logic. |

---

## The Reality Check: How Long Should 1 Core Problem Take?

The original 60–75 minute "Optimized Maintenance" frame was aspirational. In practice, a **thoughtful** session that includes:

- Brute-force attempt (with some struggle)
- Socratic review and critique
- Golden-solution reproduction and understanding
- Artifact documentation

…will often take **90–120 minutes** for an easy/medium problem when done well.

That’s **expected**. The idea isn’t to race; it’s to create a sustainable weekly rhythm where each session builds durable understanding.

---

## Recommended Weekly Process

### Time Allocation (90–120 Minutes Total)

| Phase | Time | Action |
|-------|------|--------|
| **1. The Sprint** | 20–25 min | Attempt the problem in `brute_force.py`. Get brute-force if you can. **Hard cap: 25 min.** If stuck, move on—don’t spin. |
| **2. The Audit** | 20–25 min | Ask Cursor: *"Critique my logic. What is the O(n) pattern here?"* Socratic dialogue. Focus on *why* brute force is slow and what the optimal pattern addresses. |
| **3. The Golden Solve** | 20–25 min | Create `{problem_snake_case}.py` (e.g. `two_sum.py`). Rewrite using the optimal pattern. See *"Making the Golden Solve Less Scary"* below. |
| **4. The Artifact** | 10–15 min | Update `psuedo.txt` with the pattern name (e.g., "Hash Map Lookup") and the 2–3 line "gotcha" logic. |

---

## Making the Golden Solve Less Scary

The Golden phase often feels like a threat—a blank screen with no "excuse" left. Use these **safety nets**:

1. **Open Book Policy** — Keep optimal pseudocode visible on half your screen while you type. Aim to understand *flow*, not memorize syntax.

2. **Lego Strategy** — Write in chunks: setup (2–3 lines) → main loop → return. Don’t try to hold the whole thing in your head.

3. **Reproduce, Don’t Invent** — You’re tracing a blueprint. Senior engineers learn patterns; they don’t rediscover Dijkstra every time.

4. **Kiro Bridge** — If you freeze, ask for "just the first two lines" to get momentum. Then continue.

5. **Muscle Memory** — Typing the optimal solution encodes it differently than reading. Even with pseudocode open, the act of typing matters.

---

## Cadence: The Weekly Gym

- **Frequency:** 1 core problem per week.
- **When:** Block a 90–120 minute slot (e.g., Sunday morning, Saturday afternoon).
- **Mindset:** This is a deliberate practice block, not a speed run. Daily SE work is the field; this is the gym.

---

## Compact Variant (75–80 Minutes)

Use when time is tight:

| Phase | Time | Adjustment |
|-------|------|------------|
| Sprint | 20 min | Strict cap. Move on earlier if stuck. |
| Audit | 15–20 min | Focus on one core inefficiency and the pattern name. Fewer Socratic rounds. |
| Golden | 20 min | Open Book from the start. Less invention, more reproduction. |
| Artifact | 10 min | Update `psuedo.txt` with pattern name + 1–2 line gotcha only. |

---

## Why Both Brute Force and Golden?

- **Brute force** builds the habit of "get something working" and surfaces the inefficiency you’ll later optimize.
- **Golden** encodes the canonical pattern (Two-Pointer, Sliding Window, etc.) into your toolkit.
- Together, they give you the *essence*: why the problem exists and how the optimal pattern solves it.

---

## Alignment with Teaching Style

This process works with the hint-first Socratic style in `maintenance-teaching-style.mdc`:

- Use **`learn`** in a problem directory to start the flow. Cursor reviews `intuition.txt`, `brute_force.py`, then `{problem_snake_case}.py` (e.g. `two_sum.py`).
- The Audit phase is where Socratic dialogue happens; let it run until you reach mastery before moving to Golden.
- The Golden phase is reproduction in `{problem_snake_case}.py`; Cursor can still nudge with hints if you ask.

---

## Summary

| Question | Answer |
|----------|--------|
| How long should 1 core LeetCode question take? | **90–120 minutes** for a full session (brute + audit + golden + artifact). |
| Can it be adjusted? | Yes — cap Sprint at 25 min, use Compact variant when needed, split across two days if desired. |
| What’s the goal? | Weekly gym trips: deep, sustainable learning of one problem’s essence, not volume. |
