import PySimpleGUI as sg

layout = [
          [sg.Text("Wie heißt Du?")],
          [sg.Input(key = "-INPUT-")],
          [sg.Text(size = (40, 1), key = "-OUTPUT-")],
          [sg.Button("Okay"), sg.Button("Quit")]
]

window = sg.Window("Hallo PySimpleGUI", layout)

keep_going = True
while keep_going:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Quit":
        keep_going = False
    
    window["-OUTPUT-"].update("Hallöchen " + values["-INPUT-"] + "!")

window.close()