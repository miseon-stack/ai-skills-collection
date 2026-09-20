# Four-report suite contract

## Shared evidence ledger

Maintain one structured ledger during the run:

| Field | Meaning |
|---|---|
| `evidence_id` | Stable ID reused across all reports |
| `source` | Screenshot/page/file and visible location |
| `chronology` | Message/phase ordering basis |
| `page_text` | Exact visible text, kept concise |
| `agent` | Visible Agent label, if any |
| `ui` | Button, form, card, task, preview, or error |
| `asset` | Text/image/video/audio asset and count |
| `state` | Visible task/confirmation/error state |
| `grade` | confirmed, inferred, recommended, unknown |
| `notes` | conflict or access limitation |

Do not put hidden reasoning, credentials, private identifiers, or guessed backend details in the ledger.

## Cross-report invariants

- The earliest user request is identical in reports 1–4.
- Agent inventory and names are identical in reports 2 and 4.
- Report 3's selected Agent exists in report 2.
- Confirmed tools in reports 2–4 have page/result evidence; functional names are labeled non-official.
- Context field status is not upgraded across reports without new evidence.
- Asset counts and model names match raw evidence.
- Explicit and inferred handoffs remain visually distinct.
- Chat/canvas/task/asset conflicts remain visible in all affected reports.
- “Completed” requires assets and state verification, not an Agent sentence.

## Four file markers

- `01-user-journey.html`: `<body data-report="user-journey">`
- `02-agent-contracts.html`: `<body data-report="agent-contracts">`
- `03-single-agent-system-prompt.html`: `<body data-report="single-agent-system-prompt">`
- `04-product-architecture.html`: `<body data-report="product-architecture">`

## Visual standard

- Standalone HTML5, UTF-8, responsive desktop/mobile.
- Clear table overflow inside containers; no page-level horizontal spill.
- Sticky compact navigation when useful.
- Consistent badges: confirmed green, inferred amber/dashed, recommended orange, unknown gray, risk red.
- Evidence IDs adjacent to claims and diagram nodes.
- Mermaid source/fallback included for ER/state/sequence/panorama diagrams.
- No TODO, placeholder, empty required section, or copied product credential.

## Final acceptance

The suite is complete only when all four files exist, the validator succeeds, and opening them shows no runtime warning or broken primary diagram. If a diagram CDN cannot load, the source/fallback must remain readable.
