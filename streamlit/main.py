# Streamlit tutorial
import streamlit as st

st.title("Hello programming language app")
st.subheader("Checked with Streamlit")
st.text("welcome to first interactive app with streamlit")
st.write("Choose your favorite programming language from the list below:")

language = st.selectbox("You programming languages", ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift"])
st.write(f"Your choice {language} is a great programming language!")