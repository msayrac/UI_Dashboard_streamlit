import streamlit as st

st.title("Streamlit Demos")

st.write("Welcome to the streamlit demos app!")


st.header("Interactivity with widgets")

name = st.text_input("Enter your name")

st.write(f"Hello, {name}!")

age = st.number_input("Enter your age",min_value=0, max_value=120, value=18)
st.write(f"Your age is {age}")

st.write(f"You are {age} years ols")



