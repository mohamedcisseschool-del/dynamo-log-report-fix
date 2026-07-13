import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_PATTERN = re.compile(
    r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH)\s+(\S+)\s+HTTP/\d(?:\.\d)?"'
)


def main() -> None:
    total_requests = 0
    unique_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    for raw_line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        unique_ips.add(line.split()[0])

        match = REQUEST_PATTERN.search(line)
        if match:
            path_counts[match.group(1)] += 1

    if not path_counts:
        raise RuntimeError("No HTTP request paths were found in /app/access.log")

    report = {
        "total_requests": total_requests,
        "unique_ips": len(unique_ips),
        "top_path": path_counts.most_common(1)[0][0],
    }

    REPORT_PATH.write_text(
        json.dumps(report, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
