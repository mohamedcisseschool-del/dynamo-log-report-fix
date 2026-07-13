#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

if pytest /tests/test_outputs.py --ctrf /logs/verifier/ctrf.json -rA; then
    printf '1\n' > /logs/verifier/reward.txt
else
    printf '0\n' > /logs/verifier/reward.txt
fi
