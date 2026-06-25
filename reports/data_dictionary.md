# Mutual Fund Analytics - Data Dictionary

## Project Overview

This document describes the datasets used in the Mutual Fund Analytics project, including column definitions, data types, business meanings, and data sources.

**Data Source:** AMFI (Association of Mutual Funds in India) datasets and MFAPI (https://api.mfapi.in)

---

# 1. Fund Master (`clean_fund_master.csv`)

| Column             | Data Type | Description                            |
| ------------------ | --------- | -------------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier          |
| fund_house         | Text      | Name of the mutual fund company        |
| scheme_name        | Text      | Name of the mutual fund scheme         |
| category           | Text      | Fund category (Equity, Debt, etc.)     |
| sub_category       | Text      | Specific category within the fund type |
| plan               | Text      | Direct or Regular plan                 |
| launch_date        | Date      | Scheme launch date                     |
| benchmark          | Text      | Benchmark index used for comparison    |
| expense_ratio_pct  | Float     | Expense ratio (%)                      |
| exit_load_pct      | Float     | Exit load (%)                          |
| min_sip_amount     | Float     | Minimum SIP investment amount          |
| min_lumpsum_amount | Float     | Minimum lump sum investment amount     |
| fund_manager       | Text      | Fund manager name                      |
| risk_category      | Text      | Risk classification                    |
| sebi_category_code | Text      | SEBI category code                     |

---

# 2. NAV History (`clean_nav_history.csv`)

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| amfi_code | Integer   | AMFI scheme identifier |
| date      | Date      | NAV date               |
| nav       | Float     | Net Asset Value        |

---

# 3. AUM by Fund House (`clean_aum_by_fund_house.csv`)

| Column         | Data Type | Description                          |
| -------------- | --------- | ------------------------------------ |
| date           | Date      | Reporting date                       |
| fund_house     | Text      | Mutual fund company                  |
| aum_lakh_crore | Float     | Assets Under Management (Lakh Crore) |
| aum_crore      | Float     | Assets Under Management (Crore)      |
| num_schemes    | Integer   | Number of schemes managed            |

---

# 4. Monthly SIP Inflows (`clean_monthly_sip_inflows.csv`)

| Column                    | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | Date      | Reporting month                  |
| sip_inflow_crore          | Float     | SIP inflow amount                |
| active_sip_accounts_crore | Float     | Active SIP accounts              |
| new_sip_accounts_lakh     | Float     | Newly registered SIP accounts    |
| sip_aum_lakh_crore        | Float     | SIP Assets Under Management      |
| yoy_growth_pct            | Float     | Year-over-Year growth percentage |

---

# 5. Category Inflows (`clean_category_inflows.csv`)

| Column           | Data Type | Description          |
| ---------------- | --------- | -------------------- |
| month            | Date      | Reporting month      |
| category         | Text      | Mutual fund category |
| net_inflow_crore | Float     | Net inflow amount    |

---

# 6. Industry Folio Count (`clean_industry_folio_count.csv`)

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Date      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

---

# 7. Scheme Performance (`clean_scheme_performance.csv`)

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | AMFI scheme identifier        |
| scheme_name        | Text      | Scheme name                   |
| fund_house         | Text      | Mutual fund company           |
| category           | Text      | Fund category                 |
| plan               | Text      | Direct/Regular                |
| return_1yr_pct     | Float     | One-year return               |
| return_3yr_pct     | Float     | Three-year return             |
| return_5yr_pct     | Float     | Five-year return              |
| benchmark_3yr_pct  | Float     | Benchmark return              |
| alpha              | Float     | Alpha                         |
| beta               | Float     | Beta                          |
| sharpe_ratio       | Float     | Sharpe Ratio                  |
| sortino_ratio      | Float     | Sortino Ratio                 |
| std_dev_ann_pct    | Float     | Annualized standard deviation |
| max_drawdown_pct   | Float     | Maximum drawdown              |
| aum_crore          | Float     | Assets Under Management       |
| expense_ratio_pct  | Float     | Expense ratio                 |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | Text      | Risk grade                    |

---

# 8. Investor Transactions (`clean_investor_transactions.csv`)

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | Integer   | Investor identifier         |
| transaction_date   | Date      | Transaction date            |
| amfi_code          | Integer   | AMFI scheme identifier      |
| transaction_type   | Text      | SIP, Lumpsum, or Redemption |
| amount_inr         | Float     | Transaction amount          |
| state              | Text      | Investor state              |
| city               | Text      | Investor city               |
| city_tier          | Text      | City classification         |
| age_group          | Text      | Investor age group          |
| gender             | Text      | Investor gender             |
| annual_income_lakh | Float     | Annual income               |
| payment_mode       | Text      | Payment method              |
| kyc_status         | Text      | KYC verification status     |

---

# 9. Portfolio Holdings (`clean_portfolio_holdings.csv`)

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | AMFI scheme identifier   |
| stock_symbol      | Text      | Stock ticker             |
| stock_name        | Text      | Company name             |
| sector            | Text      | Industry sector          |
| weight_pct        | Float     | Portfolio weight         |
| market_value_cr   | Float     | Market value             |
| current_price_inr | Float     | Current stock price      |
| portfolio_date    | Date      | Portfolio reporting date |

---

# 10. Benchmark Indices (`clean_benchmark_indices.csv`)

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |
