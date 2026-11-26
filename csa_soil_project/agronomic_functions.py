"""Reusable functions for the WoSIS Ghana soil project (digital-agronomist-180).

Setup in a notebook (two folders below csa_soil_project):
    import sys
    sys.path.append("../..")
    from agronomic_functions import build_flat, quality_flags

Needs db_config.py (private, not in Git) with a run_query() function.
"""

import pandas as pd
from db_config import run_query

ALLOWED = {"orgc": "wosis_orgc",
           "ph": "wosis_phaq",
           "clay": "wosis_clay",
           "sand": "wosis_sand"}


def count_rows(short_name, country="Ghana"):
    """Count the rows of one WoSIS table for one country.

    Args:
        short_name: "orgc", "ph", "clay" or "sand".
        country: country name as written in the table (default "Ghana").

    Returns:
        The number of rows.

    Raises:
        ValueError: if short_name is not one of the four allowed names.

    Example:
        count_rows("clay")   # 801 for Ghana
    """
    if short_name not in ALLOWED:
        raise ValueError(f"Unknown table: {short_name}")
    table = ALLOWED[short_name]
    query = f"SELECT COUNT(*) AS n FROM {table} WHERE country_name = '{country}';"
    return run_query(query)["n"].iloc[0]


def build_flat(base, others, country="Ghana"):
    """Join a base table with other tables into one flat table, safely.

    Joins on layer_id with LEFT JOINs, so no base row is lost. Checks the
    row count against count_rows(base) before returning.

    Args:
        base: short name of the base table, e.g. "orgc".
        others: list of short names to join, e.g. ["ph", "clay", "sand"].
        country: country name (default "Ghana").

    Returns:
        DataFrame with profile_id, layer_id, the base value and one column
        for each table in others.

    Raises:
        ValueError: unknown table name, the base name also in others, a
            name repeated in others, no data for the country, or the joined
            row count is different from count_rows(base).

    Example:
        flat = build_flat("orgc", ["ph", "clay", "sand"])   # 1,756 rows
    """
    # 1. Check all names are safe
    if base not in ALLOWED:
        raise ValueError(f"Unknown table: {base}")
    for name in others:
        if name not in ALLOWED:
            raise ValueError(f"Unknown table: {name}")

    # 1b. Check no name is used twice (two columns with one name break things)
    if base in others:
        raise ValueError(f"Base table {base} must not also be in others")
    if len(others) != len(set(others)):
        raise ValueError(f"A name is repeated in others: {others}")

    expected = count_rows(base, country=country)
    if expected == 0:
        raise ValueError(f"No data for country: {country}")

    # 2. SELECT parts
    select_parts = [
        "b.profile_id",
        "b.layer_id",
        f"b.value_avg AS {base}"
    ]

    # 3. JOIN parts
    join_parts = []
    for i, name in enumerate(others, start=1):
        alias = f"t{i}"
        table = ALLOWED[name]
        select_parts.append(f"{alias}.value_avg AS {name}")
        join_parts.append(
            f"LEFT JOIN {table} AS {alias} ON b.layer_id = {alias}.layer_id"
        )

    # 4. Whole query
    query = f"""
    SELECT {', '.join(select_parts)}
    FROM {ALLOWED[base]} AS b
    {' '.join(join_parts)}
    WHERE b.country_name = '{country}';
    """

    # 5. Run it
    df = run_query(query)

    # 6. Check against the same country

    if len(df) != expected:
        raise ValueError(
            f"Row count changed: got {len(df)}, expected {expected}"
        )

    # 7. Return safe DataFrame
    return df


def quality_flags(df, oc_high=200):
    """Add flag columns to a flat table. Never deletes or changes rows.

    Hard flags (impossible values):
        flag_ph (below 0 or above 14), flag_clay_sand (clay + sand above 100),
        flag_clay and flag_sand (outside 0 to 100), flag_oc_neg (orgc below 0).
    Soft flag (possible but unusual):
        flag_oc_high (orgc above oc_high).
    A missing value is never flagged (comparisons with NaN give False).

    Args:
        df: table with the columns orgc, ph, clay and sand.
        oc_high: threshold for the soft flag (default 200).

    Returns:
        A copy of df with six new True/False columns. The original is unchanged.

    Raises:
        ValueError: if a required column is missing.

    Example:
        checked = quality_flags(flat)
        checked["flag_oc_high"].sum()   # 144 for Ghana
    """
    # 1. Guard: Check for required columns
    required = ["orgc", "ph", "clay", "sand"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing needed column: {col}")

    # 2. Work on a copy
    checked = df.copy()

    # 3. Five Hard Flags (Impossible)
    checked["flag_ph"] = (checked["ph"] < 0) | (checked["ph"] > 14)
    checked["flag_clay_sand"] = (checked["clay"] + checked["sand"]) > 100
    checked["flag_clay"] = (checked["clay"] < 0) | (checked["clay"] > 100)
    checked["flag_sand"] = (checked["sand"] < 0) | (checked["sand"] > 100)
    checked["flag_oc_neg"] = checked["orgc"] < 0

    # 4. One Soft Flag (Possible but unusual)
    checked["flag_oc_high"] = checked["orgc"] > oc_high

    return checked


def dataset_alarm(df, column, group="dataset_id", ratio=5, min_n=10):
    """
    Finds groups whose median is far above the typical median.
    Groups with fewer than min_n real values are left out before the typical 
    value is found, preventing tiny sample sizes from creating false alarms.

    Args:
        df: The pandas DataFrame.
        column: The numerical column to check.
        group: The column to group by (default is "dataset_id").
        ratio: The multiplier threshold to trigger a flag (default is 5).
        min_n: The minimum number of real values a group must have to be 
               included in the comparison (default is 10).

    Returns:
        A pandas Series containing the medians of the flagged groups.

    Raises:
        ValueError: If the column or group doesn't exist in the table.
        ValueError: If min_n is less than 1.
        ValueError: If no group has at least min_n values.
        ValueError: If the typical value is 0 or missing.

    Note:
        Good for values where "times bigger" means something (carbon, clay %).
        Weak for pH, which is a log scale.

    Example:
        dataset_alarm(traced, "orgc")   # flags GH-GhaSP
    """

# 1. Old guards
    if column not in df.columns:
        raise ValueError(f"Column {column} not found in table.")
    if group not in df.columns:
        raise ValueError(f"Group {group} not found in table.")

    # 2. NEW guard: min_n must make sense
    if min_n < 1:
        raise ValueError("min_n must be at least 1.")

    # 3. The sieve
    counts = df.groupby(group)[column].count()
    enough = counts[counts >= min_n].index
    medians = df.groupby(group)[column].median()
    medians = medians[medians.index.isin(enough)]  # Keep only the big groups

    # 4. NEW guard: nobody passed the sieve
    if len(medians) == 0:
        raise ValueError(
            f"No {group} has at least {min_n} values in {column}.")

    # 5. The rest stays the same
    typical = medians.median()
    if pd.isna(typical) or typical == 0:
        raise ValueError("Typical value is 0. Cannot calculate ratio.")

    ratios = medians / typical
    return medians[ratios > ratio]


def cleaning_report(df, columns, key="layer_id"):
    """Make a short cleaning report with one row per check.

    Rows: Total layers, Duplicate rows, Duplicate <key>, then one
    "Missing <col>" row for each column in columns.
    Report columns: check, result, action.

    Actions for duplicates: count 0 "none needed"; above 0 "investigate; ...".
    Actions for missing values: 0% "none needed"; up to 25% "keep";
    above 25% "keep; X% missing, usable only for the rest".
    The action always follows the result.

    Args:
        df: the table to check.
        columns: list of column names to count missing values in.
        key: column that should be unique (default "layer_id").

    Returns:
        A DataFrame with the columns check, result and action.

    Raises:
        ValueError: if a column or the key is missing, or the table is empty.

    Example:
        cleaning_report(traced, ["ph", "clay", "sand"], key="layer_id")
    """
    # Guard 1: Check if all requested columns exist
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column {col} not found in table.")

    # Guard 2: Check if the key exists
    if key not in df.columns:
        raise ValueError(f"Key column {key} not found in table.")

    # Guard 3: Empty table guard (prevents divide by zero)
    if len(df) == 0:
        raise ValueError("Table is empty, cannot calculate percentages.")

    # Fixed baseline rows
    rows = []
    rows.append({
        "check": "Total layers",
        "result": int(len(df)),
        "action": "baseline count"
    })
    dup_rows = int(df.duplicated().sum())
    if dup_rows == 0:
        dup_rows_action = "none needed"
    else:
        dup_rows_action = "investigate; exact copies, check the source before removing"
    rows.append({
        "check": "Duplicate rows",
        "result": dup_rows,
        "action": dup_rows_action
    })

    dup_keys = int(df[key].duplicated().sum())
    if dup_keys == 0:
        dup_keys_action = "none needed"
    else:
        dup_keys_action = f"investigate; same {key} on different rows"
    rows.append({
        "check": f"Duplicate {key}",
        "result": dup_keys,
        "action": dup_keys_action
    })

    # Loop for the columns
    for col in columns:
        missing = int(df[col].isna().sum())
        pct = missing / len(df) * 100

        if pct == 0:
            action = "none needed"
        elif pct <= 25:
            action = "keep"
        else:
            action = f"keep; {pct:.0f}% missing, usable only for the rest"

        rows.append({
            "check": f"Missing {col}",
            "result": missing,
            "action": action
        })

    return pd.DataFrame(rows)
