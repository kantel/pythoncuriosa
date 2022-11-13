from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import numpy as np

fig = Figure(figsize = (6, 4), facecolor = "white")
axis = fig.add_subplot(111)

x = np.linspace(-10, 10, 1000)

axis.plot(x, np.sin(x), "-r", label = "Sinus")
axis.plot(x, np.cos(x), "--g", label = "Cosinus")

axis.set_xticks([-10, 0, 10])
axis.set_yticks([-1, 0, 1])
axis.set_ylim(-2, 2)
axis.set_xlabel("Sinus- und Cosinus-Kurve")

axis.legend()
axis.grid()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill = "both", expand = 1)
    return figure_canvas_agg

layout = [
          [sg.Text("Sinus vs. Cosinus")],
          [sg.Canvas(key = "-CANVAS-")],
          [sg.Button("Quit")]
]

window = sg.Window("PySimpleGUI Plot-Test",
                   layout,
                   element_justification = "center",
                   font = ("Menlo", 14),
                   finalize = True,
)

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)

event, values = window.read()
window.close()