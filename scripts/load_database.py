from pathlib import Path
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# ======================================================
# Paths
# ======================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_PATH = PROJECT_ROOT / "data" / "processed"

SQL_PATH = PROJECT_ROOT / "sql"

DATABASE_PATH = PROJECT_ROOT / "database"

DATABASE_PATH.mkdir(exist_ok=True)

DB_FILE = DATABASE_PATH / "bluestock_mf.db"

# ======================================================
# Create SQLite Engine
# ======================================================

engine = create_engine(f"sqlite:///{DB_FILE}")

# ======================================================
# Execute schema.sql
# ======================================================

print("=" * 60)
print("Creating Database Schema...")
print("=" * 60)

conn = sqlite3.connect(DB_FILE)

with open(SQL_PATH / "schema.sql", "r") as file:
    schema = file.read()

conn.executescript(schema)

conn.commit()
conn.close()

print("Schema Created Successfully.\n")

# ======================================================
# Load Cleaned CSVs
# ======================================================

datasets = {

    "dim_fund": "clean_fund_master.csv",

    "fact_nav": "clean_nav_history.csv",

    "fact_transactions": "clean_investor_transactions.csv",

    "fact_performance": "clean_scheme_performance.csv",

    "fact_aum": "clean_aum_by_fund_house.csv",

    "monthly_sip_inflows": "clean_monthly_sip_inflows.csv",

    "category_inflows": "clean_category_inflows.csv",

    "industry_folio_count": "clean_industry_folio_count.csv",

    "portfolio_holdings": "clean_portfolio_holdings.csv",

    "benchmark_indices": "clean_benchmark_indices.csv"

}

print("=" * 60)
print("Loading Data...")
print("=" * 60)

for table, file in datasets.items():

    df = pd.read_csv(RAW_PATH / file)

    df.to_sql(

        table,

        engine,

        if_exists="replace",

        index=False

    )

    print(f"{table:<30} {len(df)} rows")

print("\nDatabase Loaded Successfully!")

# ======================================================
# Verify Row Counts
# ======================================================

print("\n")
print("=" * 60)
print("Verifying Row Counts")
print("=" * 60)

connection = engine.connect()

for table in datasets.keys():

    count = pd.read_sql(

        f"SELECT COUNT(*) as total FROM {table}",

        connection

    )

    print(f"{table:<30} {count.iloc[0,0]} rows")

connection.close()

print("\nVerification Completed Successfully.")