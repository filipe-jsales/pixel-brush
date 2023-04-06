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

cubo = [
    [0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0],
    [0, 0, 4], [4, 0, 4], [4, 4, 4], [0, 4, 4]
]

object = projection.Projection(input_points=cubo, shift=-10)
object.project()

object.perspective(dist=-9)

screen.Draw(object.output_points, blue)


# break execution and show screen figure
mainloop()
