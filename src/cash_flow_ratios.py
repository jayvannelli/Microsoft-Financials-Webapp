import pandas as pd


def fcf_to_ocf(cash_flows: pd.DataFrame) -> pd.Series:
    """Free cash flow (fcf) / operating cash flow (ocf)."""
    return cash_flows['freeCashFlow'] / cash_flows['operatingCashFlow']
