# Real Data Dictionary — WoSIS Ghana Organic Carbon

Source file: WoSIS orgc file (Ghana subset)
Rows: 1,756 soil layers from 318 profiles
Target: `value_avg`

| Column names | Meaning | Unit | Data type | Source | Cleaning rules | Use in project |
|---|---|---|---|---|---|---|
| value_avg | The mean of the organic carbon values | g/kg | float64 | WoSIS orgc file | Flag the 144 layers above 200 g/kg. Do not delete. | target |
| upper_depth | Top edge of the soil layer, measured down from the surface (a layer from 10–30 cm has upper_depth = 10) | cm | int64 | WoSIS orgc file | None yet | predictor |
| lower_depth | Bottom edge of the soil layer, measured down from the surface (a layer from 10–30 cm has lower_depth = 30) | cm | int64 | WoSIS orgc file | Check overlapping layers (profile 1169146); ensure lower_depth > upper_depth | predictor |
| latitude | North–south position of the sample | degrees | float64 | WoSIS orgc file | None yet | predictor |
| longitude | East–west position of the sample | degrees | float64 | WoSIS orgc file | None yet | predictor |
| date | When the sample was taken | None | object | WoSIS orgc file | Replace `?` parts with missing; make a year column | needs cleaning |
| dataset_id | The survey that made the record | None | object | WoSIS orgc file | None yet | quality check |
| profile_id | Label for a soil profile | None | int64 | WoSIS orgc file | None yet | grouping |
| layer_id | Label for a single soil layer | None | int64 | WoSIS orgc file | None yet | metadata |
| layer_name | Name of the soil layer | None | object | WoSIS orgc file | None: 67% missing and not needed | unused |
| profile_code | Text code that labels the same profile as `profile_id` | None | object | WoSIS orgc file | None yet | metadata |
| positional_uncertainty | How far off the recorded location could be | km | object | WoSIS orgc file | Run `value_counts()` to see what text it holds (0 true nulls, but text can hide `?` or `< 1`); decide fill/drop then | metadata |
| country_name | Country of the sample | None | object | WoSIS orgc file | None: constant (1 unique value) | unused |
| region | Region of the sample | None | object | WoSIS orgc file | None: constant (1 unique value) | unused |
| continent | Continent of the sample | None | object | WoSIS orgc file | None: constant (1 unique value) | unused |
| organic_surface | True/False — is this an organic layer on top of mineral soil? Constant: False in all 1,756 rows | None | bool | WoSIS orgc file | None — constant (1 unique value) | unused |
| licence | Which Creative Commons licence covers each layer (3 kinds) | None | object | WoSIS orgc file | Flag the 722 CC BY-NC rows; do not use commercially | metadata |
| value | Raw organic carbon as text in curly brackets, e.g. {14.9} | g/kg | object | WoSIS orgc file | Do not parse; use `value_avg` instead | unused (target leak) |
| method_options | How the lab measured organic carbon | None | object | WoSIS orgc file | None yet | metadata |

