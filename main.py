from tkinter import mainloop

from src import (screen, bresenham, circle, scanline)

# some colors
blue = '#0080ff'
red = '#ff0000'
green = '#00ff40'
purple = '#bf00ff'
yellow = '#ffff00'

# create screen
screen = screen.Screen(600)


# EXAMPLES HERE

obj = circle.Circle({
    "center": [0,0],
    "radius": 10
})
screen.Desenhar(obj.output_points, blue)


# break execution and show screen figure
mainloop()