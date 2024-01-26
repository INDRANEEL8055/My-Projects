import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # session_state contains pari of data which user enters
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App.")
st.subheader("This is my todoapp.")
st.write("This app is to increase productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do.", placeholder="Add the new To-Do.",
              on_change=add_todo, key='new_todo')

print('hello')


