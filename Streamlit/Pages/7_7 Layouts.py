import streamlit as st

st.header("7.Layouts : ")

st.write("#### 1. Tabs : ")

st.code("""
tab1,tab2,tab3,tab4 = st.tabs(["Tab 1","Tab 2","Tab 3","Tab Name"])

with tab1:
    st.write("You are in Tab 1.")
with tab2:
    st.write("You are in Tab 2.")
with tab3:
    st.write("You are in Tab 3.")
with tab4:
    st.write("You are in Tab Name.")""")

tab1,tab2,tab3,tab4 = st.tabs(["Tab 1","Tab 2","Tab 3","Tab Name"])

with tab1:
    st.write("You are in Tab 1.")
with tab2:
    st.write("You are in Tab 2.")
with tab3:
    st.write("You are in Tab 3.")
with tab4:
    st.write("You are in Tab Name.")

st.divider()

st.write("#### 2. Columns : ")

st.code("""
col1,col2 = st.columns(2)
        
with col1:
    st.subheader("Column 1")
    st.write("content for column 1")
with col2:
    st.subheader("Column 2")
    st.write("content for column 2")""")

col1,col2 = st.columns(2)
with col1:
    st.subheader("Column 1")
    st.write("content for column 1")
with col2:
    st.subheader("Column 2")
    st.write("content for column 2")

st.divider()

st.write("#### 3. Container : ")

st.code("""
with st.container(border=True):
    st.write("This is inside container.")
    st.write("You can think of containers as a grouping for elements. ")
    st.write("Containers help manage sections of the page. ")""")

with st.container(border=True):
    st.write("This is inside container.")
    st.write("You can think of containers as a grouping for elements. ")
    st.write("Containers help manage sections of the page. ")

st.divider()

st.write("#### 4. Placeholder : ")

st.code("""
placeholder = st.empty()
placeholder.write("This is empty placeholder,useful for dynamic content.")

if st.button("Update placeholder"):
    placeholder.write("The content in this placeholder has been updated")""")

placeholder = st.empty()
placeholder.write("This is empty placeholder,useful for dynamic content.")

if st.button("Update placeholder"):
    placeholder.write("The content in this placeholder has been updated")

st.divider()

st.write("#### 5. Sidebar : ")

st.code("""
st.sidebar.title("This is sidebar.")
st.sidebar.write("This is the description of sidebar.")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

if sidebar_input:
    st.write(f"You entered : {sidebar_input} in sidebar")""")

st.sidebar.title("This is sidebar.")
st.sidebar.write("This is the description of sidebar.")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

if sidebar_input:
    st.write(f"You entered : {sidebar_input} in sidebar")

st.divider()
st.subheader("Help :")
st.page_link("Help.py",label = "Click Here")
st.divider()
