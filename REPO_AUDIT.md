---
version: 0.1.0
lastReviewed: 2025-10-18
owner: kk
---

# 🧱 Repository & System Audit
Reference for maintaining documentation, governance, and CI integrity.  
Used occasionally (monthly or before major updates) — not part of weekly pilot tracking.

---

## ✅ 1. Structure & CI Health

| Checkpoint | Status | Notes |
|-------------|--------|-------|
| Folder naming normalized (lowercase) | ✅ | All dirs follow `workshop-templates` style |
| YAML front-matter consistent (`version`, `owner`, `lastReviewed`) | ✅ | Confirmed across active docs |
| `.github/workflows/version-bump.yml` passing | ✅ | CI runs clean on main |
| Markdown linting / front-matter validator | 🟡 | Optional GitHub Action for later |
| `/docs/README.md` index added | ⏳ | To be created once doc set stabilizes |

---

## 🧭 2. Governance Documents

| Area | Status | Next Step |
|-------|--------|-----------|
| Bylaws Template | 🟡 Drafted | Finalize & merge baseline version |
| Policies | 🟢 Live | Add quarterly review cadence |
| Team Framework | 🟢 Live | Add “Decision Rights” section |
| Versioning Policy | ✅ Active | No change needed |

---

## 🧩 3. Documentation System

| Focus | Current Status | Notes |
|--------|----------------|-------|
| Active docs reduced to 2 (Pilot Log + Repo Audit) | ✅ | Old files archived in `/meta/archive/` |
| Cross-links between major docs | 🟡 | Add once `/docs/README.md` exists |
| Accessibility / plain-language review | 🟡 | Quick clarity pass before public use |
| Contributor onboarding notes | 🟢 | Covered in `PILOT_LOG.md` friction actions |

---

## 🗂️ 4. Index Status

| Element | Status | Notes |
|----------|--------|-------|
| `/docs/README.md` index file | ⏳ | To be created once core docs stabilize |
| Cross-links between main docs | 🟡 | Add links after index is live |
| Section blurbs (1–2 lines per doc) | 🟡 | Write short summaries for clarity |
| Public readiness | 🔴 | Hold until pilot docs reviewed and finalized |

---

## 🧱 5. Content Completeness

| Document | Status | Action Needed |
|-----------|--------|---------------|
| `PILOT_LOG.md` | 🟢 Active | Update weekly during pilot |
| `TEAM_FRAMEWORK.md` | 🟢 Live | Add decision-rights details |
| `FACILITY_PLAN.md` | 🟡 In Progress | Add site shortlist + insurance notes |
| `BUDGET.md` | 🟡 Draft | Add OPEX projection after pilot |
| `POLICIES.md` | 🟢 Live | Add quarterly review cadence line |
| `BYLAWS_TEMPLATE.md` | 🟡 Draft | Merge after first governance review |

---

## 🪜 6. Current Priorities (Next 2 Weeks)
- Finalize pilot log structure and maintain weekly updates.  
- Normalize folder names + verify CI workflow remains green.  
- Add “Decision Rights” section to Team Framework.  
- Begin drafting `/docs/README.md` index outline.  
- Light pass for plain-language edits across key docs.

*(Deferred scope: replication, deep financial modeling, and advanced CI automations.)*

---

## 🌟 7. Success Markers
| Metric | Target | Verification |
|---------|---------|--------------|
| Repo alignment | 100% lowercase dirs + valid front matter | CI check |
| Governance | Bylaws + Policies merged | PR review |
| Facility readiness | Pilot lease plan drafted | Facility Plan update |
| CI health | 3 consecutive successful runs | GitHub Actions logs |

---

## 🔁 8. Review Rhythm
- **Monthly:** Quick scan for metadata drift + CI errors.  
- **Quarterly:** Governance doc check-in with Dan.  
- **As Needed:** Before major merges or funding submissions.

---

**Maintainer:** kk  
