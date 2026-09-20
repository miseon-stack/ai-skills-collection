# Single-Agent prompt HTML contract

Add `data-report="single-agent-system-prompt"` to `<body>` and use these IDs:

1. `scope` — target Agent evidence and boundary.
2. `input` — six-source input contract with required/optional fields.
3. `output` — five-class output contract.
4. `tools` — tool contract.
5. `state` — state table and Mermaid `stateDiagram-v2`.
6. `rules` — fact/inference/suggestion/unknown rules.
7. `prompt` — directly usable System Prompt.
8. `trace` — rule-evidence traceability.
9. `tests` — minimum test set.
10. `unknowns` — unresolved questions.

## Fifteen System Prompt sections

1. Agent name and role.
2. Core goal.
3. Task boundary.
4. Input contract.
5. Global-context protocol.
6. Workflow.
7. Tool-call specification.
8. User confirmation mechanism.
9. Result validation.
10. Modification and rollback.
11. Exception handling.
12. State machine.
13. Downstream handoff.
14. Completion conditions.
15. Output format.

Use `<功能工具>` placeholders instead of invented API names. Semantic field names not visible on the page must say `推导设计`.

## Test columns

Test input, initial state, expected judgment, expected tool calls, expected state changes, and forbidden behavior.
