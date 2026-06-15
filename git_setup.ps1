param(
    [string]$RemoteUrl = ''
)

# Configure user info (change if needed)
git config user.name "sm"
git config user.email "smfaisal7575@gmail.com"

if (!(Test-Path -Path .git)) {
    git init
    Write-Host "Initialized empty Git repository."
} else {
    Write-Host "Git repository already initialized."
}

git add .
git commit -m "Initial commit: tests, cleanup script, fixes" -q
Write-Host "Committed files."

if ($RemoteUrl) {
    git remote add origin $RemoteUrl -f
    git branch -M main
    git push -u origin main
    Write-Host "Pushed to remote: $RemoteUrl"
} else {
    Write-Host "No remote URL provided. To add and push later run:`n git remote add origin <url> ; git push -u origin main"
}
