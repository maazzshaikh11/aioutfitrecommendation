#!/usr/bin/env sh

# default port fallback if $PORT not provided by the platform
PORT="${PORT:-8000}"

# optional workers setting (uncomment if you want)
# WORKERS=${UVICORN_WORKERS:-1}

# exec replaces shell so signals are forwarded
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
# If you need reload in dev: uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --reload
