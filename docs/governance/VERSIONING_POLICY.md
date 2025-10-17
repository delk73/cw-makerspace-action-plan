---
version: 0.1.0
lastReviewed: 2025-10-17
owner: de
---

# 🧭 Makerspace Repository Versioning Policy

All Markdown documents in this repository are **governed**, not manually versioned.  
Document metadata (`version`, `lastReviewed`) ensures consistency across the project through automated validation and explicit human review signals.

---

## 1. Canonical Source of Truth

| Field | Source | Description |
|-------|---------|-------------|
| **`repoVersion`** | `version.json` | Defines the current repository phase (e.g., `0.1` for *Smoke Test*). |
| **`version`** | YAML front matter of each doc | Immutable, auto-managed patch version (e.g., `0.1.2`). Bumped automatically on material content change. Never edited manually. |
| **`lastReviewed`** | YAML front matter of each doc | The only manually editable metadata field. Used to mark a human review when content itself is unchanged. |

The prefix (e.g., `0.1`) is immutable within a phase.  
All documents share that prefix.  
`version` progression and enforcement are handled exclusively by repository tooling.

---

## 2. Enforcement Rules

- Manual edits to **`version`** cause CI to **fail the build**.  
- Manual edits to **`lastReviewed`** are **permitted and encouraged**.  
- CI checks all `.md` files for:
  - Non-semantic versions (`draft-*`, `v0.1.0`, etc.)
  - Prefix drift (`0.0.x` vs `0.1.x`)
  - Missing or malformed version metadata  

If drift is detected, CI halts with:

```

Immutable version prefix: 0.1.x
❌ Drift detected — one or more docs contain user-edited or non-semantic version tags.

```

---

## 3. Version & Review Responsibilities

| Field | Who Controls | When It Changes | Purpose |
|--------|--------------|----------------|----------|
| **`version`** | Automation | On material body edits (below front matter) | Tracks canonical document evolution |
| **`lastReviewed`** | Human | On manual validation or audit | Tracks date a human verified content accuracy |

### 🧩 `version`
- Managed entirely by repository tooling.
- Increments automatically when body text changes.
- Never edited manually or incremented by hand.

### 🕓 `lastReviewed`
- Safe to update manually when confirming a doc remains accurate.  
- Does **not** trigger a `version` bump or CI failure.  
- Example workflow:

```yaml
lastReviewed: 2025-10-17
```

```bash
git add docs/NAME.md
git commit -m "docs: mark reviewed (no content change)"
```

---

## 4. Local Normalization

Before committing or pushing, maintainers can align metadata locally:

```bash
# Preview (detects drift, exits 1 if found)
python scripts/bump_doc_versions.py --dry-run

# Apply normalization (auto-fixes version prefixes and patch numbers)
python scripts/bump_doc_versions.py
```

This ensures all Markdown files remain synchronized with the immutable `repoVersion` prefix.

---

## 5. CI Integration

The workflow `.github/workflows/version-guard.yml` runs on every push or pull request:

* Executes `bump_doc_versions.py --dry-run`
* Fails if **version drift** or non-semantic tags are detected
* Allows manual `lastReviewed` edits
* Prints the governed version prefix (`repoVersion`) for transparency

---

## 6. Governance Principle

> **Version metadata is canonical infrastructure, not author content.**
> Authors and reviewers focus on substance and correctness.
> CI and automation maintain chronology, integrity, and version consistency.

---

**Maintainer:** de
**Script:** `scripts/bump_doc_versions.py`
**Workflow:** `.github/workflows/version-guard.yml`