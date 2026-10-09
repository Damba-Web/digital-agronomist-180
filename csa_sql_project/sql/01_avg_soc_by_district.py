# ============================================
# 01_avg_soc_by_district.py
# Goal: Find average SOC by district and save as CSV
# ============================================

# STEP 1: Import the tools
import os
os.makedirs("outputs", exist_ok=True)
import pandas as pd
from sqlalchemy import create_engine
from db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# STEP 2: Build the connection (using the config file)
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# STEP 3: Paste the SQL query you already tested in DBeaver
query = """
SELECT district, AVG(soc_percent) AS avg_soc
FROM soil_samples
GROUP BY district
ORDER BY avg_soc DESC;
"""

# STEP 4: Run the query and get a DataFrame
df = pd.read_sql(query, engine)

# STEP 5: Print the result (so you can see it)
print(df)

# STEP 6: Save the result as a CSV file
df.to_csv("python 01_avg_soc_by_district.py/avg_soc_by_district.csv", index=False)
print("Saved to outputs/avg_soc_by_district.csv")