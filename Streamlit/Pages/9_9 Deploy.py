import streamlit as st

st.header("9.Deploy : ")

st.write("#### 1. Creating git repository : ")
st.caption("• Login to github, and click 'New Repository'")

st.image("Streamlit/static/github_repo.png")
st.divider()
st.caption("• Provide repo name, toggle public/private and twitch other parameters.")
st.image("Streamlit/static/ghub_new_repo.png")
st.divider()
st.caption("• Create repo")
st.image("Streamlit/static/create_repo.png")
st.divider()
st.write("### 2. Upload streamlit project folder in github.")
st.write("##### (Make sure the file are structured for example : ")
st.image("Streamlit/static/directory.png")
st.divider()
st.image("Streamlit/static/upload_ghub.png")
st.divider()
st.image("Streamlit/static/git_repo_base.png")
st.divider()
st.write("#### 3. Streamlit Cloud Setup")
st.caption("Click on to link given below and sign-in to the Streamlit Cloud.")
st.caption("It would also ask to use and edit github repository authorization, click ok and login to GitHub from the prompt")
st.page_link("https://streamlit.io/cloud", label=":green-background[Streamlit Cloud link]", help="Click me to open streamlit cloud")
st.write("#### Steamlit's interface would look like this after login/signup")
st.write("• Click create app to continue.")
st.image("Streamlit/static/st_createapp.png")
st.write("• Choose GitHub & continue.")
st.image("Streamlit/static/st_createapp_menu.png")
st.write("• New App Form would look like this : ")
st.image("Streamlit/static/st_createapp_form.png")
st.write("Basic Breakdown of Form :")
st.write("• Select your repository from the following list : ")
st.image("Streamlit/static/st_createapp_form_repo.png")
st.write("• Let the branch be :blue-background[Default] ")
st.write("• Select your main filepath")
st.caption("(This file would be your main file / startup file incase of multi-page structure) ")
st.image("Streamlit/static/st_createapp_form_filepath.png")
st.write("• Choose any name as App's URL & Hit Deploy")
st.image("Streamlit/static/st_createapp_form_url.png")
st.write("• It would take some time in processing wait for few minutes.")
st.success("Yay! Our first streamlit file hosted sucessfully.")
st.image("Streamlit/static/st_createapp_sucess.png")
st.divider()
st.write("""#### You can share your "Python Based Web App" with other.""")
st.write("• Click share and copy the link.")
st.image("Streamlit/static/st_createapp_share.png")

st.divider()
st.subheader("Help :")
st.page_link("Help.py",label = "Click Here")
st.divider()

