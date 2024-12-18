import PySimpleGUI as sg

todo_frame = [[sg.Text('Pick Up meds', size=(50,1)), sg.Button('Delete', button_color='red')]]

todo_frame_2 = [[sg.Text('Call wife', size=(50,1)), sg.Button('Delete',button_color='red')]]

todo_frame_3 = [[sg.Text('Mow the lawn', size=(50,1)), sg.Button('Delete',button_color='red')]]

new_todo_label = sg.Text(text="New Todo")

todo_text = sg.Input(key='-NEW-')

new_button = sg.Button("Create")

layout = [[sg.Frame(title='', layout= todo_frame)],
[sg.Frame(title='', layout=todo_frame_2)],
[sg.Frame(title='', layout=todo_frame_3)],
[new_todo_label, todo_text, sg.Push(), new_button]]

window = sg.Window('TooDoo', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Create":
        sg.popup('Done')

window.close()
