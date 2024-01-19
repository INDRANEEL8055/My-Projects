import functions
import PySimpleGUI as sg  # replace PySimpleGUI with sg

label = sg.Text("Type in a To-Do")  # creates text on window
input_box = sg.InputText(tooltip="Enter To-DO", key="todo")
# as the input comes in dictionary form we added key so that
# its easier to take its value to add it in to the todo
add_button = sg.Button("Add")

window = sg.Window('My To-Do app',
                   layout=[[[label], input_box, add_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()  # displays the window on the screen
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()  # importing the todo from file
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:  #  TO fix error window popup after closing
            break


window.close()  # closes the window
