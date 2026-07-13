import json
from pathlib import Path

import pytest


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def read_report() -> dict:
    """Read the JSON report used by the success-criterion tests."""
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_criterion_1_report_format() -> None:
    """Success criterion 1: report.json exists and has the exact keys and value types."""
    assert REPORT_PATH.exists(), "Missing /app/report.json"

    try:
        report = read_report()
    except json.JSONDecodeError as exc:
        pytest.fail(f"/app/report.json is not valid JSON: {exc}")

    assert isinstance(report, dict), "The report must be one JSON object"
    assert set(report) == EXPECTED_KEYS, (
        f"Expected exactly {sorted(EXPECTED_KEYS)}, got {sorted(report)}"
    )
    assert type(report["total_requests"]) is int, "total_requests must be an integer"
    assert type(report["unique_ips"]) is int, "unique_ips must be an integer"
    assert isinstance(report["top_path"], str), "top_path must be a string"


def test_criterion_2_total_requests() -> None:
    """Success criterion 2: total_requests equals the number of nonblank log lines."""
    report = read_report()
    assert report["total_requests"] == 6, (
        f"Expected total_requests=6, got {report['total_requests']!r}"
    )


def test_criterion_3_unique_ips() -> None:
    """Success criterion 3: unique_ips equals the number of distinct client IPs."""
    report = read_report()
    assert report["unique_ips"] == 3, (
        f"Expected unique_ips=3, got {report['unique_ips']!r}"
    )


def test_criterion_4_top_path() -> None:
    """Success criterion 4: top_path equals the path requested most often."""
    report = read_report()
    assert report["top_path"] == "/index.html", (
        f"Expected top_path='/index.html', got {report['top_path']!r}"
    )
