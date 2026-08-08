# abhishek-python-foundations

Daily Python builds — Phase 1 of a structured path toward becoming a **Smart Contract Security Auditor / Researcher** and **Blockchain Developer**.

## What's actually in this repo
Everything here is from a guided, concept-first Python track — deep explanations, deliberately broken code, and real bugs found and fixed, not just finished solutions. I'm also working through PY4E (Python for Everybody, Chuck Severance) separately as my primary structured course; this repo specifically tracks the deeper, applied side of that learning.

## Progress so far — `python-mastery/`
- **Module 1** — How Python actually executes code, print, comments, reading errors bottom-up
- **Module 2** — Variables, data types, dynamic typing, implicit type conversion
- **Module 3** — Operators (arithmetic, comparison, logical, assignment), short-circuit evaluation
- **Module 4** — Safe input handling with try/except, specific vs. combined exception handling
- **Module 5** — Conditionals (if/elif/else), nested logic, truthy/falsy — including a deliberately reproduced condition-ordering bug (the same bug class behind real access-control exploits in smart contracts)
- **Module 6** — Loops (while, for, break, continue), infinite loop recovery with Ctrl+C, validated input patterns, running totals

Each module includes working code *and* intentionally broken versions, used to understand exactly why something fails — the habit of testing edge cases and reading errors carefully is being built deliberately from day one, since it's the core skill an auditor actually needs.

## Where this is headed
This repo is the foundation stage of a longer path:

**Python Foundations (this repo) → Solidity & EVM internals → Foundry → Smart Contract Security Auditing & Research**

The end goal isn't just writing working code — it's being able to read someone else's contract, understand exactly how it behaves, and find what breaks it.

## Follow along
Commits build up daily. Each one represents a real concept tested, not just copied.
