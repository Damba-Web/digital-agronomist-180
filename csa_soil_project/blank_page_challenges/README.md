# Blank-Page Challenges

Closed-book practice for Python data analysis in agriculture and soil science.

## The rules
1. No cheat sheet. No AI. No Google while you work.
2. If you must look something up, write it down. That list is your next study list.
3. Try the tasks first. Open `solutions/` only after you finish.
4. Pass mark: 6 out of 7 tasks (about 86%). If you miss, fix your mistakes, then do the next similar challenge.

## What you need
- Python 3, Jupyter, pandas, SQLAlchemy, PostgreSQL
- The WoSIS Ghana tables (`wosis_orgc`, `wosis_phaq`, `wosis_clay`, `wosis_sand`) loaded into PostgreSQL
- A `db_config.py` with a `run_query()` function (keep it out of Git, and publish a `db_config.example.py` with no password)

Setup cell for every notebook:

```python
import sys
sys.path.append("../..")
import pandas as pd
from db_config import run_query
```

## Folder layout
```
blank_page_challenges/
  README.md
  day_81_inspection/
    challenge_01_ph.md
    challenge_02_clay.md
    solutions/
      solution_01_ph.md
      solution_02_clay.md
```

## Data licence and attribution
WoSIS data is licensed per row (CC BY 4.0, CC BY-NC 3.0, CC BY 3.0). All licences require attribution, and CC BY-NC rows cannot be used commercially without permission.
Do NOT commit raw data. The solution files hold only counts and summary statistics.
Cite WoSIS (ISRIC - World Soil Information) as the source.
