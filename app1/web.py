import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"  # session_state contains pari of data which user enters
    todos.append(todo1)
    functions.write_todos(todos)


st.title("My To-Do App.")
st.subheader("This is my todoapp.")
st.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a To-Do.", placeholder="Add the new To-Do.",
              on_change=add_todo, key='new_todo')



