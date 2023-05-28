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
# line = bresenham.Bresenham((16, -4), (-14, -14))
# screen.Draw(line.output_points, blue)

#POLILINHA
# points = [(3, 4), (-7, 1), (2, -9)]
# lines = polyline.Polyline(points)
# screen.Draw(lines.output_points, green)

#CURVAS
# c = curves.Curves(10, [(-14, 20), (-10, 20), (0, 0), (-8, -10)])
# screen.Draw(c.output_points, yellow)

#CIRCULO
# object = circle.Circle({
# "center": [0,0],
# "radius": 5
# })

#PREENCHIMENTO RECURSIVO
# points = [(3, 4), (3, -2), (-5, -2), (-5, 4)]

# object = polyline.Polyline(points, close=True)
# screen.Draw(object.output_points, blue)

# pr = flood_fill.FloodFill((2,2), green, blue, screen)

# screen.Draw(object.output_points, blue)

#SCANLINE
# points = [(-4, 0), (8,-16), (20, 5)]

# object = scanline.Scanline(points)
# screen.Draw(object.output_points, blue)

#RECORTE DE LINHA
# p1, p2 = (-7,9),(1, 1)
# xmin = -10
# xmax = 2
# ymin = -5
# ymax = 10
# object = line_clipping.LineClipping(p1, p2, xmin, xmax, ymin, ymax)
# screen.outlineWindow(xmin, xmax, ymin, ymax)

# screen.Draw(object.output_points, blue)


#RECORTE DE POLÍGONO
# points = [(-5,5),(-5, -5),(5, -5), (5, 5)]
# xmin = -1
# xmax = 10
# ymin = -9
# ymax = 9

# object = polygon_truncation.PolygonTruncation(points, xmin, xmax, ymin, ymax)
# screen.outlineWindow(xmin, xmax, ymin, ymax)
# screen.Draw(object.output_points, blue)

#original_polygon = polyline.Polyline(points, close=True)
#screen.Draw(original_polygon.output_points, blue)


#TRANSFORMAÇÕES
# square = [
#     [5, 5], [6, 5], [7, 5], [8, 5],
#     [8, 6], [8, 7], [8, 8], [7, 8],
#     [6, 8], [5, 8], [5, 7], [5, 6]
# ]

# object = transformation.Transformation(input_points=square)
#object.translate(-10,-10)
#object.scale(1, 1)
#object.rotate([5, 5], 0)

# screen.Draw(object.output_points, blue)


#PROJEÇÃO
# cube = [
#     [0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0],
#     [0, 0, 4], [4, 0, 4], [4, 4, 4], [0, 4, 4]
# ]

# object = projection.Projection(input_points=cube, shift=-10)
# object.project()
# object.perspective(dist=-30)

# screen.Draw(object.output_points, red)

mainloop()
