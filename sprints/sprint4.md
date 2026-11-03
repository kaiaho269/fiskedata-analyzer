# Sprint 4 — Data-driven species filter

## Goal

Remove the hard-coded species limitation from the FA species filter.

The species available in the UI should come from the actual dataset rather than being manually specified in `app.py`.

---

## Work completed

### 1. Investigated species data

Queried the 2025 dataset directly with DuckDB.

The dataset contains **33 distinct values** in `"Art - gruppe"`.

Examples include:

- Torsk
- Sei
- Hyse
- Kveite
- Makrell
- Steinbiter
- Lange
- Uer
- Krabbe
- several broader species groups

This confirmed that limiting the UI to Torsk and Sei would be hard-coding and would not scale.

### 2. Added `get_species()`

Added a function to `analysis.py`:

```python
def get_species():
    conn = connect()

    query = f"""
        SELECT DISTINCT "Art - gruppe" AS species
        {base_query()}
        WHERE "Art - gruppe" IS NOT NULL
        ORDER BY species
    """

    return [row[0] for row in conn.execute(query).fetchall()]
```

The function discovers the species directly from the dataset.

### 3. Updated the Streamlit species filter

`app.py` now imports `get_species()` and builds the dropdown dynamically:

```python
species_options = ["All species"] + get_species()
```

The UI therefore no longer contains a hard-coded list of fish species.

### 4. Fixed the `All species` case

Initial testing revealed that selecting `All species` produced zero vessels.

The reason was that the UI value `"All species"` was being passed to the analytical engine as if it were an actual species.

Fixed with:

```python
selected_species = None if species_filter == "All species" else species_filter
```

The analytical engine now receives:

- a real species name when a species is selected
- `None` when all species should be included

This keeps UI terminology separate from analytical logic.

---

## Testing

The Streamlit UI was tested with different species.

Results in Romsdalsfjorden 07-31:

| Species | Vessels |
|---|---:|
| Hyse | 64 |
| Torsk | 76 |
| All species | 137 |

The results change correctly when the species selection changes.

---

## Important discovery

The original Torsk/Sei limitation was not necessary.

The dataset itself is capable of providing the species list, so FA should use the data as the source of truth rather than maintaining manually coded species lists.

This is an important architectural principle:

> **UI vocabulary and analytical values should be separated.**

For example:

`"All species"` is a UI concept.

`None` is the analytical meaning of "do not filter by species."

---

## Result

**Sprint 4 successful.**

The species filter is now **data-driven** rather than hard-coded.

FA can automatically accommodate additional species appearing in the dataset without requiring changes to the species list in the UI.

---

## Lessons

- Do not hard-code values that already exist in the dataset.
- Let the data provide selectable categories where practical.
- Translate UI concepts into analytical values before passing them to the engine.
- Test both specific selections and the "all" case.
- A bug discovered during implementation is useful information, not a failed sprint.

---

## Next

Close Sprint 4 with a Git commit.

Potential commit message:

```text
Make species filter data-driven
```

Sprint 5 should begin from this clean state.
