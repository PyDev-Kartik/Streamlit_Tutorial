import streamlit as st
st.title("This page is under constrution.")

st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("9_9 Deploy.py",label = ":green-background[Next page >]")
st.divider()

