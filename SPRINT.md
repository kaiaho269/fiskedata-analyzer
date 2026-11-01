# Fiskedata Analyzer — Sprint Guide

## Purpose

Fiskedata Analyzer is a fishing-fleet intelligence tool built on the Norwegian Directorate of Fisheries 2025 catch data.

The goal is **not** to make a CSV viewer. The goal is to let a user define a fishing fleet/home area and then investigate:

> Who fishes here, what do they catch, what is it worth, and where else do they fish?

---

# 1. Current status — 2026-11-01

### Data
- Source: Fiskeridirektoratet 2025 catch data
- Raw CSV: `~/Downloads/fangstdata_2025.csv`
- Size: ~1 GB
- Catch records: **974,502**
- Unique vessels: **4,591**
- Engine: DuckDB
- Python environment: `.venv`

### Backend already working

`analysis.py` contains:

- `rank_vessels_by_value(...)`
  - date filtering
  - vessel-size filtering
  - multiple statistical areas
  - species filtering
  - catch value in NOK
  - vessel name
  - registration mark

- `follow_vessels(...)`
  - follows selected vessel IDs across the entire dataset
  - returns area, species, catch value, vessel name and registration

### Important terminology / data rules

- `Fartøy ID` = internal vessel identifier
- `Fartøynavn` = vessel name
- `Registreringsmerke (seddel)` = registration mark
- Example: `TF0008S` represents the real-world registration **TF-8-S**
- `TF` = Troms og Finnmark
- `M` = Møre og Romsdal
- Registration format changed historically, so do **not** treat the raw string as the final display format.
- `Kvotefartøy` means a vessel with quota; it is still an ordinary vessel in the fleet.
- Open-group vessels have seasonal limits for species such as torsk and sei.

### Proven analysis checkpoint

Initial home-area test:
- Main area: `07`
- Location: `31`
- Combined test area: `07-30`, `07-31`, `07-32`

For `07-31`:
- Under 11 m + torsk/sei:
  - **58 unique vessels**
  - **45 caught both torsk and sei**

The backend can now follow those vessel IDs across the whole 2025 dataset.

---

# 2. Current UI

Streamlit UI is running at:

`http://localhost:8501`

Current screen has:
- Fiskedata Analyzer title
- Catch records
- Unique vessels
- Vessel length filter
- Gear filter
- Dataset connection status

The next UI step is deliberately **big**, not cosmetic.

---

# 3. NEXT SPRINT — Build the Fleet Investigation UI

## Main concept

### HOME AREA → FLEET → CATCH → VALUE → ELSEWHERE

The user should not have to think in ugly statistical codes.

### Home Area

Eventually this will be a **map-based selection**.

The user can select one or more statistical grid cells to create a logical:

> **My Home Area**

Example:
- 07-30
- 07-31
- 07-32
- possibly additional neighboring cells

The codes remain underneath in the analysis layer.

## First UI version

Use `07-31` as the working test area.

Controls:
1. Home Area
2. Species
   - Torsk
   - Sei
   - Both
   - later: any species
3. Vessel size
   - All
   - Under 11 m
   - 11–14.99 m
   - 15–20.99 m
   - 21–27.99 m
   - 28 m and over

## Fleet result

Show a proper table:

| Vessel | Registration | Catch | Value |
|---|---|---:|---:|
| ARNØYTIND | TF-8-S | ... t | ... NOK |

Important:
- Display vessel name and registration to humans.
- Keep `Fartøy ID` internally for joins/tracking.
- Format registration marks for display (`TF0008S` → `TF-8-S`).

## Vessel investigation

Selecting a vessel should show:

- Vessel name
- Registration
- Total 2025 catch
- Total 2025 value
- Home-area catch
- Home-area value
- Outside-home-area catch
- Outside-home-area value
- % of catch from home area
- % of value from home area
- Areas fished elsewhere
- Species caught elsewhere

This is the core "follow the fleet" feature.

---

# 4. Product architecture

Keep these layers separate.

### Human layer
Map + simple UI:
> "My Home Area"

### Analysis layer
Selected map cells → official statistical codes → vessel IDs → calculations

### Data layer
DuckDB + official Fiskeridirektoratet fields.

This separation is important.

**Do not redesign the analysis engine just because the map UI changes.**

---

# 5. Roadmap

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
- [ ] Big Fleet Investigation UI
- [ ] Home Area selector
- [ ] Multi-cell Home Area
- [ ] Vessel drill-down
- [ ] Home vs outside-home comparison

## Phase 2 — Map
- [ ] Statistical-area map
- [ ] Click/select grid cells
- [ ] Save Home Area
- [ ] Human-friendly area names
- [ ] Keep official codes hidden underneath

## Phase 3 — Fleet intelligence
- [ ] Species breakdown
- [ ] Area-by-area movement/fishing footprint
- [ ] Annual catch/value
- [ ] Home-area dependency
- [ ] Fleet comparisons
- [ ] Rankings
- [ ] Export reports

## Phase 4 — Time
- [ ] 2024
- [ ] 2025
- [ ] 2026
- [ ] Year-over-year comparison
- [ ] Seasonal analysis

## Phase 5 — Advanced
- [ ] AIS integration
- [ ] Fishing effort analysis
- [ ] Spatial/temporal patterns
- [ ] More advanced fleet behaviour analysis

---

# 6. Development rules

### Every sprint starts here

Before coding:
1. Read this file.
2. Check the current UI.
3. Check `git status`.
4. Identify **one sprint goal**.
5. Make small changes.
6. Test.
7. Commit.
8. Push to GitHub.
9. Update this file.

### Git rule

Every meaningful completed feature gets:

```bash
git add <files>
git commit -m "Short description"
git push
```

Never assume work is safe until it is pushed.

### Data rule

Never put the raw 1 GB CSV into GitHub.

### Analysis rule

Validate calculations in DuckDB/Python before making them central to the UI.

---

# 7. Useful commands

Activate environment:

```bash
cd ~/fiskedata-analyzer
source .venv/bin/activate
```

Run Streamlit:

```bash
streamlit run app.py
```

Check Git:

```bash
git status
```

Check recent commits:

```bash
git log --oneline -5
```

---

# 8. Current sprint goal

## 🎣 Build the first real Fleet Investigation screen

Start with:

**07-31 → Under 11 m → Torsk + Sei**

Then display the fleet using:

**Vessel name + registration + catch + NOK value**

After that, make one vessel clickable and use `follow_vessels()` to show where that vessel fished during 2025.

That will turn Fiskedata Analyzer from a dashboard into an actual investigation tool.

---

# 9. Ideas / parking lot

Keep ideas here instead of immediately coding them.

- Map-based Home Area
- Saved Home Areas
- Compare two fleets
- Compare neighboring fishing areas
- "Who fishes here but is based elsewhere?"
- "Where do the vessels from this area fish?"
- "Which vessels are most dependent on this area?"
- Catch value per vessel
- Catch value per kg
- Species mix
- Seasonal patterns
- Open group vs quota vessel analysis
- AIS integration
- Report/export to XLS
- Possible future commercial intelligence product

---

## Sprint habit

At the end of every sprint, update:

### DONE
What actually works.

### NEXT
The next 1–3 concrete tasks.

### IDEAS
Interesting things that should NOT distract from the current sprint.

### GIT
Last pushed commit.

This file is the project's memory between ChatGPT chats.
