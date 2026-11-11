# My mistakes log: Day 87 (Challenge 9, group checks)

| Task | What happened | Fix |
|---|---|---|
| Q4 | Ran the code without writing a prediction first | Write the prediction first, then run |
| Q6 | Reported a total without showing the check | `len(traced[traced["ph"] > 8])` must equal the sum of the group counts |
| Q7 | The "safe" example was not about carbon | Carbon vs clay or sand is safe, because GH-GhaSP has no clay or sand |

Result: Challenge 9 passed (about 6.5/7).

Lessons:
1. Check every pooled number by group: `groupby("dataset_id")`.
2. Group counts must add up to the group size.
3. Median resists odd values; the mean does not.
4. A missing value is not "above 8".