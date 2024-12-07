import streamlit as st
import pandas as pd 

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

st.write("#### 6. Color-Picker : To fetch hex code of color as variable. ")
st.code("""st.color_picker("Choose Color")""")
color = st.color_picker("Choose Color")
st.write(f"##### The color code is {color}")

st.divider()

st.write("#### 7. File Uploader : To upload file. ")
st.caption("let's take an example to input csv file.")
st.code("""
# Application based example : 
file = st.file_uploader("Enter .csv file")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
""")
file = st.file_uploader("Enter .csv file")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)

st.divider()

st.write("#### 8. File Downloader : To download the processed file. ")
st.caption("let's take an example where we would the uploaded file.")
st.code("""
st.download_button("Download csv file",
                    file,
                    file_name="download.csv",
                    mime="text/csv")
""")
if file:
    st.download_button("Download csv file",file,file_name="download.csv",mime="text/csv")
else:
    st.warning("Please upload the file.")
st.divider()

st.write("#### 9. Expander : A row that expands to display more data. ")
st.code("""
with st.expander("Expand Me"):
    st.write("Line 1")
    st.write("Line 2")
    st.image("Streamlit/static/cat.jpg",width=100)
    st.success("Hii")
""")
with st.expander("Expand Me"):
    st.write("Line 1")
    st.write("Line 2")
    st.image("Streamlit/static/cat.jpg",width=100)
    st.success("Hii")

st.divider()

st.write("##### 10. popover : It's concept is similar to expander but it opens as a pop up. ")
st.code("""
with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")
""")
with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.divider()

st.write("##### 11. pills, Segmented_control, multiselect : to select Multiple options")
st.code("""
options = ["North", "East", "South", "West"]

selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

selection2 = st.segmented_control("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection2}.")

selection3 = st.multiselect("Directions",options,["North", "South"],)
st.markdown(f"Your selected options: {selection3}.")
""")
options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")
selection2 = st.segmented_control("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection2}.")
selection3 = st.multiselect("Directions",options,["North", "South"],)
st.markdown(f"Your selected options: {selection3}.")
st.divider()

st.write("##### 12. Logo : to change/add logo of sidebar and main page")
st.code("""
sidebar_logo = "Streamlit/static/logo.png"
main_body_logo = "Streamlit/static/logo.png"
if st.checkbox("Show logo : "):
    st.logo(sidebar_logo, icon_image=main_body_logo)
""")

sidebar_logo = "Streamlit/static/logo.png"
main_body_logo = "Streamlit/static/logo.png"
if st.checkbox("Show logo : "):
    st.logo(sidebar_logo, icon_image=main_body_logo)

st.write("You can check the results : At the top of sidebar and on the main page (if you minimize the sidebar)")

st.divider()

st.write("##### 13. HTML : to add HTML & CSS based styling and structuring")
st.code("""st.html("<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>")""")

st.html("<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>")

st.divider()

st.write("##### 14. Switch page : to go to next/ any other webpage")
st.code("""
if st.button("Help"):
    st.switch_page("Pages/Help.py")""")

if st.button("Help"):
    st.switch_page("Pages/Help.py")

st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("8_8 Sample Website.py",label = ":green-background[Next page >]")
st.divider()

