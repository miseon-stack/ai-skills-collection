---
name: map-product-architecture
description: Synthesize user journeys, Agent contracts, tools, global context, model options, assets, task states, billing, errors, and official evidence into a complete evidence-tiered AI product architecture. Use to produce As-Is, inferred, and To-Be architecture, data entities, Mermaid ER/sequence/panorama diagrams, risks, and traceability in a standalone HTML report.
---

# Reverse Product Architecture

Produce `04-product-architecture.html` unless the user requests another filename.

## Boundary

- Prefer completed journey, Agent-contract, tool, context, and single-Agent-prompt materials as inputs; always trace claims back to raw evidence.
- Keep browser inspection read-only. Never trigger product mutations or inspect credentials/sensitive data.
- If external research is necessary, use official product sources only.
- Do not assert backend languages, databases, queues, cloud services, model vendors, or dynamic routing without direct support.
- Classify all components and edges as `【已确认】`, `【合理推断】`, `【建议设计】`, or `【未知】`.

## Workflow

1. Create a fact-source inventory covering user actions, chat, Agent names, UI controls, canvas assets, versions, model choices, tool results, errors, billing, and official sources.
2. Identify user-facing functional domains and their evidence gaps.
3. Trace one complete task through five simultaneous flows: user, Agent control, tools, global data/context, and media assets.
4. Build nine layers: user/channel; workbench; applications; Agent/orchestration; tools/services; model access/routing; global context/data; knowledge/public assets; infrastructure/governance.
5. Decompose global context into typed subcontexts instead of one memory box.
6. Separate project data from reusable knowledge and answer style compilation, cross-shot character reuse, cinematography knowledge, model capability, safety/billing enforcement, feedback learning, and private/public isolation.
7. Describe required technical capabilities before possible/recommended implementation categories. Never present a technology example as confirmed.
8. Define core entity templates and relationships, explicitly separating page-backed relationships from architectural derivation.
9. Draw Mermaid ER, end-to-end sequence, and layered panorama diagrams. Label arrows as call/read/write/event/confirm/asset reference/state update.
10. Compare As-Is and To-Be, prioritize risks, and provide component-evidence traceability.

## Output contract

Read [references/report-contract.md](references/report-contract.md). Use responsive standalone UTF-8 HTML. Mermaid diagrams must include source fallback and a legend. Keep the main panorama readable; move dense detail into tables rather than creating an unreadable graph.

Stop after the architecture report.
