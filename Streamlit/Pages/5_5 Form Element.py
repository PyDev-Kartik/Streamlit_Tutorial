import streamlit as st
import pandas as pd
from datetime import datetime

st.header("5. Form Elements : ")

st.write("0. Form initialization :")

st.code("""# Sample example:
with st.form(key="user info"):  # it would provide the space to bind all functions related to forms
     name = st.text_input("Enter your name : ")  # Example input 
     st.form_submit_button() # This is mandatory --> Submission of form.""")   

with st.form(key="user info"):
    name = st.text_input("Enter your name : ")
    st.form_submit_button()

st.divider()

st.write("1. Text input :")
st.code("""with st.form(key="user text info"):
    name = st.text_input("Enter your name : ")
    boolean = st.text_input("Type any boolean value : (Max length : 4) ",max_chars=4)
    password = st.text_input("Enter password : ",type="password")
    address = st.text_area("Enter your address : ")
    surname = st.text_input("Enter your surname",help="surname is your last name",placeholder="surname")
    st.form_submit_button()""")
with st.form(key="user text info"):
    name = st.text_input("Enter your name : [Simple text input]")
    boolean = st.text_input("Type any boolean value : (Max length : 4) [Simple text with max length] ",max_chars=4)
    password = st.text_input("Enter password : [text input as password]",type="password")
    address = st.text_area("Enter your address : [text input as address]")
    surname = st.text_input("Enter your surname : [with placeholder and help]",help="surname is your last name",placeholder="surname")
    st.form_submit_button()

st.divider()

st.write("2. Number Input :")
st.code("""
with st.form(key="user number info"):
    no = st.number_input("Enter any no : ")
    no2 = st.number_input("Enter no2 : (in range 2-10) ",min_value=2,max_value=10)
    no3 = st.number_input("Enter no3 : ",help="This '+' key would increment step value (3) to the current no.",step=3)
    st.form_submit_button()""")

with st.form(key="user number info"):
    no = st.number_input("Enter any no : [Simple no]")
    no2 = st.number_input("Enter no2 : (in range 2-10) [Simple no with range] ",min_value=2,max_value=10)
    no3 = st.number_input("Enter no3 : [with step value of 3].Refer help section for more info :)",help="This '+' key would increment step value (3) to the current no.",step=3)
    st.form_submit_button()

st.divider()

st.write("3. Date input & Time input:")

min_date = datetime(1990,1,1)
max_date = datetime.now()

st.code("""# To add more functionality to date input no.2 like max and min value we would initialize modules as
from datetime import datetime
min_date = datetime(1990,1,1)
max_date = datetime.now()

with st.form(key="user date info"):
    date = st.date_input("Enter any date : ") # simple date        
    
    # Date with max min value, and format : 
    date2 = st.date_input("Enter any date2 : ",format="DD-MM-YYYY",min_value=min_date,max_value=max_date)
    st.form_submit_button()        
        """)

with st.form(key="user date info"):
    date = st.date_input("Enter any date : ")        
    date2 = st.date_input("Enter any date2 : ",format="DD-MM-YYYY",min_value=min_date,max_value=max_date)
    st.form_submit_button()

st.code("""
# Time input : 
with st.form(key="user time info"):
    date = st.time_input("Enter time : ")        
    st.form_submit_button()       
        """)

with st.form(key="user time info"):
    date = st.time_input("Enter time : ")        
    st.form_submit_button()

st.divider()

st.write("4. Selectbox Input :")

cities = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad",
"Ahmedabad", "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur",
    "Nagpur", "Visakhapatnam", "Indore", "Thane", "Bhopal", "Coimbatore",
    "Patna", "Vadodara", "Agra", "Madurai", "Nashik", "Faridabad",
    "Ludhiana", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad",
    "Amritsar", "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Jabalpur",
    "Gwalior", "Vijayawada", "Mysore", "Kalyan", "Bhiwandi", "Tiruchirappalli",
    "Salem", "Nanded", "Bhubaneswar", "Dehradun", "Kota", "Raipur",
    "Jodhpur", "Gurgaon", "Mangalore", "Bhopal", "Siliguri", "Agartala",
    "Durgapur", "Jamshedpur", "Warangal", "Sangli", "Udaipur", "Kochi",
    "Kozhikode", "Vellore", "Rourkela", "Guwahati", "Bardhaman", "Bilaspur",
    "Davanagere", "Kakinada", "Kurnool", "Shimla", "Imphal", "Itanagar",
    "Gangtok", "Aizawl", "Dispur", "Panaji", "Port Blair", "Dibrugarh",
    "Tirupati", "Thiruvananthapuram", "Jammu", "Srinagar", "Kargil", "Leh",
    "Belgaum", "Tumkur", "Kolar", "Hampi", "Bijapur", "Bagalkot",
    "Chandigarh", "Mohali", "Panchkula", "Ambala", "Kurukshetra", "Sonipat",
    "Panipat", "Rohtak", "Hisar", "Bhiwani", "Fatehabad", "Sirsa",
    "Nuh", "Mahendragarh", "Jhajjar", "Rewari", "Gurgaon", "Faridabad",
    "Sonipat", "Ambala", "Karnal", "Yamunanagar", "Kurukshetra", "Panchkula",
    "Mandi", "Kullu", "Solan", "Bilaspur", "Hamirpur", "Una",
    "Chamba", "Kinnaur", "Lahaul", "Spiti", "Dharamshala", "Palampur",
    "Nahan", "Rampur", "Sirmaur", "Shimla", "Kinnaur", "Chamba",
    "Mandi", "Dharamshala", "Solan", "Kullu", "Hamirpur", "Una",
    "Rudrapur", "Haldwani", "Nainital", "Kashipur", "Ramnagar", "Khatima",
    "Pithoragarh", "Champawat", "Almora", "Bageshwar", "Tehri", "Uttarkashi",
    "Haridwar", "Rishikesh", "Dehradun", "Roorkee", "Srinagar", "Pauri",
    "Kotdwar", "Lansdowne", "Bhagwanpur", "Rudraprayag", "Chamoli", "Nainital",
    "Bageshwar", "Pithoragarh", "Champawat", "Almora", "Tehri", "Uttarkashi",
    "Haridwar", "Rishikesh", "Dehradun", "Roorkee", "Srinagar", "Pauri",
    "Kotdwar", "Lansdowne", "Bhagwanpur", "Rudraprayag", "Chamoli"]

cities_df = pd.DataFrame({"cities":cities,
                          "space":[" " for i in cities]})



st.code("""
with st.form(key="user selection info"):
    opt = st.selectbox("Choice 1 [simple choice]",options=["Male","Female"])
    opt2 = st.selectbox("Choice 2 [placeholder]",["Male", "Female"],index=None, placeholder="Select Gender",)
    # Complex option: (we can make it function as auto sugggest:)
    # initialise the cities list and link it to the options.
    # Cities = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad",...]
    opt3 = st.selectbox("Choice 3 Enter City [Now this would work as auto suggest]",cities,index=None, placeholder="Select Your City",)
    
    # A new type of selection input with slider : 
    opt4 = st.select_slider("Choice 4 Rating : [slider input]",["0 Worst","1","2","3","4","5","6","7","8","9","10 Best"])    
    st.form_submit_button()""")

st.text("Indian Cities List : [initialise list based on this data]")
st.dataframe(cities_df)

with st.form(key="user selection info"):
    opt = st.selectbox("Choice 1 [simple choice]",options=["Male","Female"])
    opt2 = st.selectbox("Choice 2 [placeholder]",["Male", "Female"],index=None, placeholder="Select Gender",)
    opt3 = st.selectbox("Choice 4 Enter City [Now this would work as auto suggest]",cities_df["cities"],index=None, placeholder="Select Your City",)
    opt4 = st.select_slider("Choice 4 Rating : [slider input]",["0 Worst","1","2","3","4","5","6","7","8","9","10 Best"])
    st.form_submit_button()


st.divider()

st.subheader("Sample form Template : (with all functionalities : )")
st.code("""
CODE : 

form_values ={
    "name":None,
    "age":None,
    "height":None,
    "gender":None,
    "dob":None,
    "address":None,
    "city":None
}
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your Name : ",placeholder="Name")
    form_values["age"] = st.number_input("Enter Age : ")
    form_values["height"] = st.number_input("Enter Height : ",min_value=5.0,max_value=6.5)
    form_values["gender"] = st.selectbox("Gender :",["Male","Female"],index=None,placeholder="Select Gender")
    form_values["dob"] = st.date_input("Enter Date of birth : ",format="DD/MM/YYYY",min_value=min_date,max_value=max_date)
    form_values["address"] = st.text_area("Enter your Address : ",placeholder="Address")
    form_values["city"] = st.selectbox("Enter your City : ",cities_df["cities"],index=None, placeholder="Select Your City")

    #st.form_submit_button()
    submit = st.form_submit_button()
    if submit:
        if not all(form_values.values()):
            st.warning("Please fill all of the fields.")
        else:
            st.balloons()
            st.write("#### INFO : ")
            for key,value in form_values.items():
                st.write(f"{key}: {value}")
""")
form_values ={
    "name":None,
    "age":None,
    "height":None,
    "gender":None,
    "dob":None,
    "address":None,
    "city":None
}
st.write("Try to submit this form : ")
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your Name : ",placeholder="Name",help="Enter your Full name")
    form_values["age"] = st.number_input("Enter Age : ",help="Enter your current age")
    form_values["height"] = st.number_input("Enter Height : ",min_value=5.0,max_value=6.5,help="Enter your current height in feets")
    form_values["gender"] = st.selectbox("Gender :",["Male","Female"],index=None,placeholder="Select Gender",help="Enter your gender")
    form_values["dob"] = st.date_input("Enter Date of birth : ",format="DD/MM/YYYY",min_value=min_date,max_value=max_date,help="Enter your Date of birth")
    form_values["address"] = st.text_area("Enter your Address : ",placeholder="Address",help="Enter your Full address")
    form_values["city"] = st.selectbox("Enter your City : ",cities_df["cities"],index=None, placeholder="Select Your City",help="Select your city")

    #st.form_submit_button()
    submit = st.form_submit_button()
    if submit:
        if not all(form_values.values()):
            st.warning("Please fill all of the fields.")
        else:
            st.balloons()
            st.write("#### INFO : ")
            for key,value in form_values.items():
                st.write(f"{key}: {value}")

st.write("code break down : ")
st.code("""
# initialized a dictionay with empty values : 
        
form_values ={
    "name":None,
    "age":None,
    "height":None,
    "gender":None,
    "dob":None,
    "address":None,
    "city":None
}
""")

st.code("""
# Setup the form :
 
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your Name : ",placeholder="Name")
    form_values["age"] = st.number_input("Enter Age : ")
    form_values["height"] = st.number_input("Enter Height : ",min_value=5.0,max_value=6.5)
    form_values["gender"] = st.selectbox("Gender :",["Male","Female"],index=None,placeholder="Select Gender")
    form_values["dob"] = st.date_input("Enter Date of birth : ",format="DD/MM/YYYY",min_value=min_date,max_value=max_date)
    form_values["address"] = st.text_area("Enter your Address : ",placeholder="Address")
    form_values["city"] = st.selectbox("Enter your City : ",cities_df["cities"],index=None, placeholder="Select Your City")

    submit = st.form_submit_button()
""")

st.code("""
# Conditing After submit processes :
        
    submit = st.form_submit_button() # Buttton to submit our form : 
    if submit: # if submit is True 
        if not all(form_values.values()):    # if any value of form_values is still none.
            st.warning("Please fill all of the fields.") # we would generate a warning.
        else:
            st.balloons()   # this is just a graphical element that displays ballons. Only Fun Element :)
            st.write("#### INFO : ")
            for key,value in form_values.items():     # we would travese our dictionary and print the data it fetched from the form. 
                st.write(f"{key}: {value}")
""")
st.divider()