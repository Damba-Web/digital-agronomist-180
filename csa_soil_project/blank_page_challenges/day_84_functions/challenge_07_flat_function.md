# Challenge 7: A self-checking flat-table function (clay as the base)

Closed book. No cheat sheet. No AI. No copying your old function. Time: 35-45 minutes. Pass: 6/7.
Write down everything you look up.

Goal: a reusable function that builds the Ghana flat table for ANY base table, checks itself, and saves the result to PostgreSQL.

Setup (Python cell):
```python
import sys
sys.path.append("../..")
import pandas as pd
from db_config import run_query, get_engine
```

Tasks:
1. Write the allow-list dictionary (short name -> table name for orgc, ph, clay, sand) and `count_rows(short_name, country="Ghana")`. It must refuse unknown names with a `ValueError`. Paste `count_rows("clay")` and the error from `count_rows("clya")`.
2. Write `build_flat(base, others, country="Ghana")`. It validates every name, builds a LEFT JOIN query (base = `b`, others = `t1`, `t2`, ...; each `value_avg` renamed to its short name), filters on the base table only, and raises a `ValueError` if the row count differs from `count_rows(base, country)`. Paste the code.
3. Run `build_flat("clay", ["sand", "ph"])` and `build_flat("sand", ["clay", "ph"])`. Paste both shapes. Predict both numbers BEFORE you run them, and say how you worked them out.
4. Prove the alarm rings. Change the join key to `profile_id`, predict whether the row count goes up or down and why, run it, paste the error, then change it back.
5. Save the clay-based table to PostgreSQL as `flat_clay_ghana` (`index=False`), read it back, and paste three proofs: same shape, same sum of `clay`, same `isnull().sum()`.
6. Edge case: run `build_flat("clay", ["sand"], country="Narnia")`. Predict first what happens. Then decide: is that result good or bad? Add a guard so the function raises a clear error in this case. Paste your guard and the new message.
7. Teach-back, two sentences: (a) why must the check sit BEFORE `return`? (b) why `index=False`, and what would you see in the saved table without it?

Self-check before you submit:
- [ ] Is the Ghana (country) filter only on the base table `b`?
- [ ] Does `build_flat` pass the same `country` to `count_rows`?
- [ ] Did I predict before I ran?
- [ ] Did I paste outputs, not only say "it worked"?
- [ ] Did I change the join key back to `layer_id`?
