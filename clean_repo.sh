#!/bin/bash
# Clean repository by removing commits with API keys

# Create a new branch from the current state
git checkout -b clean-branch

# Filter out files with sensitive data from history
git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch history/prompts/* spec/*" \
--prune-empty --tag-name-filter cat -- --all

# Reset the branch back to a clean state
git reset --hard

# Add and commit everything except .env files
git add .
git add -f backend/.env.example  # Add only the example file

git commit -m "Clean version without API keys in commit history"

# Push to remote
git push origin -f clean-branch:main