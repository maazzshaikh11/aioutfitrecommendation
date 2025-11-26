#!/bin/sh
set -e

# runtime port fallback to 8000 for local dev
PORT_TO_USE="${PORT:-8000}"

echo "Starting FastAPI on port ${PORT_TO_USE}"
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT_TO_USE}"
