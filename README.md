# UPI Growth & Digital Payment Behavior Analysis

## Project Summary

This project analyzes the growth of India's Unified Payments Interface (UPI)
using monthly transaction statistics (banks live, transaction volume,
transaction value). The pipeline covers:

1. **Data cleaning** (Python/pandas) — fixing inconsistent date formats,
   missing values, and a duplicate record in the raw dataset.
2. **Growth & trend analysis** (Python) — CAGR, month-over-month and
   year-over-year growth, correlation analysis, and 6 charts.
3. **Interactive dashboard** (Power BI) — a 4-page report with KPIs,
   trend charts, slicers, and drill-down.
4. **Web dashboard** (Streamlit) — a Python-native, open-source
   alternative dashboard.
5. **Report & recommendations** — business insights derived from the
   analysis, written up for banks, fintechs, and policymakers.

## Key Findings (Quick Reference)

| Metric | Value |
|---|---|
| Approx. CAGR (Volume) | 38.78% per year |
| Peak volume month | March 2026 — 22,921.56 Mn transactions |
| Lowest volume month | January 2023 — 8,131.87 Mn transactions |
| Avg MoM Volume Growth | 2.83% |
| Avg MoM Value Growth | 2.57% |
| Correlation: Banks Live vs Volume | 0.98 |
| Correlation: Avg Txn Value vs Banks Live | -0.89 |


## Tech Stack

- **Python 3.14** — pandas, numpy, matplotlib, seaborn, plotly, streamlit
- **Power BI Desktop** — DAX measures, slicers,drill-down
- **Jupyter / VS Code** — notebook development
