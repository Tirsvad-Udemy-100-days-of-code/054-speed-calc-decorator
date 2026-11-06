# RC-007 Review of the Python source and tests of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [QC-PY-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the Python code under `src/speed_calc/` and `tests/`, plus the dev tool `docs/screenshots/generate_screenshots.py`, delivered by [MIL-002] (source code has no instance ID)
- Checklist used: [QC-PY-001]
- Scope: full review. Round 1 found one defect (criterion 4, unannotated tests), fixed in the tests; round 2 re-checked every criterion and is shown here.
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; S01 is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `ruff` rule set N (pep8-naming) passes; modules snake_case, `FAST_ITERATIONS` UPPER_SNAKE |
| 2 | Names state purpose in the domain's language | Pass | `speed_calc_decorator`, `make_speed_calc_decorator`, `RESULT_TEMPLATE`; loop variable `i` is a tiny scope |
| 3 | Formatter and linter, no unexplained suppressions | Pass | `ruff check src tests docs/screenshots`: All checks passed; `ruff format --check`: 10 files formatted. One `# type: ignore[attr-defined]` in `lecture_steps.py`, with the reason in the comment above it |
| 4 | Every signature type-annotated, including `-> None` | Pass | Round 1 Fail: tests had no annotations. Fixed in round 2 (`-> None`, `pytest.CaptureFixture[str]`, `make_clock` return type); `mypy --strict tests src`: no issues in 9 files |
| 5 | No bare `except:`, no swallowed exceptions | Pass | No `try`/`except` in the code |
| 6 | No mutable defaults, no shadowed builtins | Pass | Defaults are `time.time` and `print`; ruff B passes; no builtin is shadowed |
| 7 | Context managers for files, locks, connections | N-A | No resources are opened (the screenshot tool uses `subprocess.run` and `Image.save`, which need none) |
| 8 | Docstrings that say what, not how | Pass | Every module, function and constant has a Doxygen comment (`@brief`, `@param`, `@return`) |
| 9 | Logging uses `logging`, not `print`; no secrets | Pass | `print` is the assignment's required program output (`python -m speed_calc` prints the time and timing lines), not diagnostics; the decorator takes an injectable `output`. No secrets or personal data are printed |
| 10 | Classes and operations trace to the DCD | N-A | No DCD exists by decision ([ADR-0001]); the four functions trace to MIL-002 criterion 3. `make_speed_calc_decorator` and `lecture_steps` are additions for tests and screenshots, recorded in MIL-002 tasks 3 and 6 |
| 11 | Tests for new behaviour, named for behaviour, independent of order and network | Pass | `pytest -q`: 12 passed; fake clock gives exact values; no network, no shared state |
| 12 | Type checker strict, `Any` justified | Pass | `mypy src` (strict = true in `pyproject.toml`): Success, no issues in 6 source files. `Any` in `decorator.py` has the comment that a decorator accepts any function's arguments |
| 13 | Dependencies declared and pinned, none unused | Fail | Optional. `dependencies = []`; the dev extras use lower bounds (`pytest>=8`) and are not pinned. Pillow is used by the screenshot tool. Non-blocking; accepted for a learning exercise |
| 14 | Each piece of knowledge defined once | Pass | Loop sizes and the line format are only in `constants.py`; both demo loops are alike but change independently |
| 15 | Imports point inward, no cycles | Pass | `constants` <- `decorator` <- `demo_functions` <- `__main__`/`lecture_steps`; no cycle, no framework in business modules |
| 16 | SOLID holds | Pass | The decorator receives clock and output (dependency inversion); each module has one reason to change |
| 17 | Clean architecture layers and folders | Pass | Flat package `speed_calc` with a flat `tests/`, by decision in [ADR-0001] (layers would hide the three functions the course asks for); the criterion accepts a merged layer when an ADR says why. Imports still point inward |
| 18 | File and folder names English, no space, language casing | Pass | `decorator.py`, `demo_functions.py`, `test_*.py`, `generate_screenshots.py`, `step-1-current-time.png`: English, no space, snake_case or hyphen |

## MIL-002 Go criteria

| # | Criterion | Result | Evidence |
| --- | --- | --- | --- |
| 1 | `pytest` exits 0 | Go | 12 passed in the project `.venv` (fresh-venv install not repeated) |
| 2 | `python -m speed_calc` output | Go | Printed `1793943250.9...`, then `fast_function run speed: 0.017...s` and `slow_function run speed: 0.173...s` |
| 3 | Function names | Go | `speed_calc_decorator`, `fast_function`, `slow_function`; test `test_function_names_match_the_assignment` |
| 4 | Constants only in `constants.py`; Doxygen comments | Go | No numeric or format literals elsewhere; all modules carry Doxygen comments (`doxygen Doxyfile` not run) |
| 5 | 4 screenshots referenced in README | Go | 4 PNG files in `docs/screenshots/`; README lines 97, 104, 110, 117 reference them |
| 6 | No runtime dependencies | Go | `dependencies = []` |

## Overall Verdict

Go. The only Fail is criterion 13, which is Optional and so not blocking. Round 1 found a Mandatory Fail on criterion 4 (unannotated tests); it was fixed and re-checked in round 2. Criteria 7 and 10 are N-A with reasons. The review is `Mode: autonomous, not independent`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin or bound the dev dependencies if the project is kept beyond the exercise (criterion 13, Optional) | S01 | 2026-11-09 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-002]: ../../milestones/mil-002-speed-calc-decorator.md
[ADR-0001]: ../../adr/adr-0001-skip-stories-plain-package.md
