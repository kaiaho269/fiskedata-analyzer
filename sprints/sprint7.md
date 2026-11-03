# Sprint 7 — Geography architecture pivot

## Goal
Test whether official statistical sea areas were suitable as the primary representation of fishing grounds.

## Work completed
- Documented the limitation of using statistical areas as a proxy for real fishing grounds.
- Established that primary geography should eventually combine AIS activity, landing locations, vessel identity and catch data.
- Kept statistical areas as official secondary/reference geography.

## What we learned
A statistical grid cell is a reporting construct, not necessarily a physical fishing ground. Treating it as one would create false precision.

## Direction change
The architecture pivoted from:

`statistical area → fishing ground`

toward:

`AIS activity → vessel → catch → landing`

## Result
This was a strategic architecture decision, not merely a UI change. It protects FA from building its core model around the wrong geography.

## Git
`3c6098642334080916e040c82fb9bda4a23e31d3` — Document geography architecture pivot
