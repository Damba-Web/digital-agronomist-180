from db_config import run_query

ALLOWED = {"orgc": "wosis_orgc",
           "ph": "wosis_phaq",
           "clay": "wosis_clay",
           "sand": "wosis_sand"}


def count_rows(short_name, country="Ghana"):
    if short_name not in ALLOWED:
        raise ValueError(f"Unknown table: {short_name}")
    table = ALLOWED[short_name]
    query = f"SELECT COUNT(*) AS n FROM {table} WHERE country_name = '{country}';"
    return run_query(query)["n"].iloc[0]


def build_flat(base, others, country="Ghana"):
    # 1. Check all names are safe
    if base not in ALLOWED:
        raise ValueError(f"Unknown table: {base}")
    for name in others:
        if name not in ALLOWED:
            raise ValueError(f"Unknown table: {name}")

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
