# My mistakes log: Day 83 (flat table with JOIN)

| Step | What happened | Fix |
|---|---|---|
| Check question | Said INNER JOIN could cause MORE rows | INNER JOIN only removes rows; extra rows come from a non-unique key or a coarse key like profile_id |
| pH coverage | Guessed 288 unmatched pH layers by subtracting totals | Real count is 302 (2,044 - 1,742). Use COUNT(column) to count matches |
| Filter placement | Thought filters on joined tables "can work" | A filter on the joined table turns a LEFT JOIN into an INNER JOIN; filter the base table only |
| Missing clay/sand | Suggested random fill for 72% missing | Most of the column would be invented. Compare models with and without those columns instead |
| Challenge 6 | 6/7: did not paste SQL outputs; mentioned carbon in a sand join | Paste outputs as proof; re-read answers for words from the previous task |

Lessons:
1. Fewer rows means a join that loses data. More rows means a join that multiplies data.
2. Check the row count after every join.
3. The base table decides who survives.
4. Totals give guesses. COUNT(column) gives truth.
