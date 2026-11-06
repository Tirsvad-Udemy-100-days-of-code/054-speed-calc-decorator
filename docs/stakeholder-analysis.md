# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Review findings fixed: CN-007 traced to success criterion 3, abbreviations (RC-002) | pending |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go per RC-002; language checks confirmed by S01 | pending |

---

## Purpose

This analysis names the people the project serves and what each needs, so that
owners, reviewers and tasks can cite stable IDs. It uses the power/interest grid
and maps concerns to FURPS+ (Functionality, Usability, Reliability, Performance,
Supportability, plus design, implementation, interface and physical constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen (course participant) | Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct exercise solution and a record of what was learned |
| S02 | Udemy coursists | Fellow participants who share and compare code | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README run instructions |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes, reviews and accepts everything.
- **Keep Informed (S02):** no authority over the project, but depends on its
  clarity; the README and wiki are the channel.
- **Monitor (S03):** casual visitors with no stake beyond a good first
  impression; the description, topics and README serve them.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The decorator prints the time a function takes, like the expected output | Functionality |
| CN-002 | S01 | Tests prove the behaviour without depending on real elapsed time | Reliability |
| CN-003 | S01 | The learning of each lecture step is written down in three languages | Supportability |
| CN-004 | S02 | Function names match the assignment (`speed_calc_decorator`, `fast_function`, `slow_function`) | Functionality |
| CN-005 | S02 | Setup and run instructions with a local `.venv` are easy to follow | Usability |
| CN-006 | S03 | Repository description, topics and README explain the project at a glance | Usability |
| CN-007 | S03 | The project installs and runs with no runtime dependencies | Implementation |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Pull request review | One per milestone | Pull request with the milestone's changes | MIL-001, MIL-002, MIL-003 |
| CR-002 | README | Updated per milestone | Run and test instructions with screenshots | MIL-001, MIL-002 |
| CR-003 | Wiki (en, da, ms) | Once | Lecture-step explanations with screenshots | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the exact assignment shape, S01 wants well-structured code (package, constants, tests) | S01, S02 | Keep the assignment's function names and output; add structure around them |
| S01 wants a thorough wiki in three languages, S03 wants a short entry point | S01, S03 | README is short and links to the wiki for detail |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 and 2 |
| S01 | CN-003 | [BC-001] objective 4 |
| S02 | CN-004 | [BC-001] objective 1 |
| S02 | CN-005 | [BC-001] objective 3 |
| S03 | CN-006 | [BC-001] objectives 4 and 5 |
| S03 | CN-007 | [BC-001] success criterion 3 (0 runtime dependencies) and the constraint "No runtime dependencies" |

## Sign-Off

Product Owner: S01, accepted 2026-11-06 via RC-002.

---

[BC-001]: ./business-case.md
