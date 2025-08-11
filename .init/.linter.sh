#!/bin/bash
cd /home/kavia/workspace/code-generation/simple-notes-web-app-5016-5026/notes_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

