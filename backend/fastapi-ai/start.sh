#!/usr/bin/env sh
# start.sh
: "${PORT:=8000}"   # default PORT=8000 if not provided
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --proxy-headers
