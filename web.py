import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo =  st.session_state['new_todo']+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do app")
st.subheader("to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

new_todo = st.text_input(label="",placeholder="Enter a todo...",on_change=add_todo,key='new_todo')
# st.session_state
