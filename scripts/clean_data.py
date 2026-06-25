import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(exist_ok=True)

print("=" * 70)
print("Starting Data Cleaning Pipeline")
print("=" * 70)

# -------------------------------------------------------
# Helper Function
# -------------------------------------------------------

def save_dataset(df, filename):
    output_path = PROCESSED_PATH / filename
    df.to_csv(output_path, index=False)
    print(f"Saved -> {filename}")


##########################################################
# 1. FUND MASTER
##########################################################

print("\nCleaning Fund Master...")

fund = pd.read_csv(RAW_PATH / "01_fund_master.csv")

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

save_dataset(
    fund,
    "clean_fund_master.csv"
)


##########################################################
# 2. NAV HISTORY
##########################################################

print("\nCleaning NAV History...")

nav = pd.read_csv(
    RAW_PATH / "02_nav_history.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

nav = nav[
    nav["nav"] > 0
]

save_dataset(
    nav,
    "clean_nav_history.csv"
)


##########################################################
# 3. AUM
##########################################################

print("\nCleaning AUM...")

aum = pd.read_csv(
    RAW_PATH / "03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum = aum.drop_duplicates()

save_dataset(
    aum,
    "clean_aum_by_fund_house.csv"
)


##########################################################
# 4. SIP INFLOWS
##########################################################

print("\nCleaning SIP Inflows...")

sip = pd.read_csv(
    RAW_PATH / "04_monthly_sip_inflows.csv"
)

sip["month"] = pd.to_datetime(
    sip["month"],
    errors="coerce"
)

sip = sip.drop_duplicates()

save_dataset(
    sip,
    "clean_monthly_sip_inflows.csv"
)


##########################################################
# 5. CATEGORY INFLOWS
##########################################################

print("\nCleaning Category Inflows...")

category = pd.read_csv(
    RAW_PATH / "05_category_inflows.csv"
)

category["month"] = pd.to_datetime(
    category["month"],
    errors="coerce"
)

category = category.drop_duplicates()

save_dataset(
    category,
    "clean_category_inflows.csv"
)


##########################################################
# 6. INDUSTRY FOLIOS
##########################################################

print("\nCleaning Industry Folios...")

folios = pd.read_csv(
    RAW_PATH / "06_industry_folio_count.csv"
)

folios["month"] = pd.to_datetime(
    folios["month"],
    errors="coerce"
)

folios = folios.drop_duplicates()

save_dataset(
    folios,
    "clean_industry_folio_count.csv"
)


##########################################################
# 7. SCHEME PERFORMANCE
##########################################################

print("\nCleaning Scheme Performance...")

performance = pd.read_csv(
    RAW_PATH / "07_scheme_performance.csv"
)

performance = performance.drop_duplicates()

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

performance["negative_sharpe"] = (
    performance["sharpe_ratio"] < 0
)

performance["expense_ratio_valid"] = (
    performance["expense_ratio_pct"]
        .between(0.1, 2.5)
)

save_dataset(
    performance,
    "clean_scheme_performance.csv"
)


##########################################################
# 8. INVESTOR TRANSACTIONS
##########################################################

print("\nCleaning Investor Transactions...")

transactions = pd.read_csv(
    RAW_PATH / "08_investor_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
        .str.strip()
        .str.title()
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

transactions = transactions[
    transactions["kyc_status"].isin(valid_kyc)
]

transactions = transactions.drop_duplicates()

save_dataset(
    transactions,
    "clean_investor_transactions.csv"
)


##########################################################
# 9. PORTFOLIO HOLDINGS
##########################################################

print("\nCleaning Portfolio Holdings...")

portfolio = pd.read_csv(
    RAW_PATH / "09_portfolio_holdings.csv"
)

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio = portfolio.drop_duplicates()

save_dataset(
    portfolio,
    "clean_portfolio_holdings.csv"
)


##########################################################
# 10. BENCHMARK
##########################################################

print("\nCleaning Benchmark Indices...")

benchmark = pd.read_csv(
    RAW_PATH / "10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark = benchmark.drop_duplicates()

save_dataset(
    benchmark,
    "clean_benchmark_indices.csv"
)

print("\n")
print("=" * 70)
print("Data Cleaning Completed Successfully")
print("=" * 70)