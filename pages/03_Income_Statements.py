import streamlit as st

from src.data import annual_income_statements, quarterly_income_statements
from src.constants import DROP_COLUMN_NAMES


def main():
    st.set_page_config("$MSFT Income Statements", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. income statements")

    annual_inc_statements = annual_income_statements()
    quarterly_inc_statements = quarterly_income_statements()

    with st.sidebar:
        st.subheader("Income statements date ranges")

        st.subheader("Annual")
        st.write(f"Start date: {annual_inc_statements.index[-1]}")
        st.write(f"End end: {annual_inc_statements.index[0]}")

        st.subheader("Quarterly")
        st.write(f"Start date: {quarterly_inc_statements.index[-1]}")
        st.write(f"End date: {quarterly_inc_statements.index[0]}")

    annual_inc_statements_tab, quarterly_inc_statements_tab = st.tabs(
        ["Annual Income Statements", "Quarterly Income Statements"]
    )

    with annual_inc_statements_tab:
        st.write("Annual income statements")
        annual_inc_statements = annual_inc_statements.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(annual_inc_statements)

    with quarterly_inc_statements_tab:
        st.write("Quarterly income statements")
        quarterly_inc_statements = quarterly_inc_statements.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(quarterly_inc_statements)


if __name__ == "__main__":
    main()
