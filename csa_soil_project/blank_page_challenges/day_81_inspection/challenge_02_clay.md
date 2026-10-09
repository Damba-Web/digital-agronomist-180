# Challenge 2: Inspect the clay table (Ghana)

Closed book. Time: 20-30 minutes. Pass: 6/7.

Load the data:
```python
clay = run_query("SELECT * FROM wosis_clay WHERE country_name = 'Ghana';")
```

Tasks (write the code AND one sentence of what you learned):
1. How many rows and columns?
2. How many values are missing in `layer_name`? Count and percentage.
3. Summarise `value_avg` (min, median, mean, max). Give the unit.
4. How many rows come from each `dataset_id`?
5. How many distinct soil profiles are there?
6. What does one row represent?
7. Is any clay value impossible? State the valid range and your decision.

Write down everything you looked up.
