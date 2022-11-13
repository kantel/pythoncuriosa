import PySimpleGUI as sg

layout = [
          [sg.Text("Hallo von PySimpleGUI")],
          [sg.Button("Quit")]
]

window = sg.Window("Hallo PySimpleGUI", layout, font = ("Menlo", 18))

keep_going = True
while keep_going:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Quit":
        keep_going = False

window.close()