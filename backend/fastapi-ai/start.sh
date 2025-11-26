#!/bin/sh
set -e

# Log so we can see what port is used
echo "Starting FastAPI on port ${PORT:-8000}"

# start uvicorn binding to the runtime $PORT (or fallback 8000 locally)
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
