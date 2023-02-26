import pandas as pd


def gross_profit_margin(income_statements: pd.DataFrame) -> pd.Series:
    """Gross profit / revenue."""
    return income_statements['grossProfit'] / income_statements['revenue']


def operating_profit_margin(income_statements: pd.DataFrame) -> pd.Series:
    """Operating income / revenue."""
    return income_statements['operatingIncome'] / income_statements['revenue']


def pretax_profit_margin(income_statements: pd.DataFrame) -> pd.Series:
    """Income before tax / revenue."""
    return income_statements['incomeBeforeTax'] / income_statements['revenue']


def net_profit_margin(income_statements: pd.DataFrame) -> pd.Series:
    """Net income / revenue."""
    return income_statements['netIncome'] / income_statements['revenue']
