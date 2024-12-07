import streamlit as st
import pandas as pd

st.header("3. Data Elements : Pandas based")

st.write("0. Initialization : Initializing a pandas dataframe. ")
df = pd.DataFrame({
            "Name":["Kartik","Vedant","Shyamal","Abhi","Arya","Riya","Shivam"],
            "Age":[20,21,22,23,22,21,20],
            "Occupation":["Ai Developer","Ml Developer","SDE","Prompt Engineer","Mechanical Engineer","Front End Engineer","Mechatronics Engineer"]})
st.code(""" import pandas as pd
df = pd.DataFrame({
            "Name":["Kartik","Vedant","Shyamal","Abhi","Arya","Riya","Shivam"],
            "Age":[20,21,22,23,22,21,20],
            "Occupation":["Ai Developer","Ml Developer","SDE","Prompt Engineer","Mechanical Engineer","Front End Engineer","Mechatronics Engineer"]}
""")

st.divider()

st.write("1. Dataframe : Displaying pandas dataframe.")
st.code(""" st.dataframe(df)""")
st.dataframe(df)

st.divider()

st.write("2. Data Editor : Displaying pandas dataframe which can be edited")
st.code(""" edit_df = st.dataframe(edit_df)
        # This ensures that the new edited data is placed in a new dataframe 'edit_df'.To avoid data loss in base dataframe.""")
edit_df = st.data_editor(df)

st.divider()

st.write("3. Table : Displaying the pandas dataframe in static manner i.e in the form of a static table.")
st.code(""" st.table(df)""")
st.table(df)

st.divider()

st.write("4. Metrices : Displaying the metrice or data in new form.")
st.code(""" st.metric(label="Count",value="45")""")
st.metric(label="Count",value="45")
st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("4_4 Chart Element.py",label = ":green-background[Next page >]")
st.divider()

