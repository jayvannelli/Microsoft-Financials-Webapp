import pandas as pd


def current_ratio(balance_sheets: pd.DataFrame) -> pd.Series:
    """Total current assets / total current liabilities."""
    return balance_sheets['totalCurrentAssets'] / balance_sheets['totalCurrentLiabilities']


def quick_ratio(balance_sheets: pd.DataFrame) -> pd.Series:
    """Cash and short term investments + net receivables / total current liabilities."""
    return (
            (balance_sheets['cashAndShortTermInvestments'] + balance_sheets['netReceivables'])
            / balance_sheets['totalCurrentLiabilities']
    )


def cash_ratio(balance_sheets: pd.DataFrame) -> pd.Series:
    """Cash and cash equivalents / total current liabilities."""
    return balance_sheets['cashAndCashEquivalents'] / balance_sheets['totalCurrentLiabilities']
