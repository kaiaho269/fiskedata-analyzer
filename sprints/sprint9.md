# Sprint 9 — Fleet investigation and filter foundation

## Goal
Make Fleet Investigation usable with real filter selections and establish a repeatable sprint routine.

## Work completed
- Confirmed the Python environment and analysis functions.
- Verified `07-31` contains 10,709 catch records in the 2025 dataset.
- Connected Fleet Investigation to vessel-size filtering.
- Tested the filter in Streamlit.
- Confirmed DuckDB queries against the 2025 CSV.
- Established the sprint-end routine: update documentation, commit and push.

## What we learned
The UI needed a clear separation between selections and the analytical query. The project was ready for a deliberate filter-architecture cleanup rather than more ad-hoc UI logic.

## Direction
Next priority became filter architecture, with dependent/interactive filters deliberately postponed until the underlying query flow was sound.

## Result
Fleet Investigation became a working, testable part of the application.

## Git
`53dafe70b97ee0e546ebb5d053ad27261335e03f` — Sprint 2026-11-02: fleet investigation and filters
