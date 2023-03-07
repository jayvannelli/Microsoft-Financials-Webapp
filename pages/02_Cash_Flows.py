import streamlit as st

from src.data import annual_cash_flows, quarterly_cash_flows
from src.constants import DROP_COLUMN_NAMES


def main():
    st.set_page_config("$MSFT Cash Flows", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. cash flows")

    annual_cfs = annual_cash_flows()
    quarterly_cfs = quarterly_cash_flows()

    annual_cfs_tab, quarterly_cfs_tab = st.tabs(
        ["Annual Cash Flow Statements", "Quarterly Cash Flow Statements"]
    )

    with annual_cfs_tab:
        st.write("Annual cash flow statements")
        annual_cfs = annual_cfs.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(annual_cfs)

    with quarterly_cfs_tab:
        st.write("Quarterly cash flow statements")
        quarterly_cfs = quarterly_cfs.drop(columns=DROP_COLUMN_NAMES)
        st.dataframe(quarterly_cfs)


if __name__ == "__main__":
    main()
