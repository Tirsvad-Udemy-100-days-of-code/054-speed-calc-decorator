# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-003], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0227b10] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003] deliverable, the wiki in `docs/wiki/` (18 pages and `_Sidebar.md`)
- Checklist used: [QC-WIKI-001] (`framework/qc/docs/wiki/` holds the framework's own wiki, not a checklist, so no second checklist applies)
- Scope: full review, 1 round, no defects found. Page content in Danish and Bahasa Malaysia was read for translation quality (the language checks of QC-LANG-001 apply to the page text); no language reviewer other than the stand-in
- Language and domain: en, da, ms / it (wiki pages)
- Language reviewer: none (the stand-in reads the three languages; `S01` confirmed the language checks for MIL-003 in RC-005)
- Mode: autonomous, not independent (reviewer `AI as stand-in for S01`)

Checks were run with a script that compares the pages: fenced code blocks, inline code spans and image URLs of each `-da` and `-ms` page against English (all identical), the language line of all 18 pages against the expected text, and every internal link against the files in the folder.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | `_Sidebar.md` exists | Pass | Present |
| 2 | Bold title, then one English list, `Home` first | Pass | `**Speed Calc Decorator**`, then Home, Setup, Steps 1 to 4 |
| 3 | List links every English page, no dead link | Pass | 6 links, 6 English pages, all targets exist |
| 4 | `Related` only when related wikis exist | Pass | No related wikis; no such section |
| 5 | `Languages` last, one line per language in its language, linking to Home | Pass | `English: [Home](Home)`, `Dansk: [Hjem](Home-da)`, `Bahasa Malaysia: [Utama](Home-ms)` |
| 6 | List not repeated per language | Pass | Listed once |
| 7 | Generated sidebar carries a generator comment | N-A | Written by hand, not generated |
| 8 | `Languages` line on each page (Optional) | Pass | See criterion 11 |
| 9 | English plus the PO language | Pass | English, Danish and Bahasa Malaysia; the Business Case names da and ms |
| 10 | Page sets identical | Pass | 6 pages x 3 languages |
| 11 | Language line on every page, current language bold, links to same page | Pass | 18 of 18 match the expected line; targets exist |
| 12 | Naming `<Page>-<code>.md`, English unsuffixed | Pass | `-da`, `-ms` suffixes, BCP 47 |
| 13 | Code, commands, file names, IDs stay English | Pass | Code blocks, inline code spans and image URLs identical to English in all 12 translations. Code comments such as `# seconds since Jan 1st, 1970` stay English as code |
| 14 | Checked on the published wiki after the change | Pass | 2026-11-06, after the merge and the publish workflow: the wiki API lists 19 pages (6 pages x 3 languages and `_Sidebar`); all 18 pages return HTTP 200 on the host; the `Step-3-Timing-Wrapper-ms` page links to the sibling pages in all three languages; `_Sidebar` and the `step-1` screenshot URL return 200. Checked by the AI as stand-in for S01 (an objective check, not a language judgement) |
| 15 | Layout change made in generator and checklist (Optional) | N-A | No layout rule changed |
| 16 | Folder flat | Pass | All 19 files directly in `docs/wiki/`, no subfolder |

Further findings:

- Internal links: every non-external link in all pages points to an existing file in the same language (content links keep the language suffix; only the language line crosses languages, as intended).
- Screenshots: the 4 image URLs (`raw/branch/main/docs/screenshots/...`) are the same in all languages and the 4 files exist in `docs/screenshots/`. The URLs resolve only after merge to `main`, which is part of criterion 14.
- Danish and Bahasa Malaysia read correctly and idiomatically; technical terms (decorator, closure, wrapper, float) are used consistently, and "What we gained" is rendered as "Hvad vi lærte" and "Apa yang kita peroleh". No errors found, nothing edited.

## MIL-003 Go criteria (verdict part excluded)

| # | Criterion | Status | Evidence |
| --- | --- | --- | --- |
| 1 | Flat; each English page has `-da` and `-ms` | Pass | Criteria 10 and 16 |
| 2 | Each page starts with the language switch line | Pass | Criterion 11; the line follows the title heading, as in the checklist example |
| 3 | Each step page shows its screenshot and a "What we gained" section | Pass | Steps 1 to 4 in all three languages have an image and the section (also `Setup`) |
| 4 | Sidebar shape | Pass | Criteria 2 to 6 |
| 5 | Review against QC-WIKI-001 is a Go | Pass | This record; see the verdict |

## Overall Verdict

Go. All Mandatory criteria pass and no defect was found. Criterion 14 was `Pending` until the wiki was published; it passed on 2026-11-06 after the merge (see its row). Mode: autonomous, not independent; reviewer AI as stand-in for S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Closed 2026-11-06: published wiki checked (criterion 14) | S01 | 2026-11-09 |

---

[MIL-003]: ../../milestones/mil-003-wiki-and-screenshots.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[0227b10]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/commit/0227b109d9b4031b137f6c1e7833ccbb8fd54f06
