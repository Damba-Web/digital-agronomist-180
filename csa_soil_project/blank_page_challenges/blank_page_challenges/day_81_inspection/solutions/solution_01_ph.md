# Solution 1: pH (Ghana)

```python
ph.shape                                   # (2044, 19)
ph['layer_name'].isnull().sum()            # 1302 missing (742 non-null) -> 63.7%
ph['value_avg'].describe()                 # min 3.8, median 5.6, mean 5.85, max 8.9
ph['dataset_id'].value_counts()
ph['profile_id'].nunique()                 # 437
```

Expected `dataset_id` counts: GH-GhaSP 937, AF-AfSP 820, AF-AfSIS-I 96, WD-WISE 89, US-NCSS 73, WD-ISIS 29.

Task 6: one row = one soil layer (one depth slice of one profile).
Task 7: the pH scale is 0-14. Nothing is impossible. 3.8 is acidic and unusual but plausible. Decision: keep.

Common mistakes:
- Reporting the number of non-null values instead of the missing count.
- Calling the mean the median (the median is the 50% row).
- Calling 3.8 suspicious (it is a false alarm).
