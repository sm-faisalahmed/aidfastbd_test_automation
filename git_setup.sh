#!/usr/bin/env bash
set -euo pipefail
REMOTE_URL=${1:-}

# Configure user (change if necessary)
git config user.name "sm"
git config user.email "smfaisal7575@gmail.com"

if [ ! -d .git ]; then
  git init
  echo "Initialized empty Git repository."
else
  echo "Git repository already initialized."
fi

git add .
git commit -m "Initial commit: tests, cleanup script, fixes" || true

echo "Committed files."

if [ -n "$REMOTE_URL" ]; then
  git remote add origin "$REMOTE_URL" || true
  git branch -M main
  git push -u origin main
  echo "Pushed to remote: $REMOTE_URL"
else
  echo "No remote URL provided. To add and push later run:\n git remote add origin <url> ; git push -u origin main"
fi
