# Scenario 20 — Mastermind (Lab-4)

Terminal-based Mastermind game enhanced incrementally with Vibe Coding.

## Original defect
The original feedback used:
`partial = sum(ch in code for ch in guess) - exact`
which could count one code occurrence multiple times.

Example: code `1123`, guess `1111` incorrectly produced `(2, 2)`. The corrected result is `(2, 0)`.

## Completed tasks
- Duplicate-aware feedback with exact matches resolved first.
- Clear win/loss/quit lifecycle.
- Guess history preserved in memory.
- Guess limit enforced.
- Invalid guesses rejected without consuming turns.
- Easy, Medium and Hard difficulty modes.
- Same feedback algorithm supports every configured code length.
- No persistence and no third-party dependencies.

## Difficulty modes

| Mode | Length | Symbols | Turns |
|---|---:|---|---:|
| Easy | 3 | 1–4 | 10 |
| Medium | 4 | 1–6 | 10 |
| Hard | 5 | 1–8 | 8 |

## Run
`python main.py`

## Required submission
1. Before video: show the original duplicate-symbol defect.
2. After video: show the fixed behavior and new features.
3. Updated code.
4. Complete Vibe Coding/LLM chat history exported as PDF/document.

## Testing
The implementation was checked for exact matches, repeated symbols, no matches, mixed exact/partial matches, all difficulties, invalid guesses, final-turn wins, losses, quitting, history and turn handling.
