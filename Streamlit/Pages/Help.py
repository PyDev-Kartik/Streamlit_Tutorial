import streamlit as st

# Let's begin to learn Streamlit: 
st.title("Help Dashboard : ")
col1,col2 = st.columns(2)

with col1:
    st.write("You can refer this video : ")
    st.link_button("Play","https://youtu.be/o8p7uQCGD0U")
    st.caption("CREDITS: Tech with Tim")

with col2:
    st.write("You can refer the official documentation : ")
    st.link_button("Open","https://docs.streamlit.io/")
    st.caption("CREDITS: Streamlit")

st.write("### If still in doubt you can leave a message at : ")
st.link_button("Instagram","https://www.instagram.com/kartik.hajela/")
st.link_button("Whatsapp","https://wa.me/+917984299346")
