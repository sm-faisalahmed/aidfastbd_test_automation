# AidFastBD Test Automation

This project contains acceptance-level automated UI tests for the AidFast website (`https://aidfastbd.com/`). It follows an AT-level (Acceptance Test) strategy with Python, Playwright, and pytest.

## What is included
- `tests/` — automated acceptance tests for homepage and business flows
- `TEST_STRATEGY.md` — test strategy, scope, coverage, and acceptance criteria
- `.venv/` — isolated Python environment created locally
- `requirements.txt` — dependencies for the automation suite

## Setup
1. Open a terminal in `C:\Users\smfai\aidfastbd_test_automation`
2. Activate the virtual environment:
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
   - Command Prompt: `.\.venv\Scripts\activate.bat`
3. Install dependencies:
   `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`
4. Install Playwright browser binaries:
   `.\.venv\Scripts\python.exe -m playwright install chromium`

## Run tests
From the project root:

`.\.venv\Scripts\python.exe -m pytest -q`

## Notes
- This suite validates user-facing acceptance criteria on the homepage.
- The test strategy is designed to match SQA best practices and acceptance-level coverage.
- If the website changes or localization text updates, selectors should be updated accordingly.
