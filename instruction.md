Parse the Apache-style access log at `/app/access.log` and write a summary to `/app/report.json`.

Treat each non-empty line as one request. The client IP is the first whitespace-separated field in the line. The request path is the field between the HTTP method and HTTP version inside the quoted request line.

Success criteria:

1. `/app/report.json` exists and contains a valid JSON object with exactly the keys `total_requests`, `unique_ips`, and `top_path`. `total_requests` and `unique_ips` must be JSON integers, and `top_path` must be a JSON string.
2. `total_requests` equals the number of non-empty lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IPs in `/app/access.log`.
4. `top_path` equals the request path that appears most often in `/app/access.log`.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
