import streamlit as st

from src.data import annual_balance_sheets, quarterly_balance_sheets
from src.liquidity import cash_ratio, current_ratio, quick_ratio
from src.leverage import debt_to_equity, equity_multiplier


def main():
    st.set_page_config("$MFT Analysis", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. financial analysis")

    annual_bal_sheets = annual_balance_sheets()
    quarterly_bal_sheets = quarterly_balance_sheets()

    liquidity_ratios_tab, leverage_ratios_tab = st.tabs(
        ["Liquidity Ratios", "Leverage Ratios"]
    )

    with liquidity_ratios_tab:
        st.subheader("Liquidity Ratios")

        left_column, right_column = st.columns(2)

        annual_current_ratios = current_ratio(annual_bal_sheets)
        quarterly_current_ratios = current_ratio(quarterly_bal_sheets)

        with left_column:
            st.write("Annual current ratios")
            st.bar_chart(annual_current_ratios)

        with right_column:
            st.write("Quarterly current ratios")
            st.bar_chart(quarterly_current_ratios)

        annual_quick_ratios = quick_ratio(annual_bal_sheets)
        quarterly_quick_ratios = quick_ratio(quarterly_bal_sheets)

        with left_column:
            st.write("Annual quick ratios")
            st.bar_chart(annual_quick_ratios)
        with right_column:
            st.write("Quarterly quick ratios")
            st.bar_chart(quarterly_quick_ratios)

        annual_cash_ratios = cash_ratio(annual_bal_sheets)
        quarterly_cash_ratios = cash_ratio(quarterly_bal_sheets)

        with left_column:
            st.write("Annual cash ratios")
            st.bar_chart(annual_cash_ratios)
        with right_column:
            st.write("Quarterly cash ratios")
            st.bar_chart(quarterly_cash_ratios)

    with leverage_ratios_tab:
        st.subheader("Leverage Ratios")

        left_column, right_column = st.columns(2)

        annual_debt_to_equity_ratios = debt_to_equity(annual_bal_sheets)
        quarterly_debt_to_equity_ratios = debt_to_equity(quarterly_bal_sheets)

        with left_column:
            st.write("Annual debt to equity ratios")
            st.bar_chart(annual_debt_to_equity_ratios)
        with right_column:
            st.write("Quarterly debt to equity ratios")
            st.bar_chart(quarterly_debt_to_equity_ratios)

        annual_equity_multiplier = equity_multiplier(annual_bal_sheets)
        quarterly_equity_multiplier = equity_multiplier(quarterly_bal_sheets)

        with left_column:
            st.write("Annual equity multiplier")
            st.bar_chart(annual_equity_multiplier)
        with right_column:
            st.write("Quarterly equity multiplier")
            st.bar_chart(quarterly_equity_multiplier)


if __name__ == "__main__":
    main()
