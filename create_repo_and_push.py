import os
import base64
import json
import requests
from pathlib import Path

TOKEN = os.environ.get('GITHUB_TOKEN')
if not TOKEN:
    print('GITHUB_TOKEN environment variable not set')
    raise SystemExit(1)

OWNER = os.environ.get('GITHUB_OWNER', 'sm-faisalahmed')
REPO = os.environ.get('GITHUB_REPO', 'aidfastbd_test_automation')
VISIBILITY = os.environ.get('GITHUB_REPO_VISIBILITY', 'public')
ROOT = Path(__file__).resolve().parent

# files to exclude
EXCLUDE_DIRS = {'.venv', '.venv_clean', '.venv_new', '.pytest_cache'}
EXCLUDE_FILES = {'aidfastbd_test_automation.zip'}

session = requests.Session()
session.headers.update({'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github+json'})

# 1) create repo
print('Creating repository...')
resp = session.post('https://api.github.com/user/repos', json={'name': REPO, 'private': False})
if resp.status_code not in (201, 422):
    print('Failed to create repo:', resp.status_code, resp.text)
    raise SystemExit(1)
if resp.status_code == 201:
    print('Repository created')
else:
    print('Repository may already exist:', resp.status_code)

# collect files
print('Collecting files...')
file_paths = []
for p in sorted(ROOT.rglob('*')):
    if p.is_dir():
        if p.name in EXCLUDE_DIRS:
            # skip entire dir
            continue
        else:
            continue
    # skip files in excluded dirs
    parts = set(p.parts)
    if parts & EXCLUDE_DIRS:
        continue
    rel = p.relative_to(ROOT)
    if rel.name in EXCLUDE_FILES:
        continue
    # skip .git and the script itself and the token
    if rel.parts[0] == '.git':
        continue
    if rel == Path('create_repo_and_push.py'):
        continue
    file_paths.append(rel)

print(f'Files to upload: {len(file_paths)}')

# 2) create blobs
blobs = {}
for rel in file_paths:
    full = ROOT / rel
    with open(full, 'rb') as f:
        data = f.read()
    # base64 encode
    b64 = base64.b64encode(data).decode('ascii')
    payload = {'content': b64, 'encoding': 'base64'}
    r = session.post(f'https://api.github.com/repos/{OWNER}/{REPO}/git/blobs', json=payload)
    if r.status_code != 201:
        print('Failed to create blob for', rel, r.status_code, r.text)
        raise SystemExit(1)
    sha = r.json()['sha']
    blobs[str(rel).replace('\\','/')] = sha

# 3) create tree
print('Creating tree...')
entries = []
for path, sha in blobs.items():
    entries.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': sha})

r = session.post(f'https://api.github.com/repos/{OWNER}/{REPO}/git/trees', json={'tree': entries})
if r.status_code != 201:
    print('Failed to create tree', r.status_code, r.text)
    raise SystemExit(1)
tree_sha = r.json()['sha']

# 4) create commit
print('Creating commit...')
commit_payload = {'message': 'Initial commit: add project files', 'tree': tree_sha}
r = session.post(f'https://api.github.com/repos/{OWNER}/{REPO}/git/commits', json=commit_payload)
if r.status_code != 201:
    print('Failed to create commit', r.status_code, r.text)
    raise SystemExit(1)
commit_sha = r.json()['sha']

# 5) create ref
print('Creating ref...')
r = session.post(f'https://api.github.com/repos/{OWNER}/{REPO}/git/refs', json={'ref': 'refs/heads/main', 'sha': commit_sha})
if r.status_code not in (201, 422):
    print('Failed to create ref', r.status_code, r.text)
    raise SystemExit(1)
print('Pushed files to https://github.com/{}/{} (main)'.format(OWNER, REPO))
