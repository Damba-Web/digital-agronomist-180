# Solution 5: Mini data dictionary (clay, Ghana)

```python
clay.dtypes
clay.nunique()                                    # 4 columns with 1 unique value
clay['layer_name'].isnull().sum()                 # 155 missing of 801 -> 19.4%
clay['positional_uncertainty'].value_counts()
clay[['value', 'value_avg']].head()
```

Expected results (801 rows):
- "These 4 columns are constant columns": `organic_surface`, `country_name`, `region`, `continent`.
- `layer_name`: 646 non-null, 155 missing = 19.4%.
- `positional_uncertainty` (text, `object`): Circa 100 m 357 | 1 km - 10 km 260 | 100 m - 1 km 184.
- `value` is the raw version of `value_avg`: data leakage.

Model answers for task 6:

| Column | Meaning | Unit | Data type | Source | Cleaning Rule | Use |
|---|---|---|---|---|---|---|
| value_avg | Clay share of the soil layer (mean of the reported values) | g/100g | float64 | wosis_202312_clay | Check values stay within 0-100; note the 0.0 values | predictor (clay helps hold carbon) |
| upper_depth | Top edge of the layer, measured down from the surface | cm | int64 | wosis_202312_clay | Check overlapping layers | predictor |
| dataset_id | Survey that made the record | none | object | wosis_202312_clay | none yet | metadata |
| latitude | North-south position of the sample | degrees | float64 | wosis_202312_clay | none yet | predictor |
| positional_uncertainty | How precisely the location is known, in text bands | m or km (bands) | object | wosis_202312_clay | Map bands to ordered codes (or midpoints 0.1, 0.55, 5.5 km) before any use | metadata |

Teach-back:
- `dataset_id` is metadata: it says who collected the data, not why carbon varies. It is useful for comparing surveys.
- `value_avg` is a predictor in the carbon project: clay is a clue for organic carbon, which is the target.

Always write the readme page where you found the unit.
