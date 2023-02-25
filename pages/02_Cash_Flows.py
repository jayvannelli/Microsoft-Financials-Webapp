import streamlit as st

from src.data import annual_cash_flows, quarterly_cash_flows


def main():
    st.set_page_config("$MSFT Cash Flows", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. cash flows")

    annual_cfs = annual_cash_flows()
    quarterly_cfs = quarterly_cash_flows()

    st.write("Annual cash flow statements")
    st.dataframe(annual_cfs)

    st.write("Quarterly cash flow statements")
    st.dataframe(quarterly_cfs)


if __name__ == "__main__":
    main()
