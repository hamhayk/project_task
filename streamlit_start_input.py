import streamlit as st
from get_currency import get_rate_by_date

currency = st.selectbox(
    "Choose currency",
    ("USD", "EUR", "RUB"),
index=None,
placeholder="currency..."
)

#print(currency)



#print(st.slider)
if currency == None:
    pass
else:
    result = (get_rate_by_date(currency))

    print(result)

