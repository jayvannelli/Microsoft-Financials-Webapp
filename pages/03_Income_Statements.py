import streamlit as st
import pandas as pd

from src.data import annual_income_statements, quarterly_income_statements
from src.constants import DROP_COLUMN_NAMES


def display_income_statements(income_statements: pd.DataFrame):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Income")
        st.bar_chart(income_statements, y="revenue")
        st.bar_chart(income_statements, y="costOfRevenue")
        st.bar_chart(income_statements, y="grossProfit")
        st.bar_chart(income_statements, y="ebitda")
        st.bar_chart(income_statements, y="operatingIncome")
        st.bar_chart(income_statements, y="incomeBeforeTax")
        st.bar_chart(income_statements, y="netIncome")
        st.bar_chart(income_statements, y="interestIncome")

    with col2:
        st.subheader("Expenses")
        st.bar_chart(income_statements, y="costAndExpenses")
        st.bar_chart(income_statements, y="operatingExpenses")
        st.bar_chart(income_statements, y="sellingGeneralAndAdministrativeExpenses")
        st.bar_chart(income_statements, y="sellingAndMarketingExpenses")
        st.bar_chart(income_statements, y="researchAndDevelopmentExpenses")
        st.bar_chart(income_statements, y="incomeTaxExpense")
        st.bar_chart(income_statements, y="depreciationAndAmortization")
        st.bar_chart(income_statements, y="generalAndAdministrativeExpenses")
        st.bar_chart(income_statements, y="totalOtherIncomeExpensesNet")
        st.bar_chart(income_statements, y="otherExpenses")
        st.bar_chart(income_statements, y="interestExpense")

    with col3:
        st.subheader("Ratios")
        st.bar_chart(income_statements, y="grossProfitRatio")
        st.bar_chart(income_statements, y="ebitdaratio")
        st.bar_chart(income_statements, y="operatingIncomeRatio")
        st.bar_chart(income_statements, y="incomeBeforeTaxRatio")
        st.bar_chart(income_statements, y="netIncomeRatio")

        st.subheader("Earnings & shares outstanding")
        st.bar_chart(income_statements, y="eps")
        st.bar_chart(income_statements, y="epsdiluted")
        st.bar_chart(income_statements, y="weightedAverageShsOut")
        st.bar_chart(income_statements, y="weightedAverageShsOutDil")


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
        annual_inc_statements = annual_inc_statements.drop(columns=DROP_COLUMN_NAMES)
        display_income_statements(annual_inc_statements)

    with quarterly_inc_statements_tab:
        quarterly_inc_statements = quarterly_inc_statements.drop(columns=DROP_COLUMN_NAMES)
        display_income_statements(quarterly_inc_statements)


if __name__ == "__main__":
    main()
