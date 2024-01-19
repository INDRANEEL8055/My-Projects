import functions
import PySimpleGUI as sg  # replace PySimpleGUI with sg

label = sg.Text("Type in a To-Do")  # creates text on window
input_box = sg.InputText(tooltip="Enter To-DO", key="todo")
# as the input comes in dictionary form we added key so that
# its easier to take its value to add it in to the todo
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

# getting the list from todos.txt

window = sg.Window('My To-Do app',
                   layout=[[[label],
                            [input_box, add_button]],
                           [list_box, edit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()  # displays the window on the screen
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()  # importing the todo from file
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case sg.WIN_CLOSED:  # TO fix error window popup after closing
            break
        case "Edit":
            todo_to_edit = values['todos'][0]  # to get the actual string
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            # to get the updated list in real time
        case 'todo':
            window['todo'].update(value=values['todo'][0])

window.close()  # closes the window
