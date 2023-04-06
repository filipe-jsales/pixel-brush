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

square = [
    [5, 5], [6, 5], [7, 5], [8, 5],
    [8, 6], [8, 7], [8, 8], [7, 8],
    [6, 8], [5, 8], [5, 7], [5, 6]
]

object = transformation.Transformation(input_points=square)
#object.translate(5,5)
#object.scale(1, 3)
#object.rotate([5, 5], 45)

screen.Draw(object.output_points, blue)


# break execution and show screen figure
mainloop()
