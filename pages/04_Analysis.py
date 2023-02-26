import streamlit as st

from src.data import (
    annual_balance_sheets,
    quarterly_balance_sheets,
    annual_income_statements,
    quarterly_income_statements,
)

from src.liquidity import cash_ratio, current_ratio, quick_ratio
from src.leverage import debt_to_equity, equity_multiplier
from src.profitability import gross_profit_margin, operating_profit_margin, pretax_profit_margin, net_profit_margin


def main():
    st.set_page_config("$MFT Analysis", page_icon=":bar_chart:", layout="wide")
    st.title("Microsoft Corp. financial analysis")

    annual_bal_sheets = annual_balance_sheets()
    quarterly_bal_sheets = quarterly_balance_sheets()
    annual_inc_statements = annual_income_statements()
    quarterly_inc_statements = quarterly_income_statements()

    profitability_ratios_tab, liquidity_ratios_tab, leverage_ratios_tab = st.tabs(
        ["Profitability Ratios", "Liquidity Ratios", "Leverage Ratios"]
    )

    with profitability_ratios_tab:
        st.subheader("Profitability Ratios")

        left_column, right_column = st.columns(2)

        with left_column:
            col1, col2 = st.columns(2)
            with col1:
                st.write("Annual EPS")
                st.bar_chart(annual_inc_statements['eps'])
            with col2:
                st.write("Annual EPS (diluted)")
                st.bar_chart(annual_inc_statements['epsdiluted'])

        with right_column:
            col1, col2 = st.columns(2)
            with col1:
                st.write("Quarterly EPS")
                st.bar_chart(quarterly_inc_statements['eps'])
            with col2:
                st.write("Quarterly EPS (diluted)")
                st.bar_chart(quarterly_inc_statements['epsdiluted'])

        annual_gross_profit_margin = gross_profit_margin(annual_inc_statements)
        quarterly_gross_profit_margin = gross_profit_margin(quarterly_inc_statements)

        with left_column:
            st.write("Annual gross profit margin")
            st.bar_chart(annual_gross_profit_margin)
        with right_column:
            st.write("Quarterly gross profit margin")
            st.bar_chart(quarterly_gross_profit_margin)

        annual_operating_profit_margin = operating_profit_margin(annual_inc_statements)
        quarterly_operating_profit_margin = operating_profit_margin(quarterly_inc_statements)

        with left_column:
            st.write("Annual operating profit margin")
            st.bar_chart(annual_operating_profit_margin)
        with right_column:
            st.write("Quarterly operating profit margin")
            st.bar_chart(quarterly_operating_profit_margin)

        annual_pretax_profit_margin = pretax_profit_margin(annual_inc_statements)
        quarterly_pretax_profit_margin = pretax_profit_margin(quarterly_inc_statements)

        with left_column:
            st.write("Annual pretax profit margin")
            st.bar_chart(annual_pretax_profit_margin)
        with right_column:
            st.write("Quarterly pretax profit margin")
            st.bar_chart(quarterly_pretax_profit_margin)

        annual_net_profit_margin = net_profit_margin(annual_inc_statements)
        quarterly_net_profit_margin = net_profit_margin(quarterly_inc_statements)

        with left_column:
            st.write("Annual net profit margin")
            st.bar_chart(annual_net_profit_margin)
        with right_column:
            st.write("Quarterly net profit margin")
            st.bar_chart(quarterly_net_profit_margin)

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
