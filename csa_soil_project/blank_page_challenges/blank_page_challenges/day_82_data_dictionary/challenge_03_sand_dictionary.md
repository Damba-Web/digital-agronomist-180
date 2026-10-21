# Challenge 3: Build a mini data dictionary (sand table, Ghana)

Closed book. No cheat sheet. No AI. Time: 25-35 minutes. Pass: 6/7.
Write down everything you look up.

Load the data:
```python
sand = run_query("SELECT * FROM wosis_sand WHERE country_name = 'Ghana';")
```

The 7 boxes for every column: Column Name, Meaning, Unit, Data Type, Source, Cleaning Rule, Use in Project.
Allowed "Use in Project" words: target, predictor, grouping, location, metadata, unused, needs cleaning.

Tasks:
1. Print the data type of every column. Write the command and paste the output.
2. Which columns have only ONE unique value? Write the command, list the columns, and say what we call such columns.
3. How many missing values are in `layer_name`? Count and percentage.
4. Run `value_counts()` on `positional_uncertainty`. List the bands and counts. Is the column a number or text?
5. Look at the first 5 rows of `value` and `value_avg`. Explain in one sentence why `value` must not be a predictor.
6. Fill in all 7 boxes for these 5 columns: `value_avg`, `upper_depth`, `dataset_id`, `profile_id`, `positional_uncertainty`.
7. Teach-back: explain in one sentence each why you chose the "Use" word for `dataset_id` and `profile_id`.

Rules for the boxes:
- Each box answers its own question. Do not put a job word in the Cleaning box.
- Units belong to measurements. Labels have none.
- Take the data type from the output of task 1, not from memory.
