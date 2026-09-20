#!/usr/bin/env python3
"""Validate the four HTML reports produced by reverse-ai-product."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPORTS = {
    "01-user-journey.html": {
        "marker": "user-journey",
        "ids": [
            "scope", "evidence", "journey-table", "journey-map", "branches",
            "inconsistencies", "pain-points", "opportunities", "unknowns",
        ],
        "tokens": ["用户", "产品界面", "系统结果"],
    },
    "02-agent-contracts.html": {
        "marker": "agent-contracts",
        "ids": [
            "scope", "agents", "contracts", "tools", "context", "dataflow",
            "flow", "claims", "validate",
        ],
        "tokens": ["输入信息", "可观察判断", "全局上下文", "完成条件"],
    },
    "03-single-agent-system-prompt.html": {
        "marker": "single-agent-system-prompt",
        "ids": [
            "scope", "input", "output", "tools", "state", "rules", "prompt",
            "trace", "tests", "unknowns",
        ],
        "tokens": ["System Prompt", "核心目标", "任务边界", "状态机", "完成条件"],
    },
    "04-product-architecture.html": {
        "marker": "product-architecture",
        "ids": [
            "summary", "evidence", "domains", "e2e", "layers", "relations",
            "context", "knowledge", "models", "tech", "entities", "sequence",
            "panorama", "as-is", "to-be", "risks", "trace", "unknowns",
        ],
        "tokens": ["erDiagram", "sequenceDiagram", "flowchart", "As-Is", "To-Be"],
    },
}

FORBIDDEN = ["TODO", "FIXME", "REPORT_TITLE", "REPORT_KIND", "REPORT_SUBTITLE"]
EVIDENCE_TERMS = ["已确认", "页面事实", "合理推断", "建议设计", "未知", "尚未确认"]


def validate_file(path: Path, spec: dict[str, object]) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"missing file: {path.name}"]
    except UnicodeDecodeError:
        return [f"not UTF-8: {path.name}"]

    lower = text.lower()
    if "<!doctype html>" not in lower:
        errors.append("missing HTML5 doctype")
    if '<meta charset="utf-8"' not in lower and "<meta charset='utf-8'" not in lower:
        errors.append("missing UTF-8 charset declaration")
    if "</html>" not in lower or "</body>" not in lower:
        errors.append("missing closing body/html")
    if len(text.encode("utf-8")) < 5000:
        errors.append("report is suspiciously small (<5 KB)")

    marker = str(spec["marker"])
    if not re.search(rf"<body\b[^>]*\bdata-report=[\"']{re.escape(marker)}[\"']", text, re.I):
        errors.append(f"missing body marker data-report={marker}")

    for section_id in spec["ids"]:
        if not re.search(rf"\bid=[\"']{re.escape(section_id)}[\"']", text, re.I):
            errors.append(f"missing section id: {section_id}")
    for token in spec["tokens"]:
        if token not in text:
            errors.append(f"missing required content token: {token}")
    for token in FORBIDDEN:
        if token in text:
            errors.append(f"unresolved placeholder: {token}")
    if not any(term in text for term in EVIDENCE_TERMS):
        errors.append("missing evidence-grade labels")
    if "/Users/" in text or "file://" in lower:
        warnings.append("contains a private absolute file path")

    for warning in warnings:
        print(f"WARN {path.name}: {warning}")
    return [f"{path.name}: {error}" for error in errors]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    output_dir = args.output_directory.expanduser().resolve()
    if not output_dir.is_dir():
        print(f"ERROR output directory does not exist: {output_dir}")
        return 2

    errors: list[str] = []
    for filename, spec in REPORTS.items():
        errors.extend(validate_file(output_dir / filename, spec))

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"FAILED: {len(errors)} validation error(s)")
        return 1

    print("OK: four-report reverse-engineering bundle passed validation")
    for filename in REPORTS:
        size = (output_dir / filename).stat().st_size
        print(f"  {filename}: {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
