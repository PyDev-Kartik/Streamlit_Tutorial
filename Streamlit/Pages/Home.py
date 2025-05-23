import streamlit as st

st.sidebar.title(":grey-background[Developer's Note :]")
with st.container(border=True):
  st.sidebar.write(":green[This Tutorial website is beginner friendly and it would keep on evolving, & providing more in-depth tutorials on 'Streamlit'.]")

# Let's begin to learn Streamlit: 
st.title("Intro to Streamlit - Tutorial")
st.write("Streamlit is a service which can help us create easy and fast paced python website in less time.")

st.image("Streamlit/static/logo.png",width=1200)
st.markdown("<h3 style='text-align: right;'> - By KARTIK HAJELA </n3>", unsafe_allow_html=True)
