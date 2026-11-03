# Sprint 10 — Filter architecture cleanup

## Goal
Move filter/query responsibility toward the analysis layer and away from duplicated UI logic.

## Work completed
- Reviewed filter construction in `app.py` and `analysis.py`.
- Added gear as an explicit parameter to `rank_vessels_by_value()`.
- Connected Gear selection to Fleet Investigation.
- Verified `Juksa/pilkki` filtering changed the fleet from 82 to 17 vessels.
- Added a visible total vessel count.
- Tested the application and compiled both Python files.

## Architecture
The intended flow became:

`app.py → user selections → analysis.py → SQL filters → DuckDB → results`

## What we learned
Keeping filter logic in two places creates drift. The UI should describe intent; the analysis layer should implement it.

## Result
The filter architecture became cleaner and more testable, with remaining duplication explicitly identified for later removal.

## Git
`e3cb6b6852328d9187348efc650f357fd9d25798` — Sprint 2: clean up filter architecture
