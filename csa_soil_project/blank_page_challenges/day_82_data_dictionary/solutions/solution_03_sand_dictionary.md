# Solution 3: Mini data dictionary (sand, Ghana)

Commands:
```python
sand.dtypes                                              # task 1
sand.nunique()                                           # task 2: columns with 1 unique value
sand['layer_name'].isnull().sum()                        # task 3 (divide by len(sand) for %)
sand['positional_uncertainty'].value_counts()            # task 4
sand[['value', 'value_avg']].head()                      # task 5
```

What to expect (check each against your own output; the table has 834 rows for Ghana):
- Same 19 columns as the other WoSIS tables, so the data types match the orgc table (depths int64, value_avg float64, organic_surface bool, positional_uncertainty object).
- `country_name` has 1 unique value (Ghana, because of the filter). Check `region`, `continent` and `organic_surface` with `nunique()`. A column with one unique value is a constant column.
- `positional_uncertainty` is text in 3 bands (for example "Circa 100 m", "100 m - 1 km", "1 km - 10 km"), not a number.
- `value` is text in curly brackets; `value_avg` is the clean number.

Model answers for task 6 (unit for `value_avg` in the sand table is g/100g; confirm in the WoSIS readme):

| Column | Meaning | Unit | Data type | Source | Cleaning Rule | Use |
|---|---|---|---|---|---|---|
| value_avg | Sand share of the soil layer | g/100g | float64 | WoSIS sand file | Check values are within 0-100 | target (for a sand model) or predictor (for a carbon model) |
| upper_depth | Top edge of the layer, measured down from the surface | cm | int64 | WoSIS sand file | Check overlapping layers | predictor |
| dataset_id | Survey that made the record | none | object | WoSIS sand file | none yet | metadata |
| profile_id | Label of the soil pit; many layers share it | none | int64 | WoSIS sand file | none yet | grouping |
| positional_uncertainty | How precisely the location is known, in 3 bands | text bands (m/km) | object | WoSIS sand file | Convert to ordered codes if used; flag the coarsest band | metadata |

Task 5: `value` is the raw version of the target. Using it would be reading the answer off the input (a leak).
Task 7: `dataset_id` says who collected the data, not why sand varies, so metadata. `profile_id` is used to group layers by soil pit, so grouping.

Common mistakes:
- Putting a job word (like "grouping") in the Cleaning box.
- Giving a unit to a label (profile_id, dataset_id).
- Writing data types from memory instead of from `dtypes`.
- Trusting `isnull().sum() == 0` as proof that a text column is clean.
- Writing a cleaning rule for a problem you have not found. Write "none yet".
