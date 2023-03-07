import pandas as pd
import streamlit as st

from src.data import annual_balance_sheets, quarterly_balance_sheets
from src.constants import DROP_COLUMN_NAMES


def main():
    st.set_page_config("$MSFT Balance Sheets", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. balance sheets")

    annual_bal_sheets = annual_balance_sheets()
    quarterly_bal_sheets = quarterly_balance_sheets()

    annual_bal_sheet_tab, quarterly_bal_sheet_tab = st.tabs(
        ["Annual Balance Sheets", "Quarterly Balance Sheets"]
    )

    with annual_bal_sheet_tab:
        st.write("Annual balance sheets statements")
        annual_bal_sheets = annual_bal_sheets.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(annual_bal_sheets)

    with quarterly_bal_sheet_tab:
        st.write("Quarterly balance sheet statements")
        quarterly_bal_sheets = quarterly_bal_sheets.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(quarterly_bal_sheets)


if __name__ == "__main__":
    main()
