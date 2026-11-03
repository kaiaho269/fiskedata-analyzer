# Sprint 11 — Consolidate summary and filter handling

## Goal
Continue the separation between UI controls and the analytical engine.

## Work completed
- Added `get_summary()` so KPI query logic moved into the analysis layer.
- Added/verified Area selection.
- Passed Area explicitly as an `areas` parameter.
- Verified `07-31` returns 82 vessels and `07-32` returns 16 vessels in the relevant test state.
- Continued cleanup of duplicated query/filter construction.
- Verified the application with compilation and Streamlit tests.

## What we learned
The clean architecture is not theoretical: every filter moved into the analysis layer removes one more place where the UI and analytical truth can disagree.

## Direction
Continue consolidating filters, then make species selection data-driven.

## Result
UI selections increasingly became a thin control layer over the analytical engine.

## Git
`64d896159d3023e68faa6e0af5ff9555bf7520c0` — Clean up filter architecture
