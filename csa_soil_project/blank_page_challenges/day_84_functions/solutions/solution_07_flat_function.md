# Solution 7: Self-checking flat-table function (clay as the base, Ghana)

```python
from db_config import run_query, get_engine

ALLOWED = {"orgc": "wosis_orgc", "ph": "wosis_phaq",
           "clay": "wosis_clay", "sand": "wosis_sand"}

def count_rows(short_name, country="Ghana"):
    if short_name not in ALLOWED:
        raise ValueError(f"Unknown table: {short_name}")
    table = ALLOWED[short_name]
    query = f"SELECT COUNT(*) AS n FROM {table} WHERE country_name = '{country}';"
    return run_query(query)["n"].iloc[0]

def build_flat(base, others, country="Ghana"):
    if base not in ALLOWED:
        raise ValueError(f"Unknown table: {base}")
    for name in others:
        if name not in ALLOWED:
            raise ValueError(f"Unknown table: {name}")

    expected = count_rows(base, country=country)
    if expected == 0:                                   # guard first: fail early
        raise ValueError(f"No data for country: {country}")

    select_parts = ["b.profile_id", "b.layer_id", f"b.value_avg AS {base}"]
    join_parts = []
    for i, name in enumerate(others, start=1):
        alias = f"t{i}"
        select_parts.append(f"{alias}.value_avg AS {name}")
        join_parts.append(
            f"LEFT JOIN {ALLOWED[name]} AS {alias} ON b.layer_id = {alias}.layer_id")

    query = f"""
    SELECT {', '.join(select_parts)}
    FROM {ALLOWED[base]} AS b
    {' '.join(join_parts)}
    WHERE b.country_name = '{country}';
    """
    df = run_query(query)

    if len(df) != expected:                             # check BEFORE return
        raise ValueError(f"Row count changed: got {len(df)}, expected {expected}")
    return df
```

Results (Ghana):
- Task 1: `count_rows("clay")` = 801; `count_rows("clya")` raises `Unknown table: clya` before any SQL runs.
- Task 3: `build_flat("clay", ["sand","ph"])` = (801, 5); `build_flat("sand", ["clay","ph"])` = (834, 5). Rows = rows of the base table; columns = 3 (profile_id, layer_id, base) + 1 per other table.
- Task 4:
  - Key `profile_id`: rows go UP (35,699 instead of 801). Each layer matches every layer of its pit, so the count check rings.
  - Key `layer_id + 1`: rows stay 801, NULLs rise only a little (sand 69, pH 70). Layer IDs are consecutive, so the neighbour layer usually exists and the join glues the NEIGHBOUR's values. Count and NULL checks barely notice. Only a spot check against the source table catches it.
- Task 5: `flat.shape == check.shape` True; `flat["clay"].sum() == check["clay"].sum()` True; NULLs identical (ph = 29). Why 29: 801 clay layers all exist in sand, and 772 have pH, so 801 - 772 = 29.
- Task 6: Narnia gives count 0, the query returns 0 rows, 0 == 0 passes silently, so a typo looks like success. Guard: `if expected == 0: raise ValueError(...)`. Best placed before the main query.
- Task 7: (a) `return` ends the function, so a check after it never runs and a broken table ships unchecked. (b) The pandas index is a row-numbering artifact, not data; without `index=False` the saved table gets an extra `index` column and the shape/sum/NULL round trip no longer matches.

Lesson: checks stack. Row count catches multiplication. NULL counts catch some loss. A spot check against the source table catches a wrong-but-valid key.
