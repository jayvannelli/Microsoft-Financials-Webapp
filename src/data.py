import pandas as pd


def annual_balance_sheets():
    return pd.read_csv("data/msft_annual_bal_sheet.csv").set_index("date")


def quarterly_balance_sheets():
    return pd.read_csv("data/msft_quarterly_bal_sheet.csv").set_index("date")


def annual_income_statements():
    return pd.read_csv("data/msft_annual_inc_stmt.csv").set_index("date")


def quarterly_income_statements():
    return pd.read_csv("data/msft_quarterly_inc_stmt.csv").set_index("date")


def annual_cash_flows():
    return pd.read_csv("data/msft_annual_cash_flow.csv").set_index("date")


def quarterly_cash_flows():
    return pd.read_csv("data/msft_quarterly_cash_flow.csv").set_index("date")
