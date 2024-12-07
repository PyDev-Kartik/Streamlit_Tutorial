import streamlit as st
import time

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

st.image("Streamlit/static/code.png",width=5000)

st.write("### So this is one of the complex addressing methods,\n ### let's see a simpler one too : ")
st.code("""st.image("streamlit/static/cat.jpg",caption="Cat in office",width=200)""") 
# Code to display image of a cat :

st.image("Streamlit/static/cat.jpg",caption="Cat in office",width=200)


st.divider()

st.write("3. Audio : To display audio file.")

st.code("""st.audio("streamlit/static/multimedia/phonk.mp3",
          format="audio/mpeg", 
          loop=True,
          start_time=4,
          end_time=25,
          autoplay=True)""")

st.audio("Streamlit/static/multimedia/phonk.mp3",
          format="audio/mpeg", 
          loop=True,
          start_time=4,
          end_time=25,
          autoplay=True)

st.divider()

st.write("4. Audio-Input : To record audio.")

st.code("""voice2 = st.audio_input("Record a Voice note")""")

voice2 = st.audio_input("Record a Voice note")
st.write("Playing the recorded audio : ")
st.code("st.audio(voice2)")
st.audio(voice2)

st.divider()

st.write("5. Video : To display the video.")

st.code("""st.video("Streamlit/static/multimedia/phonk.mp4",
         format = "video/mp4",
         start_time = 4,
         subtitles = None,
         end_time = 25 ,
         loop = False,
         autoplay= False,
         muted= False)
""")

st.video("Streamlit/static/multimedia/phonk.mp4", format = "video/mp4", start_time = 4, subtitles = None, end_time = 25 , loop = False, autoplay= False, muted= False)

st.divider()

st.write("6. Camera-Input : To access the camera and click photos, save and access them.")

st.code("""
access = st.checkbox("Provide camera access : ")
if access:
    photo = st.camera_input("Click photo")
    if photo:
        st.image(photo)
""")

access = st.checkbox("Provide camera access : ")
if access:
    photo = st.camera_input("Click photo")
    if photo:
        st.image(photo)

st.divider()

st.write("7. Toast : To display quick message.")
st.code("""
text = st.text_input("Write anything")
if text : 
    st.toast('You inputted data sucessfully!', icon='😍')""")

text = st.text_input("Write any thing")
if text : 
    st.toast('You inputted data sucessfully!', icon='😍')

st.divider()

st.write("8. Balloon/Snow : To display ballons and snow as easter eggs.")

st.code("""
ch1 = st.checkbox("Ballon")
ch2 = st.checkbox("Snow")
if ch1:
    st.balloons()
if ch2:
    st.snow()""")

ch1 = st.checkbox("Ballon")
ch2 = st.checkbox("Snow")
if ch1:
    st.balloons()
if ch2:
    st.snow()

st.divider()

st.write("9. Spinner : To spin a wheel just like a loader it will load till our process finishes.")
st.caption("In the given example we have used time module to add extra time.")

st.code("""
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success("Done!")""")

st.video("Streamlit/static/multimedia/spinner.mp4",autoplay=True,loop=True)

st.divider()

st.write("10. Status : To display the current status of the process")
st.write("If the process is 'going-on' it would be displayed as : :blue-background[spinner]")
st.write("If the process is 'completed' it would be displayed as : :green[✓]")
st.write("If the process is 'completed' it would be displayed as : ⚠️")

st.code("""
#Code:
st.status("Running...",expanded=True,state='running')
st.status("Completed",expanded=True,state="complete")
st.status("error occured",expanded=True,state="error")""")

st.status("Running...",expanded=True,state='running')
st.status("Completed",expanded=True,state="complete")
st.status("error occured",expanded=True,state="error")

st.divider()

st.write("11. Chats : To display and send messages")
st.write("st.chat_input - to provide text-box to write message")
st.write("""st.chat_message("user",avatar="user") - to display message and avatar is used to signify who is writing message""")
st.caption("There are just two modes of avatar : user and assistant")

st.code('''
prompt = st.chat_input("Say, Hii")
if prompt:
    with st.chat_message("user",avatar="user"):
        st.write(prompt)
    with st.chat_message("AI",avatar="assistant"):
        st.write("Hello 👋")
''')
st.write("## Chats: ")
st.caption("(Write anything)")

chat=st.checkbox("Open chats")
if chat:
    prompt = st.chat_input("Say, Hii")
    if prompt:
        with st.chat_message("user",avatar="user"):
            st.write(prompt)
        with st.chat_message("AI",avatar="assistant"):
            st.write("Hello 👋")
   
st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("3_3 Data Element.py",label = ":green-background[Next page >]")
st.divider()

