# Sprint 15 — Baseline review and planning (closed / paused)

## Goal
Review the current analysis and UI behavior, agree on the expected filter-classification model, and prepare stabilization work.

## Work completed
- Inspected `analysis.py`, `app.py`, `SPRINT.md` and the Sprint 14 audit record on `copilot/sprint-15`.
- Documented current filter behavior and identified the mismatch between KPI calculations and the vessel ranking.
- Identified that the ranking filters by `Lengdegruppe (kode)` while the KPI summary uses a numeric `Største lengde < 11` check for the under-11-m option.
- Recorded the code's current length-group mapping without treating it as verified source-data documentation.
- Agreed on three record classifications: Confirmed, Excluded and Unknown.
- Agreed that missing information should make a record Unknown only when it is needed to evaluate an active filter. Missing vessel ID does not imply that every other field is unknown.
- Agreed that unknown reasons should be extensible, support multiple reasons per record, and be reported separately rather than silently included or discarded.
- Clarified that confirmed catch-record counts are separate from the confirmed vessel population; vessel count and ranking must use the same identifiable confirmed vessels.
- Decided to pause implementation until the user can access the local 2025 dataset and laptop at home.

## Changes
- Documentation only: updated `SPRINT.md` to mark Sprint 15 closed/paused and set Sprint 16 as the next sprint; added this sprint record.
- No application code or automated tests were changed.

## Tests and results
- No automated tests were run or added.
- No tests against the full 2025 dataset were run in this environment. The CSV is local to the user's laptop and was unavailable while travelling.
- Checkpoint A (baseline inspection and behavior review) was completed. Checkpoints B, C and D were not performed.
- Existing values in Sprint 14 remain historical results; they were not revalidated as part of this sprint.

## Decisions and limitations
- Do not equate length-group code values with numeric length ranges until their meanings are verified from the dataset's source documentation or data on the user's laptop.
- Implementation and expected-result tests require access to the actual local data fields and manually verified fixtures.
- This sprint is closed as a deliberate pause, not as completion of the planned stabilization implementation.

## Remaining work for Sprint 16
1. With the laptop and data available, verify/document length-group codes and field semantics.
2. Finalize the Confirmed / Excluded / Unknown rules using actual available fields and active filters.
3. Preserve multiple uncertainty reasons per record without implementing a full data-quality dashboard.
4. Implement shared, parameterized filter logic in the analysis layer.
5. Keep confirmed catch-record metrics separate from the confirmed identifiable vessel count/ranking.
6. Add automated tests with manually verified expected results, then test against the local dataset as feasible.
7. Investigate connection/CSV loading behavior, document actual results, and review the complete diff before any PR.

## Git
Documentation-only closeout on `copilot/sprint-15`. No merge to `main` is authorized by this record.
