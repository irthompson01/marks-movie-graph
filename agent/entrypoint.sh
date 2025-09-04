#!/usr/bin/env bash
set -e

# Optional: show what we're running
echo "[agent] OPENAI_API_BASE=${OPENAI_API_BASE}"

# Ensure git is initialized so the agent can commit
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  git init
  git add .
  git commit -m "chore: baseline" || true
}

# Run your Crew
python crew_runner.py
