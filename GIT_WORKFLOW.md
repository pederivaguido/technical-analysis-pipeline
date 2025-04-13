
# Git Branch Workflow for This Project

This guide outlines the recommended steps for working with feature branches alongside `main` to ensure clean version control, consistent releases, and easy collaboration.

---

## 🚀 Overview

| Branch         | Purpose                                       |
|----------------|-----------------------------------------------|
| `main`         | Stable, production-ready code                 |
| `feature/*`    | Development branches for features, fixes, etc.|

---

## ✅ Step-by-Step Workflow

### 1. Start a New Feature Branch
git checkout main
git pull origin main
git checkout -b feature/your-feature-name

### 2. Work on Your Feature
- Edit or create files
- Test locally
- Stage and commit regularly
git add .
git commit -m "Describe what this commit does"

### 3. Push Your Feature Branch to GitHub
git push -u origin feature/your-feature-name
```

---

### 4. Open a Pull Request (PR)
- On GitHub, open a PR from `feature/your-feature-name` → `main`
- Fill in a clear title and description
- Add a related `CHANGELOG.md` entry if applicable

---

### 5. Merge the PR into `main`
- Click **Merge Pull Request** on GitHub
- Use a squash merge if appropriate for cleaner history

---

### 6. Delete the Feature Branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

---

### 7. Sync Before Starting Another Feature
git checkout main
git pull origin main
```
