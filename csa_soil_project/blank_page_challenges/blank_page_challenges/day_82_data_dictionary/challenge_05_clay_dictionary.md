# Challenge 5: Build a mini data dictionary (clay table, Ghana)

Closed book. No cheat sheet. No AI. No copying your old tables. Time: 25-35 minutes. Pass: 6/7.
Write down everything you look up.

Load the data:
```python
clay = run_query("SELECT * FROM wosis_clay WHERE country_name = 'Ghana';")
```

The 7 boxes for every column: Column Name, Meaning, Unit, Data Type, Source, Cleaning Rule, Use in Project.
The ONLY allowed "Use in Project" words: target, predictor, grouping, location, metadata, unused, needs cleaning.

Tasks:
1. Print the data type of every column. Paste the command and the output.
2. Which columns have exactly ONE unique value? Give the command and the output. Then write this sentence, filled in: "These ___ columns are ___ columns."
3. How many values are missing in `layer_name`? Give the count AND the percentage.
4. Run `value_counts()` on `positional_uncertainty`. List the bands and counts. Is the column a number or text? Prove it with your task 1 output.
5. Look at the first 5 rows of `value` and `value_avg`. In one sentence, say why `value` must not be a predictor. Use the correct word.
6. Fill in all 7 boxes for: `value_avg`, `upper_depth`, `dataset_id`, `latitude`, `positional_uncertainty`.
   - Find the unit of clay in the WoSIS readme and write the page.
   - Think about what clay does in YOUR project: is it the target, or a clue for the target?
7. Teach-back: one sentence each on why you chose the "Use" word for `dataset_id` and `value_avg`.

Self-check before you submit (these are the slips from Challenges 3 and 4):
- [ ] Does the Meaning of `value_avg` talk about CLAY, not organic carbon or pH?
- [ ] Is every "Use" word on the allowed list? (No "quality check".)
- [ ] Does the Cleaning box describe a fix, not a job word like "needs cleaning" or "grouping"?
- [ ] Did I name the constant columns with the right word?
- [ ] Is every Source and Unit about THIS table?
