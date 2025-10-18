---
version: 0.1.0
lastReviewed: 2025-10-17
owner: de
---

# 🧭 Makerspace Repository Versioning Policy

All Markdown documents in this repository are **governed**, not manually versioned.  
Document metadata (`version`, `lastReviewed`) ensures consistency across the project through automated CI normalization.

---

## 1. Canonical Source of Truth

| Field | Source | Description |
|-------|---------|-------------|
| **`repoVersion`** | `version.json` | Defines the current repository phase (e.g., `0.1` for *Smoke Test*). |
| **`version`** | YAML front matter of each doc | Immutable, auto-managed patch version (e.g., `0.1.2`). Bumped automatically on material content change through CI. |
| **`lastReviewed`** | YAML front matter of each doc | Automatically updated to the current date when the document is modified or normalized by CI. |

The prefix (e.g., `0.1`) is immutable within a phase.  
All documents share that prefix.  
`version` progression and enforcement are handled exclusively by repository automation.

---

## 2. Enforcement Rules

- Manual edits to **`version`** are ignored and will be overwritten by CI.  
- **`lastReviewed`** is updated automatically during CI normalization.  
- CI scans all `.md` files for:
  - Non-semantic versions (`draft-*`, `v0.1.0`, etc.)
  - Prefix drift (`0.0.x` vs `0.1.x`)
  - Missing or malformed front-matter metadata  

If drift or edits are detected, CI **commits corrected metadata automatically** with a standardized message:

```

ci: normalize doc versions

```

---

## 3. Version & Review Responsibilities

| Field | Controlled By | When It Changes | Purpose |
|--------|---------------|----------------|----------|
| **`version`** | CI automation (`ci_bump_doc_versions.py`) | When a document body changes in a pull request | Tracks canonical document evolution |
| **`lastReviewed`** | CI automation | On every content change or normalization | Tracks date of last validation or update |

### 🧩 `version`
- Managed entirely by the CI workflow.  
- Increments automatically when body text changes between a PR branch and its base (`origin/main`).  
- Never edited manually.

### 🕓 `lastReviewed`
- Automatically updated by CI to today’s date when content changes.  
- Requires no manual edits or human intervention.

---

## 4. Local Development Behavior

Local normalization scripts (`bump_doc_versions.py`, `--dry-run`, etc.) are **deprecated**.  
Maintainers do **not** need to bump or check versions locally.  
All version enforcement occurs during CI evaluation on push or pull request.

---

## 5. CI Integration

The workflow `.github/workflows/version-bump.yml` governs repository version consistency.

### Behavior Summary
- Executes `scripts/ci_bump_doc_versions.py`
- Compares Markdown documents between `origin/main` and `HEAD`
- Bumps `version` and updates `lastReviewed` where content differs
- Commits and pushes the normalization automatically using the bot identity
- Ensures all documents share the immutable prefix from `version.json`

### Example CI Log Output
```

✅ Bumped versions:
★ docs/governance/VERSIONING_POLICY.md: 0.1.0 → 0.1.1

```

---

## 6. Governance Principle

> **Version metadata is canonical infrastructure, not author content.**  
> Authors and reviewers focus solely on substance and correctness.  
> CI automation maintains chronology, integrity, and version coherence.

---

**Maintainer:** de  
**Script:** `scripts/ci_bump_doc_versions.py`  
**Workflow:** `.github/workflows/version-bump.yml`