from tkinter import mainloop

from src import (screen, bresenham, circle, scanline, polyline,
                 transformation, recursive_filling, curves, line_clipping, polygon_truncation, projection)

# some colors
blue = '#0080ff'
red = '#ff0000'
green = '#00ff40'
purple = '#bf00ff'
yellow = '#ffff00'

# create screen
screen = screen.Screen(600)


# EXAMPLES HERE

line = bresenham.Bresenham((15, -3), (-15, -15))
screen.Draw(line.output_points, blue)


# break execution and show screen figure
mainloop()
