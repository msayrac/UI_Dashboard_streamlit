import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Streamlit Demos")
st.write("Welcome to the streamlit demos app!")

st.header("Interactivity with widgets")
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")
age = st.number_input("Enter your age",min_value=0, max_value=120, value=18)
st.write(f"Your age is {age}")

st.write(f"You are {age} years ols")

slider = st.slider("Select your slider level", min_value=1, max_value=10, value = 5)
st.write(f"Slider, {slider}")

if st.button("Say Hello!"):
    st.write("Hello Youtube!")

option = st.selectbox("Choose an option", [1,2,3])
st.write(f"Your option is {option}")

st.header("Displaying Data and Charts")

data = {
    "Name": ["Alice","Bob","Charlie"],
    "Age": [25,30,35]
}

df = pd.DataFrame(data)
st.subheader("Sample DataFrame")
st.write(df)

st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()

x = np.linspace(0,10,100)
ax.plot(x, np.sin(x))
st.pyplot(fig)

st.subheader("Columns Layout")
col1, col2 = st.columns(2)

with col1:
    st.write("Content for col1")
with col2:
    st.write("Content for col2")

st.subheader("Tab layout")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content for tab1")
    fig, ax = plt.subplots()

    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x))
    st.pyplot(fig)
with tab2:
    st.write("Content for tab2")


st.sidebar.title("Sidebar Title")

sidebar_option = st.sidebar.selectbox("Select an option", ["A","B","C"])
st.sidebar.write(f"You selected : {sidebar_option}")













