# Sprint 14 – Architecture and UI audit

## Goal
Audit the current FA architecture, application behaviour
and identify priorities for the next development sprint.

## Work completed
- Verified Git repository, SSH authentication and clean working tree.
- Reviewed SPRINT.md and strategy.md.
- Inspected repository structure.
- Inspected analysis.py and app.py.
- Started the existing Streamlit application.
- Tested vessel length, gear, species and area filters.
- Confirmed that Fleet Investigation responds to filter changes.

## Test results

Dataset:
- Catch records: 974,502
- Unique vessels: 4,591

Filter tests:
- Under 11 m, area 07-31: 108 vessels.
- Under 11 m, Juksa/pilk, area 07-31: 14 vessels.
- Above filters + Sei: 11 vessels.
- Above filters + area 07-32: 3 vessels.

## Findings

1. KPI metrics do not reflect all active filters.
2. Fleet Investigation responds to all four filters.
3. KPI and fleet results therefore describe different datasets.
4. analysis.py contains six analytical functions.
5. app.py contains UI logic and a separate DuckDB connection.
6. SQL query construction requires a security review.
7. CSV loading and DuckDB connection handling require investigation.
8. No dedicated automated test directory was found.
9. Streamlit reports a deprecated use_container_width parameter.

## What we learned

The current application works and provides a useful
foundation for further development.

However, analytical consistency must take priority
over adding new UI features.

KPI metrics must always describe the same filtered
dataset as the Fleet Investigation results.

## Result

FA is operational, but the analytical architecture
requires further stabilization and testing.

No application code was modified during this sprint.

## Next sprint – Proposed work

1. Correct KPI filtering across all four dimensions.
2. Establish shared filtering logic in the analysis layer.
3. Review SQL parameterization and query safety.
4. Investigate DuckDB connection and CSV loading strategy.
5. Introduce automated analytical tests.
6. Document the current architecture.

## Git
Documentation and audit findings only.
