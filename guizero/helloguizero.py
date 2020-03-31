from guizero import App, Text, PushButton

def say_hello():
    text.value = "Willkommen, Jörg, in GUI Zeros Welt."

app = App(title = "Hällo Wörld!", bg = (235, 215, 182), height = 320, width = 480)
text = Text(app)
text.size = 24
button = PushButton(app, command = say_hello)

app.display()