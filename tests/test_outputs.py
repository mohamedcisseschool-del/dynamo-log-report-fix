import json
from pathlib import Path
from typing import Any

import pytest


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def _load_report() -> Any:
    """Load the report for the individual success-criterion tests."""
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_criterion_1_report_format() -> None:
    """Success criterion 1: report.json exists and has the exact JSON schema and types."""
    assert REPORT_PATH.exists(), f"Missing required report: {REPORT_PATH}"

    try:
        report = _load_report()
    except json.JSONDecodeError as exc:
        pytest.fail(f"{REPORT_PATH} is not valid JSON: {exc}")

    assert isinstance(report, dict), "report.json must contain one JSON object"

    assert set(report) == EXPECTED_KEYS, (
        f"Expected exactly the keys {sorted(EXPECTED_KEYS)}, "
        f"but received {sorted(report)}"
    )

    assert isinstance(report["total_requests"], int) and not isinstance(
        report["total_requests"], bool
    ), "total_requests must be a JSON integer"

    assert isinstance(report["unique_ips"], int) and not isinstance(
        report["unique_ips"], bool
    ), "unique_ips must be a JSON integer"

    assert isinstance(report["top_path"], str), "top_path must be a JSON string"


def test_criterion_2_total_requests() -> None:
    """Success criterion 2: total_requests equals the number of non-empty log lines."""
    report = _load_report()

    assert report["total_requests"] == 6, (
        f"Expected total_requests to be 6, "
        f"but received {report['total_requests']!r}"
    )


def test_criterion_3_unique_ips() -> None:
    """Success criterion 3: unique_ips equals the number of distinct client IPs."""
    report = _load_report()

    assert report["unique_ips"] == 3, (
        f"Expected unique_ips to be 3, "
        f"but received {report['unique_ips']!r}"
    )


def test_criterion_4_top_path() -> None:
    """Success criterion 4: top_path equals the most frequently requested path."""
    report = _load_report()

    assert report["top_path"] == "/index.html", (
        f"Expected top_path to be '/index.html', "
        f"but received {report['top_path']!r}"
    )
