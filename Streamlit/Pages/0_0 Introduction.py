import streamlit as st

st.header("0. Introduction : ")
st.write("#### 1. Why Streamlit ? ")
st.write("Streamlit is fast, less complex platform that helps us to integrate UI with our python programming. We can deploy our code as website and share it with others easily.")
st.divider()
st.write("#### 2. Structure of Code : ")
st.code("""
# SYNTAX :
import streamlit as st

#syntax --> st.elementname()
st.write("Hello Streamlit") """)

st.write("Implementation : ")
with st.container(border=True):
    st.write("Hello Streamlit")

st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("1_1 Text Element.py",label = ":green-background[Next page >]")
st.divider()
