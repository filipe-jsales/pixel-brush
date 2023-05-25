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

points = [(3, 4), (3, -2), (-5, -2), (-5, 4)]

object = polyline.Polyline(points, close=True)
screen.Draw(object.output_points, blue)

pr = flood_fill.FloodFill((2,2), green, blue, screen)


# break execution and show screen figure
mainloop()
