# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version: BC, SA, PP, MIL-001 to MIL-003 and RC-001 to RC-005 | [a07d05b] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [SA-001] | Stakeholder Analysis | en | it | - | [BC-001], [PP-001] | [RC-002] (Go) |
| [BC-001] | Business Case | en | it | [SA-001] | [PP-001], [MIL-001], [MIL-002], [MIL-003] | [RC-001] (Go) |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - (no review gate; accepted by S01 through the accepted plan) |
| [MIL-001] | Milestone / Gateway | en | it | [BC-001], [PP-001] | [MIL-002]; source code is not built yet; ADR-0001 is written | [RC-003] (Go) |
| [MIL-002] | Milestone / Gateway | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003]; source code and tests are not built yet | [RC-004] (Go) |
| [MIL-003] | Milestone / Gateway | en | it | [BC-001], [PP-001], [MIL-002] | - | [RC-005] (Go) |
| [ADR-0001] | Architecture Decision Record | n/a | n/a | [BC-001], [PP-001] | source code and tests are not built yet | [RC-006] (Go) |
| [RC-001] | SQA Review Record | - | - | [BC-001] | - | - |
| [RC-002] | SQA Review Record | - | - | [SA-001] | - | - |
| [RC-003] | SQA Review Record | - | - | [MIL-001] | - | - |
| [RC-004] | SQA Review Record | - | - | [MIL-002] | - | - |
| [RC-005] | SQA Review Record | - | - | [MIL-003] | - | - |
| [RC-006] | SQA Review Record | - | - | [ADR-0001] | - | - |

## Concern Coverage

No view (architecture, design or use case artifact) exists yet, and none is planned
before the milestones: the exercise is one function and the reason for skipping
user stories and use cases is recorded in ADR-0001, a task of [MIL-001]
(accepted). Each concern is delivered by a milestone Go criterion; that is
noted in the first column. There is no Architecture Description, so the gaps
are not listed there.

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | none; delivered by [MIL-002] Go criteria 1 and 2 | none (ADR-0001 does not address it) | none | Gap |
| CN-002 | none; delivered by [MIL-002] Go criterion 1 | none (ADR-0001 does not address it) | none | Gap |
| CN-003 | none; delivered by [MIL-003] Go criteria 1 to 3 | none (ADR-0001 does not address it) | none | Gap |
| CN-004 | none; delivered by [MIL-002] Go criterion 3 | none (ADR-0001 does not address it) | none | Gap |
| CN-005 | none; delivered by [MIL-001] Go criterion 3 | none (ADR-0001 does not address it) | none | Gap |
| CN-006 | none; delivered by [MIL-001] Go criteria 3 and 5 | none (ADR-0001 does not address it) | none | Gap |
| CN-007 | none; delivered by [MIL-001] Go criterion 1 and [MIL-002] Go criterion 6 | none (ADR-0001 does not address it) | none | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [SA-001], [BC-001] | CN-007 (no runtime dependencies) was traced to Business Case objective 3 (venv and run instructions), which does not cover it | [RC-002] | Closed | [SA-001] version of 2026-11-06 |
| 2 | [BC-001] | The constraint "No runtime dependencies unless needed" contradicted success criterion 3 (0 runtime dependencies) | [RC-001] | Closed | [BC-001] version of 2026-11-06 |
| 3 | [PP-001], [MIL-002] | The plan placed `constants.py` at [MIL-001], while [MIL-002] task 1 creates it | informal review of [PP-001] (no RC) | Closed | [PP-001] version of 2026-11-06 |

## Coverage Notes

- Types with no instance yet: KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, TP, AD, GOV, DICT. User stories and use cases are skipped on purpose (recorded in [ADR-0001]); GOV and DICT are not in the plan, which leaves QC-LANG-001 criterion 5 without a dictionary to check against.
- `-` in Upstream means foundational; in Downstream, nothing is built on it yet; in Last Reviewed, no `RC-*` exists yet.
- All five reviews are `Mode: autonomous, not independent` and `Go`: S01 confirmed criteria 3, 5 and 9 of QC-LANG-001 as a person in chat on 2026-11-06, so BC-001, SA-001 and MIL-001 to MIL-003 are `Accepted`.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-baseline.md
[MIL-002]: ../milestones/mil-002-speed-calc-decorator.md
[MIL-003]: ../milestones/mil-003-wiki-and-screenshots.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-project-baseline.md
[RC-004]: ./reviews/rc-004-mil-002-speed-calc-decorator.md
[RC-005]: ./reviews/rc-005-mil-003-wiki.md
[RC-006]: ./reviews/rc-006-adr-0001.md
[ADR-0001]: ../adr/adr-0001-skip-stories-plain-package.md
[a07d05b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/commit/a07d05b385e6b831b90731aefe08f078ebb951ca
