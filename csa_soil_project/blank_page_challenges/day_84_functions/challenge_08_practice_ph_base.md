# Challenge 8 (practice only): Flat function with pH as the base + a spot check

Optional practice for later. No need to send answers. Do it closed book, then compare with your notes.
Same rules as before: no cheat sheet, no AI, write down anything you look up. Aim for 6/7.

Setup:
```python
import sys
sys.path.append("../..")
import pandas as pd
from db_config import run_query, get_engine
```

Tasks:
1. Write the allow-list and `count_rows(short_name, country="Ghana")`. Paste `count_rows("ph")` and the error for `count_rows("phh")`.
2. Write `build_flat(base, others, country="Ghana")` with name checks, a guard for zero rows, LEFT JOINs on `layer_id`, and a row-count check before `return`. Predict the shape of `build_flat("ph", ["orgc", "clay", "sand"])` first, then run it.
3. Write `spot_check(df, name, n=3)`. It takes the first `n` layer IDs of `df`, reads their values for `name` straight from the source table, and raises a `ValueError` if they differ from `df`. Show it passes on the correct build.
4. Break the join on purpose (`layer_id + 1`). Show that `build_flat` still returns without error, and that `spot_check` raises. Then fix the join.
5. Print the percentage of missing values per column, rounded to 1 decimal. Predict which column has the most missing before you run it.
6. Save the table as `flat_ph_ghana` (`index=False`), read it back, and prove the round trip with shape, sum and NULL counts.
7. Edge case: `build_flat("ph", ["ph"])` puts the same name twice. Predict what happens, run it, and add a guard with a clear message.
