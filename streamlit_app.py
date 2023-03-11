import streamlit as st


def main():
    st.title("Microsoft Corporation ($MSFT) Financials & Analysis")
    st.info("Data is obtained directly from Financial Modeling Prep (FMP)")

    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.image("images/msft-logo.png")
    with right_column:
        st.image("images/streamlit-logo.png")


if __name__ == "__main__":
    main()
