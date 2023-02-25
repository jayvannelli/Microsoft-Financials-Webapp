import pandas as pd


def debt_to_equity(balance_sheets: pd.DataFrame) -> pd.Series:
    """Long term debt / total stockholders equity."""
    return balance_sheets['longTermDebt'] / balance_sheets['totalStockholdersEquity']


def equity_multiplier(balance_sheets: pd.DataFrame) -> pd.Series:
    """Long assets / total stockholders equity."""
    return balance_sheets['totalAssets'] / balance_sheets['totalStockholdersEquity']

