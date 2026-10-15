# Challenge 6: Build a flat table with JOIN (sand as the base table)

Closed book. No cheat sheet. No AI. No copying your old query. Time: 30-40 minutes. Pass: 6/7.
Write down everything you look up.

Goal: one row per sand layer in Ghana, with sand, clay and pH side by side.

Setup (Python cell):
```python
import sys
sys.path.append("../..")
import pandas as pd
from db_config import run_query
```

Tasks:
1. Key check. For `wosis_sand` and `wosis_clay`, write one SQL query each that shows `rows_total` and `layers_distinct` (Ghana only). Paste the outputs. Say whether `layer_id` is a safe key and why.
2. Write the SQL that builds the flat table with `wosis_sand` as the BASE table, LEFT JOINing clay and pH. Use aliases and rename the three `value_avg` columns to `sand`, `clay` and `ph`. Paste the query.
3. Run it with `run_query` into a DataFrame called `flat2`. Paste `flat2.shape`. Is the row count equal to the number of Ghana sand layers (834)? If not, explain.
4. Paste `flat2.isnull().sum()`. For clay and pH, write the matching SQL count that proves the numbers (use `COUNT(c.layer_id)`).
5. Prediction with reasoning: if you add `AND c.country_name = 'Ghana'` to the WHERE, how many rows do you expect? Write the 3-step reasoning first, then run it and compare.
6. Run `flat2.dropna().shape[0]`. What does the number mean for a model that uses all three columns? Name two options for the missing values and one risk of each.
7. Teach-back: in two sentences, explain (a) why a LEFT JOIN is right when sand is the target, and (b) two different causes of MORE rows than expected after a join.

Self-check before you submit:
- [ ] Did the row count stay at the base table's count?
- [ ] Is the Ghana filter only on the base table `s`?
- [ ] Are the three `value_avg` columns renamed?
- [ ] Did I use COUNT(column) (matches) instead of subtracting totals?
- [ ] Did I ignore the ID columns in describe()?
