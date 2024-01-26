import streamlit as st
import functions

todos = functions.get_todos()


st.title("My To-Do App")
st.subheader("This is my todoapp")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do", placeholder="Add the new To-Do")

