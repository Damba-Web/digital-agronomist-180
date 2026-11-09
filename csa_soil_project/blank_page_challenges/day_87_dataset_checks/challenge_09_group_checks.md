# Challenge 9: Check a pooled number by group

Closed book. No cheat sheet, no AI, no Google while you work. Write down anything you look up.
Pass mark: 6 out of 7 (about 86%). If you miss, fix your mistakes and I give you a similar one.
Tools you may use: `groupby`, `.median()`, `.mean()`, `.size()`, `.count()`, `value_counts()`, `merge`, boolean filters.

Setup cell (rebuilds the real table):
```python
import sys
sys.path.append("../..")
import pandas as pd
from agronomic_functions import build_flat, quality_flags
from db_config import run_query

flat = build_flat("orgc", ["ph", "clay", "sand"])
checked = quality_flags(flat)
meta = run_query("SELECT layer_id, dataset_id FROM wosis_orgc WHERE country_name = 'Ghana'")
traced = pd.merge(checked, meta, on="layer_id", how="left")
print(len(traced))   # must be 1756
```

## Part 1: made-up data (no database)
```python
toy = pd.DataFrame({
    "dataset": ["A", "A", "A", "B", "B", "B", "B"],
    "ph":      [5.0, 5.5, 9.0, 6.0, 6.5, 7.0, 7.5],
    "flag":    [False, False, True, False, False, False, False]
})
```

1. **Predict, then run.** Write the median `ph` of each dataset. Then write the `groupby` line. Does it match?
2. For dataset A, is the mean or the median closer to a "typical" layer? Why, in one sentence?
3. Print how many layers each dataset has, and how many **flagged** layers each has. Show that the counts add up to 7. Which dataset looks more suspicious, and why (use "out of how many")?

## Part 2: the real soil table (`traced`)
4. **Predict, then run.** Which dataset has the lowest median `ph`? Paste the `groupby` output.
5. How many layers have a non-missing `clay` value in each dataset? Compare with the total layers in each dataset. The clay counts must add up to the total number of non-missing clay values in the table. Which dataset has none?
6. How many layers have `ph` above 8? Show how many come from each dataset. Check that the dataset counts add up to the total.

## Part 3: judgement
7. Write 3 sentences:
   - one example where a pooled (table-wide) number would mislead you
   - the check you used to find or avoid it
   - one analysis that would be **safe** and one that would be **unsafe** if GH-GhaSP's carbon values are wrong (say why)

## Record your work
Save your answers in your notebook as `challenge_09_my_answers.ipynb`, and keep a `mistakes_log.md` row for every mistake.
