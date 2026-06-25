-- ============================================
-- Mutual Fund Analytics - SQLite Star Schema
-- ============================================

DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_fund;

------------------------------------------------
-- Dimension: Fund
------------------------------------------------

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT

);

------------------------------------------------
-- Dimension: Date
------------------------------------------------

CREATE TABLE dim_date (

    date DATE PRIMARY KEY,

    year INTEGER,
    month INTEGER,
    day INTEGER,
    quarter INTEGER

);

------------------------------------------------
-- Fact: NAV
------------------------------------------------

CREATE TABLE fact_nav (

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    PRIMARY KEY(amfi_code, date),

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(date)
        REFERENCES dim_date(date)

);

------------------------------------------------
-- Fact: Transactions
------------------------------------------------

CREATE TABLE fact_transactions (

    investor_id INTEGER,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)

);

------------------------------------------------
-- Fact: Performance
------------------------------------------------

CREATE TABLE fact_performance (

    amfi_code INTEGER PRIMARY KEY,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)

);

------------------------------------------------
-- Fact: AUM
------------------------------------------------

CREATE TABLE fact_aum (

    date DATE,

    fund_house TEXT,

    aum_lakh_crore REAL,

    aum_crore REAL,

    num_schemes INTEGER

);