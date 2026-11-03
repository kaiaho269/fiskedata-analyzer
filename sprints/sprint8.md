# Sprint 8 — Landing and buyer-register investigation

## Goal
Understand what `Mottaksstasjon` actually represents and whether it can be safely converted into a physical landing location.

## Work completed
- Investigated `Mottaksstasjon` in the catch data.
- Investigated the official buyer register.
- Established relationships between approval-number codes and buyer/site records.
- Found that one approval number can map to multiple registered buyer sites.
- Established the distinction between buyer/company, receiving site and physical quay/landing location.

## What we learned
Landing geography is not a simple one-code/one-coordinate lookup. The real-world structure can be many-to-many and may contain missing or ambiguous coordinates.

## Direction change
The geography model became:

`AIS activity → vessel → catch → landing → receiving site / buyer`

rather than treating the buyer's company address as the landing point.

## Result
FA gained an important data-model constraint before any map or landing analysis is built.

## Git
`90a0762dba1f51f038bf31392d39925bae245f7a` — Document landing and buyer register investigation
