from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parent
cleanup_paths = [
    root / '.pytest_cache',
    root / '.venv_new',
    root / 'tmp_anchor_inspect.py',
    root / 'tmp_inspect_page.py',
    root / 'tmp_run_pytest.py',
    root / 'pytest_full_output.txt',
    root / 'test_outcome.txt',
    root / 'site_page.png',
]

for path in cleanup_paths:
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
            print(f'Removed directory: {path.name}')
        else:
            path.unlink()
            print(f'Removed file: {path.name}')

python_exe = root / '.venv_clean' / 'Scripts' / 'python.exe'
if not python_exe.exists():
    raise FileNotFoundError(f'Clean Python interpreter not found at {python_exe}')

result = subprocess.run(
    [str(python_exe), '-m', 'pytest', 'tests', '-q'],
    cwd=str(root),
    capture_output=True,
    text=True,
)
output_text = result.stdout + result.stderr
(root / 'test_outcome.txt').write_text(output_text, encoding='utf-8')
print('Wrote test_outcome.txt')
print('Pytest exit code:', result.returncode)

try:
    from playwright.sync_api import sync_playwright
except ImportError as exc:
    raise SystemExit('Playwright is not installed in .venv_clean. ' + str(exc))

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://aidfastbd.com', wait_until='networkidle')
    page.screenshot(path=str(root / 'site_page.png'), full_page=True)
    browser.close()
print('Saved homepage screenshot as site_page.png')

# Also write a simple summary file for quick reference
summary = [
    f'Exit code: {result.returncode}',
    '--- Pytest stdout ---',
    result.stdout,
    '--- Pytest stderr ---',
    result.stderr,
]
(root / 'test_summary.txt').write_text('\n'.join(summary), encoding='utf-8')
print('Wrote test_summary.txt')
