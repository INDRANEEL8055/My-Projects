import functions
import PySimpleGUI as sg  # replace PySimpleGUI with sg

label = sg.Text("Type in a To-Do")  # creates text on window
input_box = sg.InputText(tooltip="Enter To-DO")
add_button = sg.Button("Add")

window = sg.Window('My To-Do app', layout=[[[label], input_box, add_button]])
window.read()  # displays the window on the screen
window.close()  # closes the window
