# User journey HTML contract

## Required sections

Use these IDs so the suite validator can check the report:

1. `scope` — viewed range, ordering method, inaccessible evidence.
2. `evidence` — evidence ledger with IDs, screenshot/page source, exact visible text, UI controls, Agent, asset/state/error.
3. `journey-table` — columns: phase, user goal, user action, page feedback, decision, asset/state change, friction, emotion/thought, evidence.
4. `journey-map` — three swimlanes: user, interface, system result.
5. `branches` — normal, modify/correct, failure/insufficient-credit/interruption.
6. `inconsistencies` — chat/task/canvas/assets/preview conflicts.
7. `pain-points` — at least three prioritized UX problems.
8. `opportunities` — opportunities for a comparable product.
9. `unknowns` — evidence gaps and next validation actions.

Add `data-report="user-journey"` to `<body>`.

## Diagram rules

- Put the user's intent/action, interface response, decision, next state, and failure handling in nodes.
- Use a diamond for every judgment and label every branch, for example `满意 / 不满意`, `成功 / 失败`, `余额充足 / 不足`, `继续 / 中断`.
- Put evidence IDs in every fact-backed node.
- Visually distinguish confirmed, inferred, suggested, and unknown nodes.
- Do not present unobserved failure paths as existing product behavior.

## Completion check

- The earliest user message and first product response are included.
- Every observed confirmation explains what changed afterward.
- Buttons, forms, cards, asset history, current state, preview/edit/export, and errors were checked.
- “Agent completed” was cross-checked against visible assets/state.
- The report is self-contained and has no TODO or placeholder text.
