# Solution 6: Flat table with sand as the base (Ghana)

Task 1: key check (run for wosis_sand and wosis_clay)
```sql
SELECT COUNT(*) AS rows_total, COUNT(DISTINCT layer_id) AS layers_distinct
FROM wosis_sand
WHERE country_name = 'Ghana';
```
Results: sand 834 / 834, clay 801 / 801 (pH 2,044 / 2,044). `layer_id` is unique in every table, so a join on it cannot multiply rows.

Task 2: the flat table
```sql
SELECT ws.profile_id,
       ws.layer_id,
       ws.value_avg AS sand,
       wc.value_avg AS clay,
       p.value_avg  AS ph
FROM wosis_sand ws
LEFT JOIN wosis_clay wc ON ws.layer_id = wc.layer_id
LEFT JOIN wosis_phaq p  ON ws.layer_id = p.layer_id
WHERE ws.country_name = 'Ghana';
```

Task 3: `flat2.shape` is (834, 5). The row count equals the base table (834), so no rows were lost or multiplied.

Task 4: `flat2.isnull().sum()` gives clay 33 missing, pH 61 missing, sand 0.
Proof in SQL: `COUNT(*) - COUNT(c.layer_id)` gives 33 for clay, and `COUNT(*) - COUNT(p.layer_id)` gives 61 for pH. Use COUNT(column) to count the matches.

Task 5: prediction = 801 rows.
1. Sand layers with no clay match get an empty `c.country_name`.
2. `NULL = 'Ghana'` is not true, so those layers are removed (the LEFT JOIN turns into an INNER JOIN on clay).
3. 834 - 33 = 801 layers survive.
Rule: put the country filter on the base table only.

Task 6: `flat2.dropna().shape[0]` is 772 (92.6% of 834) complete rows.
Options for missing values: remove incomplete rows (risk: lose data and bias the sample); fill (risk: invent patterns that are not real). A third option is to model with and without the incomplete columns and compare.

Task 7:
(a) Sand is the target, so every sand layer must stay, even when clay or pH is missing; the missing matches become NULL.
(b) More rows than expected happen when the key is not unique on the right side (one left row matches many right rows), or when you join on a coarse key like `profile_id` (every layer matches every layer in that profile).

Observation: the carbon-based table had only 486 complete rows of 1,756 (27.7%), while this one has 772 of 834 (92.6%). The choice of base table decides how complete the flat table is.
