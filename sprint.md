
## Sprint 2026-11-02

### Completed
- Confirmed `.venv` activation and Python path.
- Verified `rank_vessels_by_value()` in `analysis.py`.
- Verified statistical area `07-31` contains 10,709 catch records in the 2025 dataset.
- Added/verified Fleet Investigation in the Streamlit UI.
- Fleet ranking supports vessel-size filtering in `rank_vessels_by_value()`.
- Tested vessel-size selection in the UI.
- Confirmed DuckDB queries against the 2025 CSV work correctly.
- Established sprint-end routine: update sprint.md, commit, and push.

### Current state
- Streamlit application runs successfully.
- Fleet Investigation displays vessel rankings.
- Current filters include the existing sidebar filters plus Fleet Investigation vessel-size selection.
- Streamlit reports a deprecation warning for `use_container_width`; replace it later with `width="stretch"`.

### Next sprint
1. Review and clean up the filter architecture.
2. Connect Fleet Investigation more systematically to the main UI filters.
3. Add/verify gear filtering.
4. Add species and area selection in a controlled way.
5. Later: investigate dependent filter options, where available choices/counts respond to previous selections.
6. Keep the UI simple and understandable before adding advanced functionality.

### Notes
- Do not build dependent Booking.com-style filters yet; first make the underlying filter/query architecture solid.
- README does not require an update for this sprint.

## Sprint 2 — 2026-11-02

### Completed
- Reviewed the filter architecture in `app.py` and `analysis.py`.
- Identified that filter logic was split between the UI and analysis layer.
- Added `gear` as a filter parameter to `rank_vessels_by_value()`.
- Connected the Gear selection in `app.py` to Fleet Investigation.
- Verified that filtering by `Juksa/pilkki` changes the Fleet Investigation result from 82 vessels to 17 vessels.
- Verified the analysis code with direct Python tests.
- Added a total vessel count above the Fleet Investigation table.
- Verified the application runs successfully in Streamlit.
- Verified `app.py` and `analysis.py` with `py_compile`.

### Architecture
Current direction:

app.py
→ user selections
→ analysis.py
→ SQL filters
→ DuckDB
→ results

The goal is to gradually move filter logic toward the analysis layer rather than maintaining separate SQL filter logic in the UI.

### UX
Fleet Investigation now displays:

`Total vessels: N`

This makes the number of results immediately visible without requiring the user to discover that the table continues below the visible area.

### Known follow-up
- The main KPI query in `app.py` still has its own filter construction and should eventually be aligned with the analysis layer.
- Vessel-size filtering is still implemented differently in `app.py` and `analysis.py`.
- Species and area are still hard-coded for Fleet Investigation.
- Dependent/interactive filter options will be considered later, after the underlying architecture is stable.
- Streamlit still reports the `use_container_width` deprecation warning; this can be cleaned up later.

### Sprint result
The filter architecture is now one step closer to having a clear separation between UI selections and analysis/query logic.
## Sprint 3 – 2026-11-02

### Completed
- Continued filter architecture cleanup.
- Added `get_summary()` to move KPI query logic into the analysis layer.
- Connected Gear filtering to Fleet Investigation.
- Added Area selection to the UI.
- Verified statistical areas 07-31 and 07-32 against the dataset.
- Refactored Area handling in `app.py` so UI selection is converted into an `areas` parameter before calling the analysis layer.
- Verified 07-31 returns 82 vessels.
- Verified 07-32 returns 16 vessels.
- Verified `app.py` and `analysis.py` with `py_compile`.
- Verified the Streamlit UI after the changes.

### Sprint result
The filter flow is becoming cleaner:
UI selections → analysis layer → DuckDB → results.

Area and Gear are now passed explicitly into the analysis layer instead of being embedded directly in the Fleet Investigation query call.

### Next
- Continue consolidating filter logic in the analysis layer.
- Add species selection in a controlled way.
- Eventually remove the remaining duplicate filter/query logic from `app.py`.
- Later investigate dependent/interacting filter options.

