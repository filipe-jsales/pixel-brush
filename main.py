from tkinter import mainloop

from src import (screen, bresenham, circle, scanline, polyline,
                 transformation, flood_fill, curves, line_clipping, polygon_truncation, projection)

# some colors
blue = '#0080ff'
red = '#ff0000'
green = '#00ff40'
purple = '#bf00ff'
yellow = '#ffff00'

# create screen
screen = screen.Screen(600)


# EXAMPLES HERE

p1, p2 = (-7,9),(1, 1)
xmin = -10
xmax = 2
ymin = -5
ymax = 10
object = line_clipping.LineClipping(p1, p2, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)

screen.Draw(object.output_points, blue)


# break execution and show screen figure
mainloop()
