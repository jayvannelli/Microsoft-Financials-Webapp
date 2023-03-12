import streamlit as st
import pandas as pd

from src.data import annual_cash_flows, quarterly_cash_flows
from src.constants import DROP_COLUMN_NAMES


def display_cash_flows(cash_flows: pd.DataFrame):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Operating Activities")
        st.bar_chart(cash_flows, y="netIncome")
        st.bar_chart(cash_flows, y="depreciationAndAmortization")
        st.bar_chart(cash_flows, y="deferredIncomeTax")
        st.bar_chart(cash_flows, y="changeInWorkingCapital")
        st.bar_chart(cash_flows, y="otherWorkingCapital")
        st.bar_chart(cash_flows, y="accountsReceivables")

        st.bar_chart(cash_flows, y="inventory")
        st.bar_chart(cash_flows, y="accountsPayables")
        st.bar_chart(cash_flows, y="netCashProvidedByOperatingActivities")

    with col2:
        st.subheader("Investing Activities")
        st.bar_chart(cash_flows, y="netCashUsedForInvestingActivites")
        st.bar_chart(cash_flows, y="otherInvestingActivites")
        st.bar_chart(cash_flows, y="investmentsInPropertyPlantAndEquipment")
        st.bar_chart(cash_flows, y="acquisitionsNet")
        st.bar_chart(cash_flows, y="purchasesOfInvestments")
        st.bar_chart(cash_flows, y="salesMaturitiesOfInvestments")
        st.bar_chart(cash_flows, y="effectOfForexChangesOnCash")

    with col3:
        st.subheader("Financing Activities")
        st.bar_chart(cash_flows, y="debtRepayment")
        st.bar_chart(cash_flows, y="stockBasedCompensation")
        st.bar_chart(cash_flows, y="commonStockIssued")
        st.bar_chart(cash_flows, y="commonStockRepurchased")
        st.bar_chart(cash_flows, y="dividendsPaid")
        st.bar_chart(cash_flows, y="netCashUsedProvidedByFinancingActivities")
        st.bar_chart(cash_flows, y="otherFinancingActivites")

        st.subheader("Cash Flows")
        st.bar_chart(cash_flows, y="netChangeInCash")
        st.bar_chart(cash_flows, y="otherNonCashItems")
        st.bar_chart(cash_flows, y="cashAtEndOfPeriod")
        st.bar_chart(cash_flows, y="cashAtBeginningOfPeriod")
        st.bar_chart(cash_flows, y="operatingCashFlow")
        st.bar_chart(cash_flows, y="capitalExpenditure")
        st.bar_chart(cash_flows, y="freeCashFlow")


def main():
    st.set_page_config("$MSFT Cash Flows", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. cash flows")

    annual_cfs = annual_cash_flows()
    quarterly_cfs = quarterly_cash_flows()

    with st.sidebar:
        st.subheader("Cash flows date ranges")

        st.subheader("Annual")
        st.write(f"Start date: {annual_cfs.index[-1]}")
        st.write(f"End end: {annual_cfs.index[0]}")

        st.subheader("Quarterly")
        st.write(f"Start date: {quarterly_cfs.index[-1]}")
        st.write(f"End date: {quarterly_cfs.index[0]}")

    annual_cfs_tab, quarterly_cfs_tab = st.tabs(
        ["Annual Cash Flow Statements", "Quarterly Cash Flow Statements"]
    )

    with annual_cfs_tab:
        annual_cfs = annual_cfs.drop(columns=DROP_COLUMN_NAMES)
        display_cash_flows(annual_cfs)

    with quarterly_cfs_tab:
        quarterly_cfs = quarterly_cfs.drop(columns=DROP_COLUMN_NAMES)
        display_cash_flows(quarterly_cfs)


if __name__ == "__main__":
    main()
