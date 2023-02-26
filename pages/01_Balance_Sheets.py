import streamlit as st

from src.data import annual_balance_sheets, quarterly_balance_sheets
from src.constants import DROP_COLUMN_NAMES


def main():
    st.set_page_config("$MSFT Balance Sheets", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. balance sheets")

    annual_bal_sheets = annual_balance_sheets()
    quarterly_bal_sheets = quarterly_balance_sheets()

    balance_sheet_col_names = annual_bal_sheets.drop(columns=DROP_COLUMN_NAMES).columns
    st.write(balance_sheet_col_names)

    st.write("Annual balance sheets statements")
    st.dataframe(annual_bal_sheets)

    st.write("Quarterly balance sheet statements")
    st.dataframe(quarterly_bal_sheets)


if __name__ == "__main__":
    main()