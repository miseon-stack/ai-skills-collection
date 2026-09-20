---
name: map-agent-contracts
description: Identify every Agent actually visible in an AI product workflow and derive evidence-based I/O contracts, functional judgments, tool calls, global-context reads/writes, state, re-entry, and downstream handoffs. Use for multi-Agent product teardown from screenshots, browser pages, chats, canvas assets, task states, and errors, producing a standalone Agent-contract HTML report.
---

# Reverse Agent Contracts

Produce `02-agent-contracts.html` unless the user requests another filename.

## Non-negotiable boundaries

- Use only observable behavior. Public “thinking complete” or “planning complete” is a user-facing summary, not hidden chain-of-thought.
- A verbal plan is not a tool call. Confirm execution only with an asset, state transition, tool result, page result, or error.
- Do not assume a standard number of Agents. Record only names supported by page evidence.
- Distinguish a UI/session identity from a proven executing/orchestrating Agent.
- If no official tool name is visible, use a functional label and append `（功能命名，并非官方工具名）`.
- Keep browser work read-only and follow the same privacy/safety restrictions as the journey skill.
- Tag claims as confirmed, inferred, suggested, or unknown.

## Workflow

1. Build an evidence ledger and chronological phase map.
2. Identify each visible Agent name, first appearance, trigger, predecessor, successor, re-entry, and absent expected roles.
3. For every Agent inspect six input sources: current user input, long-term user information, project global context, upstream Agent output, platform knowledge/public assets, and tool/runtime results.
4. Summarize functional judgments only: completeness checks, confirmation gates, automatic continuation, stop conditions, modification, failure, validation, and completion.
5. Inventory tools and classify each as confirmed result, announced-only, inferred function, or unknown.
6. Inspect five output classes: user reply, page components, text/media assets, global-context writes, downstream task/handoff.
7. Create one fixed-format ten-section contract card per Agent.
8. Build global context, producer-consumer, version, reference, invalidation, and inconsistency tables.
9. Draw the Agent input→judgment→tool→output→handoff flow. Use solid edges for explicit handoffs and dashed edges for inferred handoffs.
10. List facts, inferences, suggestions, unknowns, and five highest-value validation questions.

## Output contract

Read [references/report-contract.md](references/report-contract.md) before writing. The file must be standalone UTF-8 HTML, responsive, searchable/scannable, and include evidence IDs in cards and diagrams.

Stop after the Agent-contract report. Do not write complete System Prompts in this skill.
