# Project baseline and repository

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Review findings fixed: Go criterion 6 for ADR-0001, traceability to success criteria (RC-003) | [a07d05b] |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go per RC-003; language checks confirmed by S01 | [a07d05b] |

---

## Purpose

Decide whether the repository is ready for code: configuration, documentation
skeleton and repository metadata exist and follow the Business Case constraints.

## Deliverable

`pyproject.toml`, Python `.gitignore`, `Doxyfile`, README from the framework
template with venv instructions, ADR-0001, and the repository description and
topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.13 or newer, has no runtime dependencies and a pytest dev extra | Yes | No |
| 2 | `.env` is git-ignored and `git ls-files` does not list it | Yes | No |
| 3 | README follows the template and documents `.venv`, `python -m pip install --upgrade pip` and pytest | Yes | No |
| 4 | `Doxyfile` exists with `INPUT = src` | Yes | No |
| 5 | The git host application programming interface (API) returns a non-empty description and at least 5 topics | Yes | No |
| 6 | ADR-0001 exists, records why user stories and use cases are skipped, and its review is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 (venv and run instructions) | [BC-001] |
| Objective 5 (description and topics) | [BC-001] |
| Success criteria 3 and 6 (0 runtime dependencies; repository metadata) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-06 — within the Business Case target of 2026-11-09.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Record ADR-0001: skip user stories and use cases | The exercise is a single function with no user interaction, so stories and use cases add no information. Record the reason and the plain package layout (no clean-architecture layers) in an architecture decision record (ADR). | No | |
| 2 | Add pyproject.toml and venv setup | Configure the project for Python 3.13 or newer with the `src/` layout, no runtime dependencies, pytest as a dev extra, and pytest settings for `tests/`. | No | |
| 3 | Add Python .gitignore | Ignore `.venv`, caches, build output and `.env` so the personal token file is never committed. | No | |
| 4 | Add Doxyfile | Configure Doxygen to read `src/` and write `docs/doxygen/`, so the Doxygen comments in the source can be rendered. | No | |
| 5 | Write README from the framework template | Fill the template: overview, requirements, creating and using a local `.venv`, `python -m pip install --upgrade pip`, run and test commands, links. Screenshots are added in MIL-002. | No | |
| 6 | Set repository description and topics | Use the git host API with the token from `.env` (read by the shell only, never by the project or printed) to set a description and topics on the `origin` repository. | No | |

---

[BC-001]: ../business-case.md
[a07d05b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/commit/a07d05b385e6b831b90731aefe08f078ebb951ca
