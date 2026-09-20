# Agent contracts HTML contract

Add `data-report="agent-contracts"` to `<body>` and use these IDs:

1. `scope` — viewed evidence and gaps.
2. `agents` — Agent inventory in chronological order.
3. `contracts` — fixed I/O contract cards.
4. `tools` — total tool table.
5. `context` — global-context field table.
6. `dataflow` — producer-consumer table.
7. `flow` — Agent input→judgment→tool→output→handoff diagram with boundaries.
8. `claims` — confirmed/inferred/suggested/unknown register.
9. `validate` — five highest-value next validations.

## Ten-section Agent card

1. Core goal.
2. Trigger conditions.
3. Inputs, grouped by all six source types.
4. Observable judgments.
5. Tools.
6. Outputs, grouped by all five output types.
7. Global-context read/write table: field/object, read/write, producer, consumer, update time, evidence grade, evidence.
8. Completion conditions.
9. Exceptions and retries.
10. Unconfirmed questions.

## Required global checks

- Same data with multiple versions.
- Chat state versus canvas/task/asset state.
- Stable references among character, scene, prop, and storyboard.
- Upstream modification invalidating downstream assets.
- Read-only or write-only fields.
- Agent saying complete while global state or assets are incomplete.

Do not use filenames or analyst-written captions as page facts when the visible screenshot disagrees.
