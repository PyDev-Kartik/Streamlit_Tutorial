import streamlit as st

st.header("2. Visual Elements :")
st.write("1. Buttons : Used to perform some set of function.")
st.code("""
        # An sample exaple of how button works : 
        if st.button("Mood Healer"):
            st.write("Happy Mood 😊")
        else:
            st.write("Sad Mood 😔")""")
if st.button("Mood Healer"):
    st.write("Happy Mood 😊")
else:
    st.write("Sad Mood 😔")

st.divider()

st.write("2. Image : we can display the images in streamlit")
st.caption("To do this, first initialise the path of directory where the image file is : ")
path = r"C:\Users\Kartik\Desktop\KDocuments\Programming\3. Python programming\AI Env\static\cat.jpg"
new_path = "C:\\Users\\Kartik\\Desktop\\KDocuments\\Programming\\3. Python programming\\AI Env\\static\\cat.jpg"
st.write("For me it's in :")
st.write(f""" :blue-background["{path}"]""")
st.write("""•   But python does't supports this addressing. So we would have to solve it. By introducing double-backslash mechanism for error control""")
st.write("We can modify our path as :")
st.image("Streamlit/static/img_path.png")

st.code("""
# Code to display image of a cat : 
# (Due to python's encoding it might not reflect below,
#  so the image of IDE is provided for the reference)
st.image("C:\\Users\\Kartik\\Desktop\\KDocuments\\Programming\\3. Python programming\\AI Env\\static\\cat.jpg",
        caption="Cat in office",width=200)
""") 

st.image("static/code.png",width=5000)

# Code to display image of a cat :
st.image("static/cat.jpg",caption="Cat in office",width=200)


st.divider()



st.write("3. name3 : Define")
st.code("""#code""")

st.divider()
