import streamlit as st

# Let's begin to learn Streamlit: 
st.title("Intro to Streamlit - Tutorial")
st.write("Streamlit is a service which can help us create easy and fast paced python website in less time.")

st.image("Streamlit/static/logo.png",width=1200)
st.markdown("<h3 style='text-align: right;'> - By KARTIK HAJELA </n3>", unsafe_allow_html=True)

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

# pages
home = st.Page("Streamlit/Pages/Home.py", title="Home")
initialization = st.Page("Streamlit/Pages/0_0 Initialization", title="0 Initialization")
textElement = st.Page("Streamlit/Pages/1_1 Text Element", title="1 Text Element")
visualElement = st.Page("Streamlit/Pages/2_2 Visual Element", title="2 Visual Element")
dataElement = st.Page("Streamlit/Pages/3_3 Data Element", title="3 Data Element")
chartElement = st.Page("Streamlit/Pages/4_4 Chart Element", title="4 Chart Element")
formElement = st.Page("Streamlit/Pages/5_5 Form Element", title="5 Form Element")
advanceFormElement = st.Page("Streamlit/Pages/6_6 Advance Form Element", title="6 Advance Form Element")
layout = st.Page("Streamlit/Pages/7 Layout", title="7 Layout")
help = st.Page("Streamlit/Pages/Help", title="Help")


# navigation
pages = {
    "": [initialization = st.Page("Streamlit/Pages/0_0 Initialization", title="0 Initialization")
textElement,visualElement,dataElement,chartElement,formElement,advanceFormElement,layout,help],
}
nav = st.navigation(pages)
nav.run()
