import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus   # <-- NEW IMPORT
from db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Encode the password so special characters like @ don't break the URL
encoded_password = quote_plus(DB_PASSWORD)

# Now build the engine using the encoded password
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create the outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Test the connection
query = "SELECT * FROM soil_samples LIMIT 5;"
df = pd.read_sql(query, engine)

# Print and save
print(df)
df.to_csv("outputs/test_output.csv", index=False)
print("SUCCESS! File saved to outputs/test_output.csv")
