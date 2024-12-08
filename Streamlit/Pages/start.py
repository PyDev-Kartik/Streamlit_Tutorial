import streamlit as st

# pages
home = st.Page("Home.py", title="Home")
initialization = st.Page("Initialization.py", title="Initialization")
introduction = st.Page("0_0 Introduction.py", title="0 Introduction")
textElement = st.Page("1_1 Text Element.py", title="1 Text Element")
visualElement = st.Page("2_2 Visual Element.py", title="2 Visual Element")
dataElement = st.Page("3_3 Data Element.py", title="3 Data Element")
chartElement = st.Page("4_4 Chart Element.py", title="4 Chart Element")
formElement = st.Page("5_5 Form Element.py", title="5 Form Element")
advanceFormElement = st.Page("6_6 Advance Form Element.py", title="6 Advance Form Element")
layouts = st.Page("7_7 Layouts.py", title="7 Layout")
sample_web = st.Page("8_8 Sample Website.py", title="8 Sample Website")
deploy = st.Page("9_9 Deploy.py", title="9 Deploy")
help = st.Page("Help.py", title="Help")


# navigation
pages = {
    "": [home,initialization,introduction,textElement,visualElement,dataElement,chartElement,formElement,advanceFormElement,layouts,sample_web,deploy,help],
}

nav = st.navigation(pages)
nav.run()

