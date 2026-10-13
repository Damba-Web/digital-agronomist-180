# Challenge 4: Build a mini data dictionary (pH table, Ghana)

Closed book. No cheat sheet. No AI. No copying your old tables. Time: 25-35 minutes. Pass: 6/7.
Write down everything you look up.

Load the data:
```python
ph = run_query("SELECT * FROM wosis_phaq WHERE country_name = 'Ghana';")
```

The 7 boxes for every column: Column Name, Meaning, Unit, Data Type, Source, Cleaning Rule, Use in Project.
Allowed "Use in Project" words (only these 7): target, predictor, grouping, location, metadata, unused, needs cleaning.

Tasks:
1. Print the data type of every column. Paste the command and the output.
2. Which columns have exactly ONE unique value? Give the command, list the columns, and name this kind of column.
3. How many values are missing in `layer_name`? Give the count AND the percentage.
4. Run `value_counts()` on `positional_uncertainty`. List the bands and counts. Is the column a number or text? Prove it with the output of task 1.
5. Look at the first 5 rows of `value` and `value_avg`. Explain in one sentence why `value` must not be a predictor, and use the correct word for this problem.
6. Fill in all 7 boxes for: `value_avg`, `lower_depth`, `dataset_id`, `profile_id`, `positional_uncertainty`.
   - Check the unit of pH in the WoSIS readme. Say which page.
   - The Source box must name the correct file for THIS table.
7. Teach-back: one sentence each on why you chose the "Use" word for `lower_depth` and `positional_uncertainty`.

Before you submit, read your table once more and ask: "Does every row describe the pH table, or did I copy a word from another table?"
