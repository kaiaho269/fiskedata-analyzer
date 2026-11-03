# Sprint 13 — Data-driven species filter

## Goal
Remove the hard-coded species limitation from the FA species filter.

## Work completed
- Queried the 2025 dataset and found 33 distinct `Art - gruppe` values.
- Added `get_species()` to `analysis.py`.
- Changed the Streamlit species dropdown to use the dataset as its source.
- Added an `All species` UI option.
- Translated `All species` into analytical `None` instead of treating it as a species value.
- Verified different species selections in `07-31`.

## Test results
- Hyse: 64 vessels
- Torsk: 76 vessels
- All species: 137 vessels

## What we learned
Values already present in the dataset should not be hard-coded into the UI when they can be discovered dynamically.

The important architectural distinction is:

`UI vocabulary → analytical value`

For example, `All species` is a UI concept; `None` is the analytical meaning of no species filter.

## Result
The species filter is now data-driven and can accommodate additional species without changing the UI code.

## Git
`32f97b564719e905cbefe93f42451ac5558c7c57` — Make species filter data-driven
