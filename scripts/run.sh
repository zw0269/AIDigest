#!/bin/bash
set -euo pipefail

cd /Users/zw/work/project_test/AIDigest
PYTHONPATH=src ./.venv/bin/python -m aidigest run
