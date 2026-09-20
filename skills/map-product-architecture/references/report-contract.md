# Product architecture HTML contract

Add `data-report="product-architecture"` to `<body>` and use these IDs:

1. `summary` — one-sentence architecture thesis.
2. `evidence` — fact sources and gaps.
3. `domains` — core functional domains.
4. `e2e` — five-flow end-to-end table.
5. `layers` — nine-layer architecture.
6. `relations` — Agent/tool/context relationships.
7. `context` — typed global-context architecture.
8. `knowledge` — knowledge/public/private asset architecture.
9. `models` — model access and routing.
10. `tech` — capability and technology-options table.
11. `entities` — entity table and Mermaid ER.
12. `sequence` — Mermaid sequence diagram.
13. `panorama` — layered panorama with subgraphs, labeled edges, legend, data/state flows, and current problems.
14. `as-is` — current architecture.
15. `to-be` — recommended architecture.
16. `risks` — prioritized architecture risks.
17. `trace` — component/evidence/grade/confidence.
18. `unknowns` — unresolved questions.

## Panorama line semantics

- Solid: confirmed.
- Dashed: inferred.
- Orange/thick or dotted: recommended.
- Gray dotted: unknown.
- Red node: current defect/risk.

## Required To-Be checks

Unified state source, verifiable completion gate, duration/style/dialogue/audio-video validation, dependency invalidation, idempotent retry, credit estimate/hold/settlement/refund, interruption propagation, full tracing, model-effect feedback, local recomputation, and private-asset isolation.
