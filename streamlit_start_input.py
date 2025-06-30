import streamlit as st
from get_currency import get_rate_by_date

currency = st.selectbox(
    "Choose currency",
    ("USD", "EUR", "RUB"),
index=None,
placeholder="currency..."
)
if st.button('Get Rate'):
    if currency:
        rate = rate = get_rate_by_date(currency)
        st.success(f"Exhcange rate for {currency}: {rate}")
    else:
        st.warning("Please select a currency first.")



