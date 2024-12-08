import streamlit as st

st.subheader("Directly jump on to the sub topics :",anchor="options")
with st.container(border=True):
        st.write("##### :grey-background[ • Section 1.Python Installation : [Link](#section-1)]", unsafe_allow_html=True)
        st.write("##### :grey-background[ • Section 2.Anaconda Installation : [Link](#section-2)]", unsafe_allow_html=True)
        st.write("##### :grey-background[ • Section 3.Vritual Environment Creation : [Link](#section-3)]", unsafe_allow_html=True)
        st.write("##### :grey-background[ • Section 4.Streamlit library Installation : [Link](#section-4)]", unsafe_allow_html=True)
st.divider()

st.header("• Section 1.Python Installation : ",anchor="section-1")
st.write("##### 1. You can download python from this link :")
st.link_button("Python Download link","https://www.python.org/downloads/")
st.write("##### 2. Make sure you choose the following settings :")
st.caption("Then hit install and wait.")
st.image("Streamlit/static/python.png")

st.write("##### 3. VS Code Installation : ")
st.write("You can download it from this link :")
st.link_button("VScode Download link","https://code.visualstudio.com/") 

st.write("##### 4. In VScode install certain Extensions : ")

col1,col2 = st.columns(2)
with col1:
        st.image("Streamlit/static/vs_ext1.png",caption="Step1: Select Extension")
with col2:
        st.image("Streamlit/static/vs_ext2.png",caption="Step2: Install these Extensions")
st.divider()



st.header("• Section 2.Miniconda Installation : ",anchor="section-2")
st.write("##### 1. You can download miniconda from this link :")
mi_col1, mi_col2, mi_col3 = st.columns(3)
with mi_col1:
        st.link_button("Windows link","https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe")
with mi_col2:
        st.write("<h4 style='text-align: left;'> OR </h4>", unsafe_allow_html=True)
with mi_col3:
        st.link_button("All OS link","https://www.anaconda.com/download/success")
st.write("##### 2. Make sure you choose the following settings :")
st.image("Streamlit/static/miniconda.png")

st.write("##### 3. You can fetch this from here :")
st.image("Streamlit/static/accessing_conda.png")

st.divider()

st.header("• Section 3.Vritual Environment Creation : ",anchor="section-3")
st.write("##### Syntax : cd path | setting the path as current directory")
st.code("cd C:\\Users\\Kartik\\Desktop\\KDocuments\\Programming\\3. Python programming\\AI Env")
st.write("""##### Syntax : conda create -n var_name python=3.7 | Creating virtual environment with "var_name" """)
st.code("conda create -n tf python=3.7")
st.write("##### Syntax : conda activate var_name | To activate virtual environment")
st.code("conda activate tf",language="bash")

st.write("#### Handling Jupyter Notebook : ")
st.write("##### pip install python_library | To install python library in virtual environment")
st.code("pip install jupyter",language="bash")
st.image("Streamlit/static/conda_terminal.png")
st.divider()
st.header("• Section 4.Streamlit library Installation : ",anchor="section-4")
st.subheader("Installation & Initialization :")

st.code("""pip install streamlit""")
st.write("NOTE: :blue-background[Intialize the same in the evironment variables.]")

st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("0_0 Introduction.py",label = ":green-background[Next page >]")
st.divider()
