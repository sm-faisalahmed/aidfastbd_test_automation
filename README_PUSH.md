Publish instructions

1) Create a GitHub repository (replace <your-username> and <repo-name>):

- Using the website: create a new public repo and copy the remote URL.

- Using the API (requires a personal access token with `repo` scope):

  curl -H "Authorization: token YOUR_TOKEN" -d '{"name":"repo-name","private":false}' https://api.github.com/user/repos

2) Locally initialize and push:

```bash
git init
git add .
git commit -m "Add tests and cleanup script; fix navigation test"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

3) If you want me to create the repo remotely, provide a GitHub Personal Access Token (repo scope) and the desired repo name; I'll create it and show the remote commands.
