# My mistakes log: Day 84 (self-checking functions)

| Step | What happened | Fix |
|---|---|---|
| Warm-up | Described what the function does but not its inputs or what the count is compared to | Say both: inputs (base name, list of other names) and the check (joined rows == rows of the base table) |
| Step A | Typed the printed result `np.int64(801)` back into a cell as code, then misspelled the function name `count_row` | Results are output, not code. Function names must match exactly (`count_rows`) |
| Step B | Comment typo (`STARTINF`) | Re-read comments before committing |

| Challenge 7 | Predicted "rows go down" for a shifted key; pasted descriptions of outputs instead of real ones at first | LEFT JOIN never drops base rows. A wrong-but-valid key keeps the count and adds few NULLs. Always paste raw output or a screenshot |
| Challenge 7 | Reported ph = 0 missing for the clay base | Real value is 29 (801 - 772). Reason from the Day 83 numbers before trusting a result |

Result: Challenge 7 passed 6/7 after redoing the proof with real screenshots.

Lessons:
1. A function that only returns is dangerous. A function that checks itself catches a bad join early.
2. A join on `profile_id` multiplied 1,756 rows into 219,324 (each layer matched every layer of its pit).
3. Put the check BEFORE `return`, and test the "bad input" case, not only the happy path.
4. `index=False` stops pandas saving its hidden row numbers as an extra column.
5. `to_sql` and `run_query` must point to the same database.
