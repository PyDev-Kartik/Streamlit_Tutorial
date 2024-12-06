import streamlit as st

st.sidebar.title("Directory")

st.sidebar.page_link("Streamlit/Pages/Home.py", label="Home")
st.sidebar.page_link("Streamlit/Pages/0_0 Initialization.py", label="0 Initialization")
st.sidebar.page_link("Streamlit/Pages/1_1 Text Element.py", label="1 Text Element")
st.sidebar.page_link("Streamlit/Pages/2_2 Visual Element.py", label="2 Visual Element")
st.sidebar.page_link("Streamlit/Pages/3_3 Data Element.py", label="3 Data Element")
st.sidebar.page_link("Streamlit/Pages/4_4 Chart Element.py", label="4 Chart Element")
st.sidebar.page_link("Streamlit/Pages/5_5 Form Element.py", label="5 Form Element")
st.sidebar.page_link("Streamlit/Pages/6_6 Advance Form Element.py", label="6 Advance Form Element")
st.sidebar.page_link("Streamlit/Pages/7_7 Layout.py", label="7 Layout")
st.sidebar.page_link("Streamlit/Pages/Help.py", label="Help")

# Let's begin to learn Streamlit: 
st.title("Intro to Streamlit - Tutorial")
st.write("Streamlit is a service which can help us create easy and fast paced python website in less time.")

st.image("Streamlit/static/logo.png",width=1200)
st.markdown("<h3 style='text-align: right;'> - By KARTIK HAJELA </n3>", unsafe_allow_html=True)
