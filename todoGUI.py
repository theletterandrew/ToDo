from item import Item
from todoList import ToDoList

import PySimpleGUI as sg

tdl = ToDoList()

# todo_frame = [[sg.Text('Pick Up meds', size=(50,1)), sg.Button('Delete', button_color='red')]]

# todo_frame_2 = [[sg.Text('Call wife', size=(50,1)), sg.Button('Delete',button_color='red')]]

# todo_frame_3 = [[sg.Text('Mow the lawn', size=(50,1)), sg.Button('Delete',button_color='red')]]

new_todo_label = sg.Text(text="New Todo")

todo_text = sg.Input(key='-NEW-')

new_button = sg.Button("Create")

# layout = [[sg.Frame(title='', layout= todo_frame)],
# [sg.Frame(title='', layout=todo_frame_2)],
# [sg.Frame(title='', layout=todo_frame_3)],
# [new_todo_label, todo_text, sg.Push(), new_button]]

layout = [[new_todo_label, todo_text, sg.Push(), new_button]]

window = sg.Window('TooDoo', layout)

def item_row(text):
    todo_frame = [[sg.Text(text, size=(50,1)), sg.Button('Delete', button_color='red')]]
    row = [sg.Frame(title='', layout=todo_frame)]
    return row


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Create":
        tdl.add_item(Item(values['-NEW-']))
        tdl.print_items()

window.close()
