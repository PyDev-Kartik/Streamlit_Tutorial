import streamlit as st


st.header("1. Text elements : ")
st.write("1. st.title : Used to define the title of the web-page. For this page it is 'Intro to Streamlit'.")
st.code("""st.title("title")""")
st.write("2. st.header : Used to define a header.Just upscaled text. for this page it is 'Getting started with streamlit'.")
st.code("""st.header("header")""")
st.write("3. st.subheader : smaller font then header. in this page it is 'First code : '.")
st.code("""st.subheader("subheader")""")
st.write("4. st.write : used to print data on the web pages.")
st.code("""st.write("Hello world")""")
st.write("5. st.markdown : used to print data with some css stuff i.e text formatting on the web pages.")
st.code("""st.markdown("Hello world, Welcome to :blue-background[INDIA].")""")
st.markdown("Hello world, welcome to :blue-background[INDIA].")
st.write("6. st.code : used to display code.")
st.code("""st.code("print("Hello world")",language="python" # or java,c,c++)""")
st.code("""#Another example of st.code : (for better understanding) 
            a = 10
            b = 20
            sum = a+b
            print("a+b")""")

st.divider()
st.subheader(":green-background[st.write] in more brief : ")
st.write("This function is one of the most important and widely used function of the streamlit library.")
st.write("This function can write string,int,float,list,tuple,dictionary")
st.subheader("Examples : ")
st.markdown(":blue-background[Examples - 1]")
st.code("""st.write("Hello") # prints string""")
st.write("Hello")
st.markdown(":blue-background[Examples - 2]")
st.code("st.write(123) # prints integer")
st.write(123)
st.markdown(":blue-background[Examples - 3]")
st.code("st.write(123.45) # prints float value")
st.write(123.45)
st.markdown(":blue-background[Examples - 4]")
st.code("""st.write([1,2,3,4,"Hello","World"]) # prints list""")
st.write([1,2,3,4,"Hello","World"])
st.markdown(":blue-background[Examples - 5]")
st.code("""st.write({
                "key":"value",
                "age":34,
                "name":23,
            }) # prints dictionary""")
st.write({
    "key":"value",
    "age":34,
    "name":23,
})

st.divider()

st.subheader(":green-background[st.markdown] in more brief : ")
st.write("This function is important for adding css based elements into the text.")
st.write(":grey-background[NOTE] : All markdown based styling works with ':green[st.write]' as well.")
st.subheader("Examples : ")
st.write(":blue-background[1. Italic]")
st.code("""st.write("*Italic*")""")
st.write("*Italic*")
st.write(":blue-background[2. Bold]")
st.code("""st.write("**Bold**")""")
st.write("**Bold**")
st.write(":blue-background[3. Bold + Italic]")
st.code("""st.write("***Bold + Italic***")""")
st.write("***Bold + Italic***")
st.write(":blue-background[4. Text Color]")
st.code("""st.write(":red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors]")""")
st.write(":red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors]")
st.write(":blue-background[5. Text Highlight (Color) ]")
st.code("""st.write(":blue-background[highlight]")""")
st.write(" :orange-background[highlight], :green-background[highlight],:red-background[highlight],:violet-background[highlight],:grey-background[highlight]")
st.write(":blue-background[6. Emoji ]")
st.code("""st.write(":tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")""")
st.write(":tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.write(":blue-background[7. Dynamic markup]")
st.code("""md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f''' 
import streamlit as st

st.markdown("{md}") 
''')

st.write(md)
        """)

st.write("#### Implementation : ")
md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:",key="markdown")


st.code(f""" import streamlit as st
st.markdown('''{md}''')""")
st.write(md)

st.divider()
st.write(":blue-background[7. Markup sizes with '#' ]")
st.write("1. : Header size (H1)")
st.code("""st.write("# Hi ")""")
st.write("# Hi ")
st.divider()
st.write("2. : Subheader size (H2)")
st.code("""st.write("## Hi ")""")
st.write("## Hi ")
st.divider()
st.write("3. : (H3)")
st.code("""st.write("### Hi ")""")
st.write("### Hi ")
st.divider()
st.write("4. : (H4)")
st.code("""st.write("#### Hi ")""")
st.write("##### Hi ")
st.divider()
st.write("5. : (H5) ")
st.code("""st.write("##### Hi ")""")
st.write("##### Hi ")
st.divider()
st.write("6. : Simple write size (H6) ")
st.code("""st.write("###### Hi ")""")
st.write("###### Hi ")



st.divider()
st.subheader("Help :")
col1_foot,col2_foot = st.columns([3,1])
with col1_foot:
        st.page_link("Help.py",label = "Click Here")
with col2_foot:
        st.page_link("2_2 Visual Element.py",label = ":green-background[Next page >]")
st.divider()
