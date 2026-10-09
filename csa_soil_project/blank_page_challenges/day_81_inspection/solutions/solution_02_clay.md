# Solution 2: Clay (Ghana)

```python
clay.shape                                 # (801, 19)
clay['layer_name'].isnull().sum()          # 155 missing (646 non-null) -> 19.3%
clay['value_avg'].describe()               # min 0.0, median 31.0, mean 30.57, max 72.0 (g/100g)
clay['dataset_id'].value_counts()
clay['profile_id'].nunique()               # 216
```

Expected `dataset_id` counts: AF-AfSP 518, AF-AfSIS-I 96, WD-WISE 87, US-NCSS 73, WD-ISIS 27.

Task 6: one row = one soil layer.
Task 7: clay is a percentage of soil mass (g/100g), so the valid range is 0-100. Min 0.0 and max 72.0 are both possible. A 0.0 is plausible (very sandy soil) but check it during cleaning. Decision: keep.
