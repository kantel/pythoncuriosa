from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with title and axis labels
p = figure(title = "Einfache Linie", x_axis_label = "x", y_axis_label = "y")

# add a line renderer with legend and line thickness
p.line(x, y, legend_label = "Temperatur", line_width = 2)

show(p)