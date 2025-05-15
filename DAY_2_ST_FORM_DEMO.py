import streamlit as st

with st.form("my_form"):
    st.header("Input Form")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
    occupation = st.selectbox("Choose your occupation:", ["Student", "Engineer", "Doctor", "Teacher", "Other"])
    experience = st.slider("Years of experience:", min_value=0, max_value=20, value=5)
    agreement = st.checkbox("I agree to the terms and conditions")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not agreement:
            st.error("You must agree to the terms and conditions to submit.")
        else:
            st.success("Form submitted successfully!")
            st.write(f"Name: {name}")
            st.write(f"Age: {age}")
            st.write(f"Occupation: {occupation}")
            st.write(f"Experience: {experience} years")
