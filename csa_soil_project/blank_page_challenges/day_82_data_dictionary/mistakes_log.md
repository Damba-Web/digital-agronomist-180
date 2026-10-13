# My mistakes log: Day 82 (data dictionary)

| Attempt | Table | Score | Main slips | Fix |
|---|---|---|---|---|
| Challenge 3 | sand | 4/7 | Copied old orgc rows (wrong Meaning, Unit, Source); called a text column "a number"; said "linkage" for leakage; no percentage | Check every box is about THIS table; trust dtypes |
| Challenge 4 | pH | 5/7 | "Organic carbon" left in Meaning; "quality check" is not an allowed word; a Use word in the Cleaning box | Sticky note with the 7 words; Cleaning box = a concrete fix |
| Challenge 5 | clay | 6/7 (pass) | Task 5 explanation reused from the pH answer; Task 7 did not explain why value_avg is a predictor | Re-run the code on the right table; explain the Use word |

Lessons:
1. A data dictionary describes one table. Copying another table's words makes it lie.
2. Each box answers its own question.
3. `isnull() == 0` does not prove a text column is clean. Run `value_counts()`.
4. A text column that looks like numbers is still text. Check `dtypes`.
