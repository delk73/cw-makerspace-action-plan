# 🧭 TODO

*(v2025-10-18 · excluding food model)*

## 1. Structural Audit — Repo Organization & CI

**Findings**

* ✅ Logical directory structure: `/docs`, `/ops`, `/funding`, `/programs`, `/meta`, `/scripts`, `.github`
* ✅ YAML front-matter consistently defines `version`, `owner`, and `lastReviewed`
* ⚠️ Some naming inconsistencies (`WORKSHOP_TEMPLATES` vs. `workshop-templates`)
* ⚠️ Redundant governance placeholders under `/docs/governance`
* ✅ CI auto-bump (`scripts/bump_doc_versions.py`) working and versioned in `.github/workflows/version-bump.yml`

**Actions**

| Priority  | Task                                                          | Est. Effort | Notes                            |
| --------- | ------------------------------------------------------------- | ----------- | -------------------------------- |
| 🔴 High   | Normalize all folder naming (`workshop-templates`, lowercase) | 1h          | Avoid CI path mismatches         |
| 🟠 Medium | Add lightweight README index per subdir                       | 1h          | For GitHub browsing clarity      |
| 🟢 Low    | Auto-lint markdown front-matter consistency                   | 2h          | Optional `md-lint` GitHub Action |

---

## 2. Content Audit — Phases, Goals, and Milestones

**Findings**

* Phase breakdown clear in root README (Alignment → Core Team → Build-Out → Operations)
* Docs like `PILOT_SMOKE_MAP.md`, `TEAM_FRAMEWORK.md`, and `FACILITY_PLAN.md` are actionable
* Budget coverage reasonable; missing ongoing OPEX tracking template
* Workshop templates good start but need consistent format
* Outreach & recruitment materials strong early drafts

**Actions**

| Priority  | Task                                                        | Est. Effort | Notes                                      |
| --------- | ----------------------------------------------------------- | ----------- | ------------------------------------------ |
| 🔴 High   | Complete & verify `PILOT_SMOKE_MAP.md` friction scoring     | 2h          | Clarify “green/yellow/red” readiness tiers |
| 🔴 High   | Refine `TEAM_FRAMEWORK.md` for decision rights & escalation | 1.5h        | Needed before governance lock-in           |
| 🟠 Medium | Expand `BUDGET.md` for monthly cost projection              | 2h          | Keep under 1-page constraint               |
| 🟠 Medium | Finalize `FACILITY_PLAN.md` for short-term lease pilot      | 1.5h        | Include zoning + insurance checklist       |
| 🟢 Low    | Add short blurbs in `programs/workshop-templates`           | 1h          | Just key outcomes & duration per template  |

---

## 3. Governance Alignment — Ownership, Versioning, Cadence

**Findings**

* Versioning automated via `version.json` (currently 0.1.x)
* Governance docs exist but not yet finalized (`BYLAWS_TEMPLATE.md`, `POLICIES.md`)
* CODEOWNERS + MAINTAINERS.yml correctly define default review roles
* Missing meeting cadence / review log pattern

**Actions**

| Priority  | Task                                                      | Est. Effort | Notes                      |
| --------- | --------------------------------------------------------- | ----------- | -------------------------- |
| 🔴 High   | Finalize `BYLAWS_TEMPLATE.md` with minimum viable charter | 3h          | Core governance baseline   |
| 🟠 Medium | Add quarterly cadence to `POLICIES.md` (“review cycle”)   | 1h          | Ensure living-doc rhythm   |
| 🟢 Low    | Add `meta/governance_log.md` for review snapshots         | 0.5h        | Helps maintain audit trace |

---

## 4. Debt Reduction Roadmap — Prioritized Focus

### Phase 1 (Next 2 weeks)

* ✅ Complete **Pilot Smoke Map**
* ✅ Normalize directory names & README index
* ✅ Tighten **Team Framework**
* ⏳ Finalize **Facility Pilot** details
* 💡 Deliver lightweight **Budget OPEX v1**

### Phase 2 (Next month)

* 🚀 Approve governance core (Bylaws + Policies)
* ⚙️ Integrate CI front-matter validator
* 📘 Expand program templates and outreach docs

---

## 5. Removed / Deferred Scope

* ❌ **Food Model** — cut for agility; revisit in post-launch community phase
* ❌ Deep OPEX/Revenue modeling — postpone until core funding secured
* ❌ Full multi-phase café model — not in pilot scope

---

## 6. Outcome Targets

| Metric             | Target                                    | Verification          |
| ------------------ | ----------------------------------------- | --------------------- |
| Repo alignment     | 100% lower-case dirs + valid front-matter | `md-lint` check       |
| Governance         | Bylaws + Policies merged to main          | Reviewed PR           |
| Facility readiness | Pilot lease plan reviewed                 | Facility doc sign-off |
| CI health          | Auto-bump runs green 3 cycles             | GitHub Actions logs   |
