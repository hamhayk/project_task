from screaping import sriping_vega
import streamlit as st
from get_currency import get_rate_by_date

st.title("vega.am կայքում ավտոմատ որոնման և ստացված արժեքեները արտարժույթով ցուցադրելու համակարգ")
search_term = st.text_input("Մուտքագրեք ապրանքի անունը")
lenght_of_list = st.text_input("Մուտքագրեք որոնման երկարությունը")

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


if st.button("Որոնել"):
    if search_term.strip() and lenght_of_list.strip():
        with st.spinner("Որոնում..."):
            prices, titles = sriping_vega(search_term, lenght_of_list)
        st.success("Որոնումը հաջողվեց")
        for title, price in zip(titles, prices):
            st.write(f"** {title}** - {price:,} AMD")
    else:
        st.warning("Խնդրում եմ մուտքագրեք որոնման նյութը")
