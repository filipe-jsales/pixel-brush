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

#BRESENHAM
# line = bresenham.Bresenham((16, -4), (-10, -10))
# screen.Draw(line.output_points, purple)

mainloop()
