-- ==========================================================
-- Mutual Fund Analytics
-- Day 2 Analytical SQL Queries
-- ==========================================================

------------------------------------------------------------
-- 1. Top 5 Funds by AUM
------------------------------------------------------------

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

------------------------------------------------------------
-- 2. Average NAV by Month
------------------------------------------------------------

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

------------------------------------------------------------
-- 3. Monthly SIP Inflow Trend
------------------------------------------------------------

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

------------------------------------------------------------
-- 4. Transactions by State
------------------------------------------------------------

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

------------------------------------------------------------
-- 5. Funds with Expense Ratio < 1%
------------------------------------------------------------

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

------------------------------------------------------------
-- 6. Top 10 Funds by 5-Year Return
------------------------------------------------------------

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

------------------------------------------------------------
-- 7. Average Return by Category
------------------------------------------------------------

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_3yr_return
FROM fact_performance
GROUP BY category;

------------------------------------------------------------
-- 8. Transaction Type Distribution
------------------------------------------------------------

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

------------------------------------------------------------
-- 9. Average NAV by Fund
------------------------------------------------------------

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;

------------------------------------------------------------
-- 10. Highest Rated Funds
------------------------------------------------------------

SELECT
    scheme_name,
    morningstar_rating,
    risk_grade
FROM fact_performance
ORDER BY morningstar_rating DESC;