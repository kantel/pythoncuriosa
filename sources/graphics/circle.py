import graphics as g

win = g.GraphWin("Jörgs Kreis", 400, 400)
c = g.Circle(g.Point(200,200), 200)
c.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

