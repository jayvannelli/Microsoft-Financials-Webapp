import streamlit as st

from src.data import annual_income_statements, quarterly_income_statements


def main():
    st.set_page_config("$MSFT Income Statements", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. income statements")

    annual_inc_statements = annual_income_statements()
    quarterly_inc_statements = quarterly_income_statements()

    st.write("Annual income statements")
    st.dataframe(annual_inc_statements)

    st.write("Quarterly income statements")
    st.dataframe(quarterly_inc_statements)



if __name__ == "__main__":
    main()
