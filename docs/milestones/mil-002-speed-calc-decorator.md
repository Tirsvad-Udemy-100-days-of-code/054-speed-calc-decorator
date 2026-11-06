# Speed calc decorator

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Review findings fixed: traceability to success criteria and constraints (RC-004) | pending |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go per RC-004; language checks confirmed by S01 | pending |

---

## Purpose

Decide whether the exercise is solved: the decorator works, is tested, and each
lecture step has a screenshot in the README.

## Deliverable

Package `speed_calc` under `src/` (`constants.py`, the decorator, `fast_function`,
`slow_function`, a `__main__` entry point), tests under `tests/`, and one
screenshot per lecture step in `docs/screenshots/`, shown in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` exits 0 in a fresh `.venv` | Yes | No |
| 2 | `python -m speed_calc` prints the current time and two lines of the form `<name> run speed: <seconds>s` | Yes | No |
| 3 | Function names are `speed_calc_decorator`, `fast_function`, `slow_function` | Yes | No |
| 4 | Constants are only in `constants.py`; source has Doxygen comments | Yes | No |
| 5 | `docs/screenshots/` has 4 images, one per lecture step, referenced in the README | Yes | No |
| 6 | `pyproject.toml` lists no runtime dependencies | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project configuration and README skeleton |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 (function names, tests) | [BC-001] |
| Objective 4 (one screenshot per step, README part) | [BC-001] |
| Success criteria 1, 2, 3 and 5 (tests, output, 0 runtime dependencies, screenshots) | [BC-001] |
| Constraint: `constants.py` holds the constants; Doxygen comments (Methodological and Standards Foundation) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-07 — within the Business Case target of 2026-11-09.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Lecture step 1: print the current time | Create the package and `constants.py`, and print `time.time()` as in the starting code. Test with a fake clock. | No | |
| 2 | Lecture step 2: decorator skeleton | Write `speed_calc_decorator(function)` that returns a wrapper calling the function and preserving its metadata with `functools.wraps`. Test that the result and name are preserved. | No | |
| 3 | Lecture step 3: time the call | Make the wrapper read the clock before and after the call and print `<name> run speed: <seconds>s`. The clock is injectable so the test asserts exact values. | No | |
| 4 | Lecture step 4: fast vs slow | Add `fast_function` (range 1,000,000) and `slow_function` (range 10,000,000) with the decorator, and the `__main__` entry point that prints the expected output shape. Constants live in `constants.py`. | No | |
| 5 | Doxygen comments on all source | Document modules, functions and constants with Doxygen-style comments, and check that `doxygen Doxyfile` runs without warnings if Doxygen is installed. | No | |
| 6 | Screenshots per lecture step | Render each step's real program output to a Portable Network Graphics (PNG) image in `docs/screenshots/` with a dev-only script (no host desktop capture), and add them to the README. | No | |
| 7 | Update README with run and test output | Add the four screenshots, the run command and the test command with expected results. | No | |

---

[BC-001]: ../business-case.md
