# Challenge 1: Inspect the pH table (Ghana)

Closed book. Time: 20-30 minutes. Pass: 6/7.

Load the data:
```python
ph = run_query("SELECT * FROM wosis_phaq WHERE country_name = 'Ghana';")
```

Tasks (write the code AND one sentence of what you learned):
1. How many rows and columns?
2. How many values are missing in `layer_name`? Give the count and the percentage.
3. Summarise `value_avg` (min, median, mean, max). Name each one correctly.
4. How many rows come from each `dataset_id`?
5. How many distinct soil profiles are there?
6. What does one row represent?
7. Is any pH value impossible? State the valid range and your decision (keep, flag or delete).

Write down everything you looked up.
