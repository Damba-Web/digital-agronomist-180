# My mistakes log: Day 84 (self-checking functions)

| Step | What happened | Fix |
|---|---|---|
| Warm-up | Described what the function does but not its inputs or what the count is compared to | Say both: inputs (base name, list of other names) and the check (joined rows == rows of the base table) |
| Step A | Typed the printed result `np.int64(801)` back into a cell as code, then misspelled the function name `count_row` | Results are output, not code. Function names must match exactly (`count_rows`) |
| Step B | Comment typo (`STARTINF`) | Re-read comments before committing |

Lessons:
1. A function that only returns is dangerous. A function that checks itself catches a bad join early.
2. A join on `profile_id` multiplied 1,756 rows into 219,324 (each layer matched every layer of its pit).
3. Put the check BEFORE `return`, and test the "bad input" case, not only the happy path.
4. `index=False` stops pandas saving its hidden row numbers as an extra column.
5. `to_sql` and `run_query` must point to the same database.
