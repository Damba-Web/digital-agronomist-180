# Digital Agronomist: 180 Days
![Organic carbon by dataset](Figures/day_92_orgc_by_dataset.png)

I am an agronomist (MSc, RUDN University) learning Python, SQL and data analysis
to work on climate-smart agriculture and soil carbon. This repo holds my daily work,
from first Python lines to real soil-data projects.

## The plan
A 180-day curriculum in phases: Python basics, pandas, SQL and PostgreSQL,
a real soil-data project, then statistics and climate data.
Current progress is in [PROGRESS.md](PROGRESS.md).

## Projects
- [`csa_soil_project`](csa_soil_project/): WoSIS soil data for Ghana
  (organic carbon, pH, clay, sand) in PostgreSQL and pandas
- [`csa_sql_project`](csa_sql_project/): SQL practice

## Where things are
- `notes/` : study notes
- `PROGRESS.md` : what I finished each day
- `Reference document/` : reference material

Soil data: WoSIS, ISRIC World Soil Information.


# WoSIS Soil Data for Ghana

Joins 1,756 Ghana organic carbon layers with pH, clay and sand into one table,
checks the data quality, and flags impossible values.

- `agronomic_functions.py` : `count_rows`, `build_flat`, `quality_flags`
- `notebooks/` : daily notebooks by week
- `blank_page_challenges/` : closed-book practice challenges
- `db_config.example.py` : copy to `db_config.py` and add your own database details

Data: WoSIS (ISRIC), licensed per row. Raw data is not committed.

## Run all checks
From the `csa_soil_project` folder: `python run_checks.py`
It builds the flat table, runs the quality flags, the cleaning report and the dataset alarm,
and saves `Reports/run_checks_report.csv`. Exit code 0 = success, 1 = a check failed.