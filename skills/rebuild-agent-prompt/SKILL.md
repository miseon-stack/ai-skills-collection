---
name: rebuild-agent-prompt
description: Reconstruct a directly usable functional-equivalent System Prompt for one selected product Agent from observable page behavior, Agent contracts, tools, global context, assets, confirmations, and errors. Use when asked to reproduce an Agent's workflow and boundaries without claiming the official prompt or hidden chain-of-thought, and deliver a traceable standalone HTML report.
---

# Reconstruct Agent Prompt

Produce `03-single-agent-system-prompt.html` for exactly one target Agent.

## Target selection

- Use the Agent named by the user.
- If the user does not name one, choose the Agent with the richest direct behavior evidence and state the rationale. Ask only when the choice would materially change the user's goal.
- Collect every occurrence of that Agent across the evidence set. Use downstream pages only to verify its output consumption, not to absorb another Agent's responsibilities.

## Evidence rules

- The goal is functional equivalence, not recovery of official wording.
- Do not claim access to hidden chain-of-thought, official System Prompt, official function names, backend implementation, or private account data.
- Separate `【事实规则】`, `【推断规则】`, `【建议规则】`, and `【未知】`.
- Never treat “done” or “compliant” as validation without checking assets and state.
- Keep browser work read-only and avoid all production side effects.

## Workflow

1. Establish the Agent boundary with ten questions: problem, takeover point, trigger, downstream, included work, excluded work, re-entry, mandatory stop, automatic continuation, and user confirmation.
2. Build the six-source input contract.
3. Build the five-class output contract.
4. Build the tool contract using only supported functional tools. Record confirmation, verification, retry, duplicate cost/assets, interruption, and state-write failure behavior.
5. Reconstruct a state machine including observed states and explicitly labeled recommended protection states.
6. Convert evidence to seventeen rule categories: identity, goal, boundary, inputs, reads, writes, workflow, tool choice, preconditions, confirmation, validation, modification/rollback, failure/retry, interruption, handoff, completion, output format.
7. Write a directly usable fifteen-section System Prompt.
8. Create a rule-evidence trace table.
9. Design at least six tests covering normal, missing input, local modification, tool failure, interruption, and UI/global-state conflict. Add insufficient credit and duplicate request when relevant.
10. Stop; do not reconstruct other Agents.

## Output contract

Read [references/report-contract.md](references/report-contract.md). Use standalone UTF-8 HTML with a copyable prompt block and Mermaid state source/fallback.
