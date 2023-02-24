import pandas as pd
import streamlit as st

from streamlit_extras.colored_header import colored_header
from streamlit_extras.toggle_switch import st_toggle_switch

from src.data import (
    annual_income_statements,
    quarterly_income_statements,
    annual_balance_sheets,
    quarterly_balance_sheets,
    annual_cash_flows,
    quarterly_cash_flows,
)


def current_ratio(balance_sheets: pd.DataFrame) -> pd.Series:
    return balance_sheets['totalCurrentAssets'] / balance_sheets['totalCurrentLiabilities']


def quick_ratio(balance_sheets: pd.DataFrame) -> pd.Series:
    return (
            (balance_sheets['totalCurrentAssets'] - balance_sheets['inventory'])
            / balance_sheets['totalCurrentLiabilities']
    )


def debt_to_equity(balance_sheets: pd.DataFrame) -> pd.Series:
    return balance_sheets['longTermDebt'] / balance_sheets['totalStockholdersEquity']


def equity_multiplier(balance_sheets: pd.DataFrame) -> pd.Series:
    return balance_sheets['totalAssets'] / balance_sheets['totalStockholdersEquity']



def main():
    st.set_page_config("MSFT Financials", page_icon=":bar_chart:", layout="wide")

    with st.sidebar:
        st.image("images/msft-logo.png", width=200)
        st.title("Microsoft Corporation ($MSFT) Financials")

        st.write("")
        quarterly_reports_toggle = st_toggle_switch(
            label="Display quarterly reports",
            key="quarterly_reports_switch",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",
            active_color="#11567f",
            track_color="#29B5E8",
        )


    income_statement_tab, balance_sheet_tab, cash_flow_tab = st.tabs(
        ["Income Statement", "Balance Sheet", "Cash Flow"]
    )

    with income_statement_tab:
        colored_header("Microsoft Corp. Income Statements", description="", color_name="blue-70")

        annual_inc_stmts = annual_income_statements()
        st.dataframe(annual_inc_stmts)

        quarterly_inc_stmts = quarterly_income_statements()
        st.dataframe(quarterly_inc_stmts)

    with balance_sheet_tab:
        colored_header("Microsoft Corp. Balance Sheets", description="", color_name="yellow-80")

        annual_bal_sheets = annual_balance_sheets()
        quarterly_bal_sheets = quarterly_balance_sheets()

        annual_current_ratio = current_ratio(annual_bal_sheets)
        quarterly_current_ratio = current_ratio(quarterly_bal_sheets)

        annual_quick_ratio = quick_ratio(annual_bal_sheets)
        quarterly_quick_ratio = quick_ratio(quarterly_bal_sheets)

        annual_debt_to_equity = debt_to_equity(annual_bal_sheets)
        quarterly_debt_to_equity = debt_to_equity(quarterly_bal_sheets)

        annual_equity_multiplier = equity_multiplier(annual_bal_sheets)
        quarterly_equity_multiplier = equity_multiplier(quarterly_bal_sheets)

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Liquidity Ratios")

            st.write("Current Ratio")

            if quarterly_reports_toggle:
                st.bar_chart(quarterly_current_ratio)
            else:
                st.bar_chart(annual_current_ratio)

            st.write("Quick Ratio")

            if quarterly_reports_toggle:
                st.bar_chart(quarterly_quick_ratio)
            else:
                st.bar_chart(annual_quick_ratio)

        with right_column:
            st.subheader("Leverage Ratios")

            st.write("Debt/Equity ratio")

            if quarterly_reports_toggle:
                st.bar_chart(quarterly_debt_to_equity)
            else:
                st.bar_chart(annual_debt_to_equity)

            st.write("Equity multiplier")

            if quarterly_reports_toggle:
                st.bar_chart(quarterly_equity_multiplier)
            else:
                st.bar_chart(annual_equity_multiplier)

        with st.expander("$MSFT Annual Balance Sheets DataFrame"):
            st.dataframe(annual_bal_sheets)

        with st.expander("$MSFT Quarterly Balance Sheets DataFrame"):
            st.dataframe(quarterly_bal_sheets)


    with cash_flow_tab:
        colored_header("Microsoft Corp. Cash Flows", description="", color_name="violet-70")

        annual_cf = annual_cash_flows()
        st.dataframe(annual_cf)

        quarterly_cf = quarterly_cash_flows()
        st.dataframe(quarterly_cf)


if __name__ == "__main__":
    main()
