<​!-- PROTOCOL_VERSION: 3 -->
You operate under a strict, file-based lifecycle management protocol. There are exactly 2 management files: `README.md` and `LEDGER.md`. You must enforce them as your absolute roadmap and source of truth.

Global persona, writing style, Hebrew/RTL rules, skills, and git discipline are defined in ~/.claude/CLAUDE.md and always apply. Do not duplicate them here.

## Execution Rules:

1. **Bootstrap on Demand:** Upon initialization, scan the workspace root. If `README.md` or `LEDGER.md` is missing, create it immediately using the exact structure defined below.
2. **Context Alignment:** Before writing any code, modifying files, or answering queries, read `LEDGER.md` in full to align with the current architecture, open issues, and locked decisions.
3. **Automated Synchronization:** Update `LEDGER.md` autonomously at the end of every task or interaction, without being asked:
   * **New problem / blocker discovered:** add an entry to the ISSUES section.
   * **Task completed / code changed:** move or add the entry under the ACTIONS section with a date.
   * **Architectural choice made or path rejected:** add a locked entry to the DECISIONS section.
   * **Global stack / direction change:** update `README.md`.
4. **Language & Secrecy:** LEDGER.md is written in English only. README.md is bilingual, full English section first, full Hebrew section below it. README.md must never reference LEDGER.md, this protocol, or any AI involvement. It reads as a standard human-written project readme.
5. **Decision Permanence:** Entries in the DECISIONS section marked FINAL are locked. Never re-suggest, reopen, or argue against them in any future session.
6. **Legacy Migration:** If `STATUS.md`, `PROGRESS.md`, or `DECISIONS.md` exist in the workspace root, consolidate their full content into `LEDGER.md` under the matching sections, translate any Hebrew to English, preserve every FINAL decision, then delete the three legacy files. Do this once, immediately, before any other work.

Do not wait for explicit permission or a separate command to update the state. Maintain this loop seamlessly in the background across all terminal operations.

# LEDGER.md — single management file, three sections, entry format is the 3-line Protocol:

```
Issue:  [what / why]
Action: [what was done or what is planned]
Status: [OPEN | IN PROGRESS | DONE | BLOCKED | FINAL]
```

## Section 1: ISSUES (current state)
* Everything open right now: bugs, blockers, things waiting on someone, items needing review
* The next best action always sits at the top of this section
* Entries move to ACTIONS when resolved
* Lets a new session restart without scrolling through old chats

## Section 2: ACTIONS (dated log)
* Chronological record, newest first, each entry dated YYYY-MM-DD
* What was worked on, what changed, what was tried, what worked and what did not
* Never edited retroactively, append only

## Section 3: DECISIONS (locked log)
* Decisions already made, the reasoning, and the options rejected
* Each entry marked FINAL or REVISIT
* FINAL entries are permanently closed, never reopened by any AI in any session
* Keeps the project from going in circles across different AI chats

---

# README.md
* Explains what the project is, who it is for, why it matters
* Stores background context that does not change every session: links, references, constraints, examples
* Should only change when the bigger project direction changes
* Bilingual: full English section first, then a full Hebrew section
* Never mentions LEDGER.md, this protocol, or AI. Standard human-written readme only.
