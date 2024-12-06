# pages
home = st.Page("Home.py", title="Home")
initialization = st.Page("0_0 Initialization.py", title="0 Initialization")
textElement = st.Page("1_1 Text Element.py", title="1 Text Element")
visualElement = st.Page("2_2 Visual Element.py", title="2 Visual Element")
dataElement = st.Page("3_3 Data Element.py", title="3 Data Element")
chartElement = st.Page("4_4 Chart Element.py", title="4 Chart Element")
formElement = st.Page("5_5 Form Element.py", title="5 Form Element")
advanceFormElement = st.Page("6_6 Advance Form Element.py", title="6 Advance Form Element")
layout = st.Page("7_7 Layouts.py", title="7 Layout")
help = st.Page("Help.py", title="Help")


# navigation
pages = {
    "": [home,initialization,textElement,visualElement,dataElement,chartElement,formElement,advanceFormElement,layout,help],
}

nav = st.navigation(pages)
nav.run()

