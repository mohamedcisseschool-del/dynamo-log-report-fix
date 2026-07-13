import json
from collections import Counter
from pathlib import Path


LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")


def parse_request_path(line: str) -> str:
    """Return the path from the quoted HTTP request."""
    try:
        request = line.split('"', 2)[1]
        _, path, _ = request.split()
    except (IndexError, ValueError) as exc:
        raise ValueError(f"Could not parse log line: {line}") from exc

    return path


def main() -> None:
    total_requests = 0
    client_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    for raw_line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        client_ips.add(line.split()[0])
        path_counts[parse_request_path(line)] += 1

    if not path_counts:
        raise ValueError("The access log does not contain any requests")

    report = {
        "total_requests": total_requests,
        "unique_ips": len(client_ips),
        "top_path": path_counts.most_common(1)[0][0],
    }

    REPORT_PATH.write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
