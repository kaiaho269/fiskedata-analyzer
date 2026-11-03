# Fiskedata Analyzer — Project Guide

## Purpose

Fiskedata Analyzer (FA) is a personal fisheries intelligence and analysis tool built on official Norwegian fisheries data.

The goal is not to make a CSV viewer. The goal is to help answer useful questions such as:

> Who fishes here, what do they catch, what is it worth, where do they fish elsewhere, and where do they land the catch?

The project follows a simple principle:

**Questions before dashboards. Analysis before presentation. Evidence before assumptions.**

---

# Current architecture

```text
Human / Streamlit UI
        ↓
FA analysis layer
        ↓
DuckDB
        ↓
Official fisheries data
```

The UI should collect human choices and translate them into analytical parameters. Numerical truth belongs in the analysis layer, not in the UI and not in an AI model.

Long-term direction:

```text
FAQuery / language layer
        ↓
FA query layer
        ↓
FA analytical engine
        ↓
DuckDB / Parquet
        ↓
data
```

Python + Streamlit + DuckDB are appropriate for the current stage. Technology can change later; analytical knowledge and reproducibility are the durable assets.

---

# Current state — 2026-11-03

### Data
- Source: Fiskeridirektoratet 2025 catch data
- Raw CSV: `~/Downloads/fangstdata_2025.csv`
- Size: ~1 GB
- Catch records: ~974,502
- Unique vessels: ~4,591
- Engine: DuckDB
- Python environment: `.venv`

### Working capabilities
- Basic Streamlit application
- Vessel/value ranking
- Vessel name and registration display
- Vessel tracking across the full dataset
- Vessel-size filtering
- Gear filtering
- Area filtering
- KPI summary through the analysis layer
- Data-driven species selection
- `All species` translated to analytical `None`

### Important analytical direction
Statistical sea areas are useful official reference geography, but they should not be treated as a direct representation of actual fishing grounds.

The longer-term geography model is:

```text
AIS activity → vessel → catch → landing → receiving site / buyer
```

Statistical areas remain available as secondary/reference geography.

### Landing geography
Investigation of `Mottaksstasjon` and the official buyer register showed that a receiving/landing relationship is not simply one buyer = one coordinate. One approval number can map to multiple registered buyer sites, and company address, receiving site and physical quay are not necessarily the same thing.

This means landing geography must eventually be modelled explicitly rather than treated as a simple lookup.

---

# Current UI / development focus

The immediate objective is to make FA an investigation tool rather than a dashboard.

Core concept:

**HOME AREA → FLEET → CATCH → VALUE → ELSEWHERE**

The UI should eventually let a user define a human-friendly Home Area, identify the fleet associated with it, inspect catch and value, and follow selected vessels elsewhere.

The species filter is now data-driven from the dataset rather than hard-coded.

---

# Current sprint — Sprint 14

## Project memory cleanup and history reconstruction

The first 13 meaningful repository commits are being represented as individual sprint records under `sprints/`.

This keeps the project guide small and current while preserving the reasoning and direction changes that shaped FA.

### Tasks
1. Keep one markdown file per historical sprint.
2. Use `SPRINT.md` only as the current project guide.
3. Retire the old monolithic `sprint.md` history file.
4. After the cleanup, begin new development from a clean Sprint 14 state.

---

# Next 1–3 development tasks

1. Finish the Fleet Investigation UI using the now-clean filter architecture.
2. Make vessel drill-down useful: home-area catch/value vs outside-area catch/value and elsewhere footprint.
3. Continue validating geography and landing relationships before adding map/AIS complexity.

---

# Roadmap

## Phase 1 — Fleet discovery
- [x] Connect 2025 dataset
- [x] Basic Streamlit UI
- [x] Vessel-size filtering
- [x] Gear filtering
- [x] Value ranking
- [x] Vessel names
- [x] Registration marks
- [x] Multiple statistical areas in backend
- [x] Follow selected vessels across dataset
- [x] Data-driven species filter
- [ ] Fleet Investigation drill-down
- [ ] Home Area selector
- [ ] Multi-cell Home Area
- [ ] Home vs outside-home comparison

## Phase 2 — Geography
- [ ] Statistical-area reference layer
- [ ] Map-based Home Area
- [ ] Human-friendly area names
- [ ] Keep official codes underneath the UI
- [ ] Explicit receiving-site / buyer model

## Phase 3 — Fleet intelligence
- [ ] Species breakdown
- [ ] Area-by-area fishing footprint
- [ ] Annual catch/value
- [ ] Home-area dependency
- [ ] Fleet comparisons
- [ ] Rankings
- [ ] Export reports

## Phase 4 — Time
- [ ] 2024
- [x] 2025
- [ ] 2026
- [ ] Year-over-year comparison
- [ ] Seasonal analysis

## Phase 5 — Advanced
- [ ] AIS integration
- [ ] Fishing-effort analysis
- [ ] Spatial/temporal patterns
- [ ] Advanced fleet behaviour analysis

---

# Development rules

Every focused sprint should:
1. Read this file.
2. Check the current UI when relevant.
3. Check `git status`.
4. Pick one clear goal.
5. Make small understandable changes.
6. Test the analytical result.
7. Record the sprint in `sprints/sprintN.md`.
8. Commit and push.

### Data rule
Never put the raw ~1 GB CSV into GitHub.

### Analysis rule
Validate calculations in DuckDB/Python before making them central to the UI.

### Architecture rule
Do not move analytical logic back into `app.py` merely because it is convenient.

### Performance rule
Measure before optimizing. Do not replace working architecture because something merely feels slow.

### History rule
Sprint records describe not only what changed, but what was learned and how the direction changed.

---

# Useful commands

```bash
cd ~/fiskedata-analyzer
source .venv/bin/activate
streamlit run app.py
git status
git log --oneline -10
git pull
```

`git pull` updates the local repository from the remote repository. `git push` sends local commits to GitHub.

---

# Parking lot

- Map-based Home Area
- Saved Home Areas
- Compare two fleets
- Who fishes here but is based elsewhere?
- Where do vessels from this area fish?
- Which vessels are most dependent on this area?
- Catch value per vessel
- Catch value per kg
- Species mix
- Seasonal patterns
- Open group vs quota vessel analysis
- AIS integration
- XLS/report export
- FAQuery natural-language interface
- Possible future commercial intelligence product
