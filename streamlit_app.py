import streamlit as st

from streamlit_extras.colored_header import colored_header
from src.data import (
    annual_income_statements,
    quarterly_income_statements,
    annual_balance_sheets,
    quarterly_balance_sheets,
    annual_cash_flows,
    quarterly_cash_flows,
)


def main():
    st.set_page_config("MSFT Financials", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corporation Financials")

    income_statement_tab, balance_sheet_tab, cash_flow_tab = st.tabs(
        ["Income Statement", "Balance Sheet", "Cash Flow"]
    )

    with income_statement_tab:
        colored_header("Microsoft Corporation ($MSFT) Income Statements", description="", color_name="blue-70")

        annual_inc_stmts = annual_income_statements()
        st.dataframe(annual_inc_stmts)

        quarterly_inc_stmts = quarterly_income_statements()
        st.dataframe(quarterly_inc_stmts)

    with balance_sheet_tab:
        colored_header("Microsoft Corporation ($MSFT) Balance Sheets", description="", color_name="yellow-80")

        annual_bal_sheets = annual_balance_sheets()
        st.dataframe(annual_bal_sheets)

        quarterly_bal_sheets = quarterly_balance_sheets()
        st.dataframe(quarterly_bal_sheets)

    with cash_flow_tab:
        colored_header("Microsoft Corporation ($MSFT) Cash Flows", description="", color_name="violet-70")

        annual_cf = annual_cash_flows()
        st.dataframe(annual_cf)

        quarterly_cf = quarterly_cash_flows()
        st.dataframe(quarterly_cf)


if __name__ == "__main__":
    main()
