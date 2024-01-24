import functions
import PySimpleGUI as sg  # replace PySimpleGUI with sg
import time

sg.theme("Reddit")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")  # creates text on window
input_box = sg.InputText(tooltip="Enter To-DO", key="todo")
# as the input comes in dictionary form we added key so that
# its easier to take its value to add it in to the todo
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[55, 20])
edit_button = sg.Button("Edit", size=10)

complete_button = sg.Button("Complete", size=10)

exit_button = sg.Button("Exit", size=10)
# getting the list from todos.txt
Layout = [[clock],
          [[label],
          [input_box, add_button]],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do app',
                   layout=Layout,
                   font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=200)  # displays the window on the screen

    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

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
            try:
                todo_to_edit = values['todos'][0]  # to get the actual string
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                # to get the updated list in real time
            except IndexError:
                sg.Popup("Please select a To- Do !", font=10)

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select a To-Do to mark as complete !", font=8)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Exit':
            break


window.close()  # closes the window
