# Solution 4: Mini data dictionary (pH, Ghana)

```python
ph.dtypes
ph.nunique()                                      # 4 columns with 1 unique value
ph['layer_name'].isnull().sum()                   # 1302 missing of 2044 -> 63.7%
ph['positional_uncertainty'].value_counts()
ph[['value', 'value_avg']].head()
```

Expected results (2044 rows):
- Constant columns (exactly one unique value): `organic_surface`, `country_name`, `region`, `continent`.
- `layer_name`: 742 non-null, 1,302 missing = 63.7%.
- `positional_uncertainty` (text, `object`): Circa 100 m 1,301 | 1 km - 10 km 395 | 100 m - 1 km 348.
- `value` is the raw text version of `value_avg`; using it would be data leakage.

Model answers for task 6:

| Column | Meaning | Unit | Data type | Source | Cleaning Rule | Use |
|---|---|---|---|---|---|---|
| value_avg | Soil acidity: pH measured in water | none (pH scale, 0-14) | float64 | wosis_202312_phaq | Check values stay within 0-14 | predictor (in the carbon project); target only in a pH model |
| lower_depth | Bottom edge of the layer, measured down from the surface | cm | int64 | wosis_202312_phaq | Check overlapping layers; lower_depth must be greater than upper_depth | predictor |
| dataset_id | Survey that made the record | none | object | wosis_202312_phaq | none yet | metadata |
| profile_id | Label of the soil pit; many layers share it | none | int64 | wosis_202312_phaq | none yet | grouping |
| positional_uncertainty | How precisely the location is known, in text bands | m or km (bands) | object | wosis_202312_phaq | Convert bands to ordered codes; flag the coarsest band (395 rows) before spatial joins | metadata |

Teach-back:
- `lower_depth` is a predictor because carbon and pH change with depth.
- `positional_uncertainty` is metadata because it describes data quality, not soil.

Mistakes to avoid:
- Leaving "organic carbon" in the Meaning of another table.
- Using a word that is not on the Use list (like "quality check").
- Putting a Use word ("needs cleaning") in the Cleaning box.
