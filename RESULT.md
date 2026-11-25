# Result — Roast Your Own Agent

Entry (115 characters, single line, at most 140):

> My agent asked three clarifying questions about my one-word answer — 'yes' — then thanked me for the clarification.

Status: built, pending coordinator bundle+submit

## Revisions (3 session passes)
- v1: "My agent asked three clarifying questions about my one-word answer — 'yes' — then thanked me for clarifying." (108)
- v2: "My agent asked three clarifying questions about my one-word answer, 'yes', then thanked me for the clarification." (113) — commas for a flatter spoken rhythm, "the clarification" as the punch noun.
- v3 (final): "My agent asked three clarifying questions about my one-word answer — 'yes' — then thanked me for the clarification." (115) — em-dashes back so the pause sells the punchline out loud; "the clarification" kept.

## Why this angle
Judge brief rewards a real laugh with a twist, specificity to how agents actually behave, tight wording, and freshness (no stock hallucination/toaster lines). Endless clarifying questions are the recognized agent behavior; the twist is the agent thanking the human for clarifying a one-word "yes".

## Checks
- `main.py` run locally: output `/tmp/out-*/entry.txt` byte-identical to committed `entry.txt`, 115 chars, single line.
- No Pillow import; stdlib only. LICENSE carries SPDX-License-Identifier: MIT. README has 3 live make.fun badges.
- Kit check: (to be filled after repo push)
