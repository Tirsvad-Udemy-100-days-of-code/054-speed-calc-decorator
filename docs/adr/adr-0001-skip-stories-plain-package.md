# Skip user stories and use cases; plain package layout

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [a07d05b] |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Review RC-006 fixed 2 defects (stakeholder IDs S01 to S03 now explained; shared rationale for the two decisions stated in Context); accepted as stand-in for S01 in autonomous mode, not independent | [a07d05b] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project solves one course exercise: a decorator that prints how long a
function takes. Two decisions shape the plan and the code; both follow from one force: the
documentation and structure should stay in proportion to a one-function exercise.

1. **User stories and use cases.** The framework asks for candidate stories and
   use cases before milestones. The exercise has one actor (S01, the author and Product Owner)
   running one command, with no input and no state. Options: (a) write a story and use case
   for "run the timing demo"; (b) skip them and plan plain technical tasks.
2. **Code layout.** The `clean-architecture` skill describes layers (domain,
   application, infrastructure, presentation). Options: (a) the full layers;
   (b) one small package, `src/speed_calc/`, with a module per concern.

Forces: the target is a prototype to finish by 2026-11-09; stakeholders S02 (Udemy
coursists) and S03 (GitHub viewers) want readable code with the assignment's function names and no runtime
dependencies; layers would hide the three functions the course asks for.

## Decision

Skip user stories and use cases, and plan every task as a plain technical task
(`Needs its own Use Case/User Story?` is `No`). Use one flat package
`src/speed_calc/` with `constants.py`, the decorator, the two demo functions and
a `__main__` entry point; apply the dependency rule by keeping the decorator
free of any import from the demo or entry modules.

## Consequences

**Positive:**

- Less documentation than the code it describes; readers (S02, S03) find the
  three assignment functions at once.
- No runtime dependencies and nothing to configure.

**Negative:**

- The layout does not scale to a larger program; a later lecture project with
  real use cases needs its own decision.
- No story-level traceability; traceability stops at the milestone task.

## Affected Artifacts

- [BC-001] — scope stays as written; no story-level scope items exist.
- [PP-001] — the Stories column says "none" and points here.

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[a07d05b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/commit/a07d05b385e6b831b90731aefe08f078ebb951ca
