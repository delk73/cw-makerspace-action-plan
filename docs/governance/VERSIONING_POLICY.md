---
version: 0.1.2
lastReviewed: '2025-10-22'
owner: de
---

# 🧭 Makerspace Repository Versioning Policy

All Markdown documents in this repository are **governed**, not manually versioned.  
Document metadata (`version`, `lastReviewed`) is normalized by CI after merge to the `main` branch.

---

## 1. Canonical Source of Truth

| Field | Source | Description |
|-------|---------|-------------|
| **`repoVersion`** | `version.json` | Defines the current repository phase (e.g., `0.1`). |
| **`version`** | YAML front matter of each doc | Auto-managed patch version (e.g., `0.1.2`). Incremented automatically on material content change when merged into `main`. |
| **`lastReviewed`** | YAML front matter of each doc | Automatically set to the merge date when the document is normalized by CI. |

The prefix (e.g., `0.1`) is immutable within a phase.  
All documents share that prefix.  
Version progression and enforcement occur exclusively on the `main` branch via CI automation.

---

## 2. Enforcement Rules

- Manual edits to **`version`** are ignored and overwritten by CI.  
- **`lastReviewed`** is updated automatically during CI normalization.  
- CI checks all `.md` files for:
  - Non-semantic or malformed versions  
  - Prefix drift (e.g., `0.0.x` vs `0.1.x`)  
  - Missing front-matter metadata  

If any corrections are needed, CI commits them automatically with:

```

ci: normalize doc versions

```

---

## 3. Version & Review Responsibilities

| Field | Controlled By | When It Changes | Purpose |
|--------|----------------|----------------|----------|
| **`version`** | CI (`scripts/ci_bump_doc_versions.py`) | When a document body changes and the commit is merged to `main` | Tracks canonical evolution of documentation |
| **`lastReviewed`** | CI | On every normalization commit to `main` | Reflects the most recent verified state |

### 🧩 `version`
- Managed only after merge into `main`.  
- Incremented automatically based on content changes.  
- Never edited manually or in pull requests.

### 🕓 `lastReviewed`
- Automatically set to the current date when CI normalizes metadata.  
- No manual updates required.

---

## 4. Local Development

Local normalization scripts and manual version updates are **deprecated**.  
Developers **do not run versioning locally**.  
CI performs all enforcement once commits reach `main`.

---

## 5. CI Integration

The workflow `.github/workflows/version-bump.yml` enforces version consistency for all Markdown documents.

### Behavior Summary
- Triggered only on `push` to `main`
- Executes `scripts/ci_bump_doc_versions.py`
- Detects Markdown changes relative to the previous commit on `main`
- Bumps `version` and updates `lastReviewed` as needed
- Commits and pushes changes automatically under the bot identity
- Ensures all documents conform to the immutable `repoVersion` prefix

### Example CI Log Output
```

✅ Bumped versions:
★ docs/governance/VERSIONING_POLICY.md: 0.1.0 → 0.1.1

```

---

## 6. Governance Principle

> **Version metadata is canonical infrastructure, not author content.**  
> Authors focus on substance; CI maintains version integrity and chronology on `main`.

---

**Maintainer:** de  
**Script:** `scripts/ci_bump_doc_versions.py`  
**Workflow:** `.github/workflows/version-bump.yml`
