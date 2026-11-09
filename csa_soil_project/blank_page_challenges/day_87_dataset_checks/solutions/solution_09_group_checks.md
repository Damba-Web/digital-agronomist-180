# Solution notes: Challenge 9 (open only after you finish)

## Part 1 (toy data)
1. Median `ph`: A = 5.5, B = 6.75 (middle of 6.5 and 7.0).
   Line: `toy.groupby("dataset")["ph"].median()`
2. A: mean = 6.5, median = 5.5. The 9.0 drags the mean up; the median is closer to a typical layer.
3. Totals: `toy.groupby("dataset").size()` gives A = 3, B = 4 (3 + 4 = 7).
   Flagged: `toy[toy["flag"] == True].groupby("dataset").size()` gives A = 1 (B has none).
   A is more suspicious: 1 of 3 flagged (33%) against 0 of 4.

## Part 2 (real table: how to check yourself, no need to match my numbers exactly)
4. Lowest median pH is WD-ISIS (4.9). Other medians: AF-AfSP 5.4, GH-GhaSP 5.8, WD-WISE 5.7 (WD-NWAFU-SCS has no pH, so it shows `NaN`).
5. `traced.groupby("dataset_id")["clay"].count()` against `traced.groupby("dataset_id").size()`.
   GH-GhaSP and WD-NWAFU-SCS have 0 clay values. The clay counts must add up to 499.
6. `traced[traced["ph"] > 8]["dataset_id"].value_counts()`; the dataset counts must add up to the number of rows in that filtered table (`len(...)`).

## Part 3: model answer
- Example: the table-wide mean of `orgc` (70.4) is pulled up by GH-GhaSP, whose median is 103.4 against 1.8 to 4.2 in the other datasets.
- Check: `groupby("dataset_id")` median, plus group counts that add up.
- Safe: carbon against clay or sand, because GH-GhaSP has no clay or sand values, so the suspicious carbon values never enter that comparison.
  Unsafe: carbon against pH over all rows, because GH-GhaSP does have pH, so its suspicious carbon values would shape the result.
