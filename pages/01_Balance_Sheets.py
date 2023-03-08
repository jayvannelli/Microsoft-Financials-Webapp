import pandas as pd
import streamlit as st

from src.data import annual_balance_sheets, quarterly_balance_sheets
from src.constants import DROP_COLUMN_NAMES


def display_balance_sheets(balance_sheets: pd.DataFrame):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Assets")
        st.bar_chart(balance_sheets, y="totalAssets")
        st.bar_chart(balance_sheets, y="totalCurrentAssets")
        st.bar_chart(balance_sheets, y="totalNonCurrentAssets")
        st.bar_chart(balance_sheets, y="cashAndShortTermInvestments")
        st.bar_chart(balance_sheets, y="shortTermInvestments")
        st.bar_chart(balance_sheets, y="netReceivables")
        st.bar_chart(balance_sheets, y="otherCurrentAssets")
        st.bar_chart(balance_sheets, y="cashAndCashEquivalents")
        st.bar_chart(balance_sheets, y="inventory")
        st.bar_chart(balance_sheets, y="propertyPlantEquipmentNet")
        st.bar_chart(balance_sheets, y="goodwill")
        st.bar_chart(balance_sheets, y="intangibleAssets")
        st.bar_chart(balance_sheets, y="longTermInvestments")
        st.bar_chart(balance_sheets, y="otherNonCurrentAssets")

    with col2:
        st.subheader("Liabilities")
        st.bar_chart(balance_sheets, y="totalLiabilities")
        st.bar_chart(balance_sheets, y="totalCurrentLiabilities")
        st.bar_chart(balance_sheets, y="totalNonCurrentLiabilities")
        st.bar_chart(balance_sheets, y="otherCurrentLiabilities")
        st.bar_chart(balance_sheets, y="deferredRevenue")
        st.bar_chart(balance_sheets, y="deferredRevenueNonCurrent")
        st.bar_chart(balance_sheets, y="accountPayables")
        st.bar_chart(balance_sheets, y="taxPayables")
        st.bar_chart(balance_sheets, y="totalDebt")
        st.bar_chart(balance_sheets, y="netDebt")
        st.bar_chart(balance_sheets, y="shortTermDebt")
        st.bar_chart(balance_sheets, y="longTermDebt")
        st.bar_chart(balance_sheets, y="deferredTaxLiabilitiesNonCurrent")
        st.bar_chart(balance_sheets, y="otherNonCurrentLiabilities")
        st.bar_chart(balance_sheets, y="deferredTaxLiabilitiesNonCurrent")
        st.bar_chart(balance_sheets, y="capitalLeaseObligations")

    with col3:
        st.subheader("Shareholder Equity")
        st.bar_chart(balance_sheets, y="commonStock")
        st.bar_chart(balance_sheets, y="retainedEarnings")
        st.bar_chart(balance_sheets, y="totalStockholdersEquity")
        st.bar_chart(balance_sheets, y="totalEquity")
        st.bar_chart(balance_sheets, y="accumulatedOtherComprehensiveIncomeLoss")
        st.bar_chart(balance_sheets, y="totalLiabilitiesAndStockholdersEquity")
        st.bar_chart(balance_sheets, y="totalLiabilitiesAndTotalEquity")
        st.bar_chart(balance_sheets, y="totalInvestments")


def main():
    st.set_page_config("$MSFT Balance Sheets", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. balance sheets")

    annual_bal_sheets = annual_balance_sheets()
    quarterly_bal_sheets = quarterly_balance_sheets()

    annual_bal_sheet_tab, quarterly_bal_sheet_tab = st.tabs(
        ["Annual Balance Sheets", "Quarterly Balance Sheets"]
    )

    with annual_bal_sheet_tab:
        annual_bal_sheets = annual_bal_sheets.drop(columns=DROP_COLUMN_NAMES)

        display_balance_sheets(annual_bal_sheets)

    with quarterly_bal_sheet_tab:
        quarterly_bal_sheets = quarterly_bal_sheets.drop(columns=DROP_COLUMN_NAMES)

        display_balance_sheets(quarterly_bal_sheets)


if __name__ == "__main__":
    main()
