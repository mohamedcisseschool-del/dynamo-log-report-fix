# Fixed Harbor log-report task

This repository contains the repaired Terminal-Bench 2 task for a small access-log report.
The agent reads `/app/access.log` and writes `/app/report.json` with the total number of
requests, the number of unique client IPs, and the most requested path.

## Task layout

- `task.toml` contains the Harbor task configuration and metadata.
- `instruction.md` is the prompt shown to the agent.
- `environment/` contains the pinned Docker image and the input log.
- `solution/` contains the oracle solution.
- `tests/` contains the verifier and its shell entry point.

## Main fixes

- Changed `artifacts` to a top-level array that points to `/app/report.json`.
- Replaced the floating Python image with an approved image pinned by digest.
- Removed the leaked solution file from the agent image.
- Rewrote the verifier so it checks the JSON structure, types, and actual values.
- Corrected the reward and CTRF output paths.
- Rewrote the instruction with four numbered criteria that match the four tests.

## Validation

Run these commands from the repository root with Docker and the required Harbor version installed:

```bash
harbor run -p . -a oracle
harbor run -p . --agent nop
```

The oracle run should return reward `1`, and the no-op run should return reward `0`.
Copy the actual output from your own Harbor runs into the assessment form.