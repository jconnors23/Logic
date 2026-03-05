# Recommended Maintenance Process

**Goal:** Weekly "gym trips" — supplement daily software engineering with one core LeetCode problem where you truly learn the *essence*: why the problem exists, the brute-force logic, and the golden solution pattern.

**Timing: flexible estimates.** The numbers below are like story points: planning and pacing guides, not stopwatches. **Ideally** the full process doesn’t exceed **about 2 hours** for one problem (easy/medium). Learning rates differ; going over when it’s productive is fine. The point is a sustainable rhythm, not hitting a fixed cap.

---

## Problem Directory Structure

Each problem lives in its own directory (e.g. `twosum/`, `validparen/`) with these files:

| File | Purpose |
|------|---------|
| `intuition.md` (or `intuition.txt`) | Notes on the core logic and why the brute-force solution works. |
| `pseudo.md` or `psuedo.txt` | Problem prompt, constraints, algorithm notes, pattern name, and 2–3 line "gotcha" logic. |
| `brute_force.py` | Your initial attempt; the working brute-force solution. |
| `golden.py` or `{problem_snake_case}.py` | The golden/optimal solution (e.g. `golden.py`, `two_sum.py`). |
| `intuition_golden.md` (or `intuition_golden.txt`) | Filled out in Phase 4: thought process behind the golden solution (why the pattern, key invariants, trace). Used for learning and future reference. |

---

## Learning Structure and Time Allocation

Sessions can be split across the week. **Total: ~2 hours** (120–135 min typical; flexible).

### Phase 1 — Brute force and mastery (~1 hour)

| Step | Time | Action |
|------|------|--------|
| **1. Problem review and understanding** | 15 min | Read the problem, constraints, and examples. Review `pseudo.md` / `psuedo.txt` (prompt, pattern name if present, gotchas). Solidify understanding before coding. |
| **2. Brute force implementation** | ~20 min | Implement in `brute_force.py`. Get a working solution. If stuck after ~20 min, move to review — don’t spin. |
| **3. Brute force review with Cursor** | 30 min | Socratic teaching: critique logic, find flaws, trace examples. Adjust `brute_force.py` until correct and tests pass. Do not proceed until brute-force mastery. |

**Phase 1 total: ~60 min (15 + 20 + 30).**

---

### Phase 2 — Golden: from hints to implementation (~40–45 min)

| Step | Time | Action |
|------|------|--------|
| **4. Golden Socratic teaching** | 15–20 min | With Cursor: Socratic dialogue toward the golden pattern. Build a **hint structure** (idea → invariant → structure) ready for implementation. No full code yet — hints and mental checklist only. |
| **5. Golden implementation** | 25 min | Implement in `golden.py` (or `{problem_snake_case}.py`) using the hint structure. Open-book from `intuition_golden.md` if it already exists from a prior run; otherwise use notes from the Socratic session. |
| **6. Final review and critic** | 15–20 min | Cursor critiques `golden.py`. Then Cursor **fills out `intuition_golden.md`** (thought process, why the pattern, key invariants, one trace, complexity). Learner reviews it for alignment and future reference. |

---

### Phase 3 — Closure

| Step | Action |
|------|--------|
| **7. Commit and mark complete** | Commit all problem files (pseudo, intuition, brute_force, golden, intuition_golden). Push. Mark the problem complete (e.g. checklist or log). |

**End-to-end: ideally ≤2 hours total**, spread across the week if you like. Estimates are flexible; depth of understanding matters more than hitting the clock.

---

## Cadence: The Weekly Gym

- **Frequency:** 1 core problem per week.
- **When:** Spread Phase 1–3 across the week (e.g. Phase 1 one day, Phase 2–3 another, or all in one 2-hour block).
- **Mindset:** Deliberate practice. Daily SE work is the field; this is the gym.

---

## Making the Golden Solve Less Scary

1. **Open Book Policy** — Use `intuition_golden.md` or Socratic notes on half your screen while you type. Aim to understand *flow*, not memorize syntax.
2. **Lego Strategy** — Write in chunks: setup → main loop → return.
3. **Reproduce, Don’t Invent** — You’re tracing a blueprint. Senior engineers learn patterns; they don’t rediscover them every time.
4. **Kiro Bridge** — If you freeze, ask for "just the first two lines" to get momentum.
5. **Muscle Memory** — Typing the solution encodes it differently than reading.

---

## Alignment with Teaching Style

This process works with the hint-first Socratic style in `maintenance-teaching-style.mdc`:

- Use **`learn`** in a problem directory to start the flow. Cursor reviews `intuition.md`, `brute_force.py`, then (after Phase 2) `intuition_golden.md` and `golden.py`.
- Phase 1 step 3 is where brute-force Socratic dialogue runs until mastery.
- Phase 2 step 4 is Socratic teaching toward the golden hint structure (no full solution).
- Phase 2 step 6: Cursor fills out `intuition_golden.md` after the final critic so the learner has a durable artifact.

---

## Critique of the Timing Methodology

**Strengths**

- **Phase 1 cap (1 hour)** keeps brute force from ballooning and forces “good enough to review” instead of perfectionism.
- **Explicit 30 min for brute-force review** signals that understanding and correction are first-class, not a quick glance.
- **Separating “golden Socratic” (15–20 min) from “golden impl” (25 min)** avoids dumping code: the learner builds a mental model before typing.
- **120–135 min total** is realistic for one problem with review, implementation, and artifact; it discourages rushing.
- **Spread across one week** reduces pressure to do everything in one sitting and supports spaced repetition (e.g. Phase 1 one day, golden the next).

**Risks and mitigations**

| Risk | Mitigation |
|------|------------|
| Phase 1 runs over (e.g. brute force takes 35 min) | After ~20–25 min on impl, move to review even if tests don’t all pass. Review can fix logic with Socratic guidance. |
| “30 min review” feels vague | Treat it as “Socratic until mastery”: trace 2–3 inputs, fix one flaw at a time, re-run tests. Stop when correct and learner can explain. |
| Golden Socratic (15–20 min) may be too short for hard problems | Use longer for medium/hard; estimates scale with difficulty. |
| Filling `intuition_golden.md` in 15–20 min with critic | Do critic first, then Cursor drafts `intuition_golden.md`; learner reviews and tweaks. |

**Summary:** The timing is **coherent and teach-friendly**. Treat it as **flexible estimates** (like story points): the ~2-hour target is reasonable for actually learning one problem’s pattern, but learning rates differ — the foolish part is rigid caps; the useful part is a session budget so you don’t drift indefinitely and Socratic phases get enough time.

---

## Summary

| Question | Answer |
|----------|--------|
| How long for one core problem? | **Ideally ≤2 hours** (typical 120–135 min). Phase times are **estimates**; flexible. |
| Can it be split? | Yes — across one week. Going over when it’s productive is fine; learning rates differ. |
| What’s the goal? | Weekly gym: deep, sustainable learning of one problem’s essence (brute + golden + artifact), not volume. |
