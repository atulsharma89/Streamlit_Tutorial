'''
Day 2: User Input Widgets - Mastering Interaction

Goal: Gain mastery over Streamlit's input widgets and learn how to create dynamic interfaces.
Topics:
Deep dive into each input widget:
st.button():  Using callbacks for more complex actions.
st.checkbox():  Conditional display of elements.
st.radio():  Controlling different sections of the app.
st.selectbox():  Dynamically updating options based on other inputs.
st.multiselect():  Filtering data based on multiple selections.
st.slider():  Setting ranges and steps.
st.text_input():  Validating input, regular expressions.
st.number_input():  Handling different number types (integers, floats).
st.date_input() and st.time_input():  Working with dates and times.
st.text_area():  For larger text input.
st.color_picker():  For selecting colors.

Form handling with st.form:  Ensuring consistent input and preventing re-runs until submission.

Activities:
Build a "Configuration Panel" app:
Use a st.form to group several input widgets: text input, number input, selectbox, slider, checkbox.
Display the values of all the inputs after the form is submitted.
Implement validation for the text input (e.g., check if it's a valid email address).

Create a simple calculator app using buttons and text inputs.
Use st.button to create buttons for addition, subtraction, multiplication, and division.
Use st.text_input to get the two numbers from the user.
Use st.write to display the result of the calculation.

Build a "To-Do List" app:
Use st.text_input to get the task from the user.
Use st.checkbox to mark the task as completed or not.
Use st.button to add the task to the list.
Display the list of tasks in a table format.
'''
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")



#Using st.button in Streamlit is straightforward. The function takes one required argument - the label of the button, which is a string. It also accepts several optional arguments that allow you to customize the button's behavior and appearance. Let's take a look at some of these arguments:
#key: A unique identifier for the button. This is useful when you have multiple buttons and you want to distinguish between them.
#help: A string that will be displayed as a tooltip when the user hovers over the button.


if st.button('Click Me', key='my_button', help='Click this button to perform an action'):
   st.write('You clicked the button!')


st.write("Application to show the use of button function in streamilit")

def load_data(file):
    import pandas as pd
    data = pd.read_csv(file)
    st.write("### Top 5 Rows of Your Data:")
    st.dataframe(data.head(5))  # Display top 5 rows as a DataFrame
    st.success("Data loaded and displayed successfully!")

    #return data

st.title("Streamlit Button")
st.write("""
# This is a simple app showcasing the use of button function in streamlit
""")

file = st.file_uploader("Upload a CSV file", type="csv")
if file is not None:
    data = load_data(file)
    st.write(data)






# checkbox

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
else:
    st.write("Please agree to continue.")



# radio

st.write("""
# Radio Button
""")
option = st.radio("What is your favorite programming language?", ("Python", "JavaScript", "R"))
st.write("You selected:", option)  # Display the selected option



# selectbox

st.write("""
# Select Box
""")
option = st.selectbox("What is your favorite programming language?", ("Python", "JavaScript", "R"))
st.write("You selected:", option)  # Display the selected option

#MULTISELECTBOX

st.write("""
# Multi Select Box
""")
option = st.multiselect("What are your favorite programming languages?", ("Python", "JavaScript", "R"))
st.write("You selected:", option)  # Display the selected option

#slider

st.write("""
# Slider
""")
option = st.slider("What is your favorite number?", 0, 10)
st.write("You selected:", option)  # Display the selected option

#text input

st.write("""
# Text Input
""")
option = st.text_input("What is your favorite number?", "Type here...")
st.write("You selected:", option)  # Display the selected option

# NUMBER INPUT

st.write("""
# Number Input
""")
option = st.number_input("What is your favorite number?", 0, 100)
st.write("You selected:", option)  # Display the selected option


#DATE INPUT

import datetime
st.write("""
# Date Input
""")
option = st.date_input("What is your favorite number?", datetime.date(2020, 1, 1))
st.write("You selected:", option)  # Display the selected option

#TIME INPUT

st.write("""
# Time Input
""")
option = st.time_input("What is your favorite number?", datetime.time(12, 0))
st.write("You selected:", option)  # Display the selected option

# text area

st.write("""
# Text Area
""")
option = st.text_area("What is your favorite number?", "Type here...")
st.write("You selected:", option)  # Display the selected option

#color picker

st.write("""
# Color Picker
""")
option = st.color_picker("What is your favorite number?", "#000000")
st.write("You selected:", option)  # Display the selected option


#Form handling with st.form:  Ensuring consistent input and preventing re-runs until submission.

st.write("""
# Form handling with st.form:  Ensuring consistent input and preventing re-runs until submission.
""")

def get_input():
    age = st.number_input("What is your age?", 0, 100)
    income = st.number_input("What is your income?", 0, 1000000)
    return age, income 

age, income = get_input()
if st.button("Submit"):
    st.write("You are", age, "years old and earn", income, "per year.")