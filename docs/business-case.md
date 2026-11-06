# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Review findings fixed: constraint wording, abbreviations spelled out (RC-001) | pending |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go per RC-001; language checks confirmed by S01 | pending |

---

## Executive Summary

Lecture 054 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp"
asks the participant to write a decorator, `speed_calc_decorator`, that prints
how many seconds a function takes to run, and to apply it to `fast_function`
and `slow_function`. This project turns that exercise into a small, tested,
documented repository that other course participants can read and run, and that
GitHub visitors can browse. It is a prototype: one Python package, a test suite,
a README and a three-language wiki that explains what each lecture step taught.

## Methodological and Standards Foundation

The documents follow the SQA and QC framework mounted at `framework/`
(Business Case, Stakeholder Analysis, Project Plan, milestones, then code).
Quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Source
code follows the `coding-conventions` skill (Python) and is documented with
Doxygen comments.

## Problem Statement

- The assignment gives only a stub (`def speed_calc_decorator(): pass`) and an
  expected output; there is no shared, runnable, tested solution layout.
- Participants who compare solutions find loose scripts without setup
  instructions, tests or an explanation of the decorator concepts involved.
- The author has no record of what each lecture step taught.

## Business Opportunity

A clean solution repository lets participants run the exercise in two commands,
lets visitors reuse the layout (`src/`, `tests/`, `docs/`) for other lectures of
the course, and gives the author a written record of the learning.

## Objectives

1. Deliver `speed_calc_decorator`, `fast_function` and `slow_function` with the
   assignment's names, printing output in the shape of the expected output.
2. Cover the behaviour with pytest tests that do not depend on real elapsed time.
3. Document how to create and use a local `.venv` and run the project and tests.
4. Provide a README and a wiki in English, Danish and Bahasa Malaysia that
   explain what each lecture step gained, with one screenshot per step.
5. Publish a repository description and topics on the git host.

## Scope

### In Scope

- Python package under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, Python `.gitignore`, `constants.py`, a `Doxyfile`.
- README from the framework template, with venv and test instructions.
- Wiki pages (en, da, ms) and one screenshot per lecture step.
- Repository description and topics on the git host.

### Out of Scope

- Other lectures of the course.
- Runtime dependencies, packaging to the Python Package Index (PyPI), a graphical user interface (GUI).
- Reading or importing the `.env` file in the project (personal use only).

## Expected Benefits

### Tangible Benefits

- A runnable solution: `python -m speed_calc` prints the expected output shape.
- A passing test suite and a documented setup.
- README and wiki in three languages with screenshots.

### Intangible Benefits

- Understanding of decorators, closures, `functools.wraps` and `time.time()`.
- A reusable layout for later lectures.

## Strategic Alignment

The project supports the author's goal of completing the 100 Days of Code course
with a documented portfolio on the author's git host, and supports the sharing
of solutions among course participants.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100 % of tests green | `python -m pytest` exits 0 |
| 2 | Program output | 3 lines in the shape of the assignment's expected output | `python -m speed_calc` run captured in the lecture-step screenshots |
| 3 | Runtime dependencies | 0 | `pyproject.toml` has an empty `dependencies` list |
| 4 | Wiki languages | 3 languages, same page set | file listing of `docs/wiki/` |
| 5 | Screenshots | 1 per lecture step in README and wiki | image files in `docs/screenshots/` |
| 6 | Repository metadata | Description and at least 5 topics set | git host application programming interface (API) response |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Timing tests are flaky on slow machines | Red continuous integration (CI) runs, false failures | Tests inject a fake clock and never assert real durations |
| Token in `.env` leaks | Account compromise | `.env` is git-ignored, never read by project code, never printed |
| Repository URL in the request differs from the configured `origin` | Metadata set on the wrong repository | Use the `origin` repository; the difference is recorded in Open Issues of [PP-001] |
| Translations contain mistakes | Misleading wiki text | Keep wording simple, English is authoritative, review by S01 |
| Screenshot capture on the host desktop disturbs the user | Interrupted work | Screenshots are rendered from captured program output, never from the desktop |

## Assumptions

- Python 3.13 or newer is installed on the author's machine.
- The git host accepts the token in `.env` for repository settings and pull requests.
- The wiki is enabled in the repository settings.
- The Product Owner is S01; S01 is the reviewer. The people for whom the work is
  intended (S02, S03) are not contacted for this prototype.

## Constraints

- Python 3.13 or newer, venv, pytest, `pyproject.toml`.
- No runtime dependencies.
- `constants.py` holds the constants.
- Folder structure `src/`, `tests/`, `docs/`.
- One pull request (branch) per milestone.
- Target: finished by 2026-11-09.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of effort | Complete, shareable solution and learning record |
| No licence or infrastructure cost | Reusable layout for later lectures |

The assessment is qualitative: this is a personal learning project with no
revenue, so numbers would add no information.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owner, developer and reviewer; wants a correct exercise and a learning record |
| S02 | Reads and runs the code; wants the assignment's function names and clear run instructions |
| S03 | Browses for ideas; wants a clear description, topics and README with no dependencies |

## Recommendation

Proceed — the scope is small, the dependencies are none, and the outcome serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
