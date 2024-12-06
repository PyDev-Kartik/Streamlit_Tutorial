import streamlit as st

st.header("6. Advance form : ")

st.subheader("1. Session State :")
st.caption("Session state acts as buffer where each and every variable update itself in reference to the rerun of streamlit.")
st.write("##### Understanding the issue / problem :")
st.write("""PROBLEM : As we all know in streamlit, the data keeps on updating itself at each re-run which occurs when data is entered or processed.
So sometimes a simple python variable can't handle such conditions and may cause errors.""")
st.write("##### Let's understand this with an example : ")
st.code("""
# Example
st.subheader("Exmple of Simple python variable error : ")
counter = 0 
st.write(f"The counter value is : {counter}")

if st.button("Increment Counter"):
    counter+=1
    st.write(f"Increment counter value : {counter}")
else:
    st.write(f"Counter stays at : {counter}")
""")

st.write("##### Implementation : ")
counter = 0 
st.write(f"The counter value is : {counter}")

if st.button("Increment Counter"):
    counter+=1
    st.write(f"Increment counter value : {counter}")
else:
    st.write(f"Counter stays at : {counter}")
st.write("========================================================================================")

st.write(""" We can clearly see that the counter is not incrementing, even if the code is perfect.
\n :grey-background[In this example :] each and every time the services are reloaded, hence as we have initialised counter as 0 it remains 0 in next re-run even if we increment it because ultimately it just refreshes in re-run.

\n :green[--> To overcome this issue a new idea is introduced  : :grey-background["Session state"]]
\n :green[--> Session state stores the data as a session which syncs itself with the functioning.] """)

st.write("##### Let's see the solution with 'Session state' : ")
st.code("""
st.subheader("Soution with session state :")

if "counter_new" not in st.session_state: # initialized the session state
    st.session_state.counter_new = 0         

if st.button("Increment Counter updated"): # Incrementation of code
    st.session_state.counter_new +=1

if st.button("Reset"): # Reset code
    st.session_state.counter_new = 0 

st.write(f"Counter : {st.session_state.counter_new}") #printing data""")

st.write("##### Implementation : ")


if "counter_new" not in st.session_state:
    st.session_state.counter_new = 0

if st.button("Increment Counter updated"):
    st.session_state.counter_new +=1

if st.button("Reset"):
    st.session_state.counter_new = 0 

st.write(f"Counter : {st.session_state.counter_new}")
st.write("========================================================================================")
st.write("We can see that the incrementer is now working well. So how did it solved the issue ?")
st.write("Let's see this in code breakdown : ")
st.code(""" # initialized the session state : 
if "counter_new" not in st.session_state: 
    st.session_state.counter_new = 0
        
# we checked "counter_variable" exists in st.session_state or not 
#(As we are initializing our first element so session state is basically empty).
# if not then it creates a session state varible "counter_new"
# as st.session_state.counter_new = 0 """)

st.code("""if st.button("Increment Counter updated"): # Incrementation of code
    st.session_state.counter_new +=1
        
# Now session_state.varname acts as a basic python varible 
# so we added incrementation function. Rest code is self explanatory. """)

st.divider()

