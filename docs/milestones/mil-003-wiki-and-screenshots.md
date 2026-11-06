# Wiki in three languages

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Review findings fixed: traceability to success criteria 4 and 5 (RC-005) | pending |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go per RC-005; language checks confirmed by S01 | pending |

---

## Purpose

Decide whether the wiki explains what each lecture step gained, in English,
Danish and Bahasa Malaysia, with a screenshot per step.

## Deliverable

`docs/wiki/` with the same page set in three languages (`Home`, `Setup`,
`Step-1-Current-Time`, `Step-2-Decorator-Skeleton`, `Step-3-Timing-Wrapper`,
`Step-4-Fast-vs-Slow`) and `_Sidebar.md`, reviewed against `QC-WIKI-001`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` is flat; every English page has a `-da` and a `-ms` page | Yes | No |
| 2 | Each page starts with the language switch line | Yes | No |
| 3 | Each step page shows its screenshot and a "What we gained" section | Yes | No |
| 4 | `_Sidebar.md` follows the framework's shape (English list, Languages last) | Yes | No |
| 5 | The wiki review against `QC-WIKI-001` is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs the screenshots and the finished lecture steps |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (wiki in three languages) | [BC-001] |
| Success criteria 4 and 5 (wiki languages, screenshots) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 — the Business Case target date.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki pages | Home, Setup and one page per lecture step. Each step page shows the screenshot and explains what was gained (time.time, closures, functools.wraps, decorators). English is the authoritative text. | No | |
| 2 | Translate wiki to Danish | Same page set as English with `-da` suffix, language line, code and commands unchanged. | No | |
| 3 | Translate wiki to Bahasa Malaysia | Same page set as English with `-ms` suffix, language line, code and commands unchanged. | No | |
| 4 | Add _Sidebar.md | One English page list, then a Languages section with Home links for en, da, ms. | No | |
| 5 | Check the wiki is enabled on the host | The publish workflow copies `docs/wiki/` to the host wiki after merge only if the wiki is enabled. Check the setting and report if it is off. | No | |

---

[BC-001]: ../business-case.md
