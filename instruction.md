Read the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

Treat each nonblank line as one request. The client IP is the first whitespace-separated value on the line. Inside the quoted request, the path is the value between the HTTP method and the HTTP version.

Success criteria:

1. `/app/report.json` exists and contains one valid JSON object with exactly the keys `total_requests`, `unique_ips`, and `top_path`. The first two values must be JSON integers, and `top_path` must be a JSON string.
2. `total_requests` equals the number of nonblank lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IPs in `/app/access.log`.
4. `top_path` equals the path requested most often in `/app/access.log`.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
