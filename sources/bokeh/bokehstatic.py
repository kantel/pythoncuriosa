from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title = "Einfache Linie", x_axis_label = "x", y_axis_label = "y")
p.line(x, y, legend_label = "Temperatur", line_width = 2)

html = file_html(p, CDN, "myplot")

show(p)