# db_config.py
# ============================================
# REUSABLE DATABASE CONNECTION
# ============================================

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus


def get_engine():
    """Returns a connection to the CSA PostgreSQL database."""
    DB_USER = "postgres"
    DB_PASSWORD = "your_real_password_here"   # <-- CHANGE THIS
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "csa_soil_project"

    encoded_password = quote_plus(DB_PASSWORD)
    connection_string = f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_string)


def run_query(query):
    """Runs a SQL query and returns a Pandas DataFrame."""
    engine = get_engine()
    return pd.read_sql(query, engine)
