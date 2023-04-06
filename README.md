# Commands to execute in main

## BRESENHAM 1

```
line = bresenham.Bresenham((15, -3), (-15, -15))
screen.Draw(line.output_points, blue)
```

## BRESENHAM 2

```
line = bresenham.Bresenham((8, 7), (-15, 10))
screen.Draw(line.output_points, blue)
```

## BRESENHAM 3

```
line = bresenham.Bresenham((5, -2), (5, 10))
screen.Draw(line.output_points, blue)
```

## POLYLINE

```
points = [(3, 4), (-7, 1), (2, -9)]
lines = polilinha.Polyline(points)
screen.Draw(lines.output_points, blue)
```

## CURVES 1

```
c = curves.Curves(15, [(0, 0), (5, 5),(10,20), (20, 0)])
screen.Draw(c.output_points, blue)
```

## CURVES 2

```
c = curves.Curves(3, [(-4, 20), (0, -20), (20, 0)])
screen.Draw(c.output_points, blue)
```

## CURVES 3

```
c = curves.Curves(10, [(-14, 20), (-20, 10), (0, 0), (-8, -10)])
screen.Draw(c.output_points, blue)
```

## CIRCLE 1

```
object = circulo.Circle({
"center": [6,3],
"radius": 10
})
screen.Draw(object.output_points, blue)
```

## CIRCLE 2

```
object = circulo.Circle({
"center": [0,0],
"radius": 5
})

screen.Draw(object.output_points, blue)
```

## CIRCLE 3

```
object = circulo.Circle({
"center": [11,-7],
"radius": 7
})

screen.Draw(object.output_points, blue)
```

## RECURSIVE FILLING 1

```
points = [(3, 4), (-7, 1), (2, -9)]

object = polilinha.Polyline(points, close=True)
screen.Draw(object.output_points, blue)

pr = recursive_filling.RecursiveFilling((0,0), green, blue, screen)

```

## RECURSIVE FILLING 2

```
points = [(3, 4), (3, -2), (-5, -2), (-5, 4)]

object = polilinha.Polyline(points, close=True)
screen.Draw(object.output_points, blue)

pr = recursive_filling.RecursiveFilling((2,2), green, blue, screen)
```

##  SCANLINE 1

```
points = [(-4, 0), (8,-16), (20, 5)]

object = varredura.Scanline(points)
screen.Draw(object.output_points, blue)

## SCANLINE 2
points = [(-6,-6), (8,-4), (8,12), (0,8), (-8,14)]

object = varredura.Scanline(points)
screen.Draw(object.output_points, blue)

object = polilinha.Polyline(points, close=True)
screen.Draw(object.output_points, red)
```

## LINE CLIPPING 1

```
p1, p2 = (-7,-5),(15, 14)
xmin = -10
xmax = 2
ymin = -15
ymax = 1
object = line_clipping.LineClipping(p1, p2, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)

screen.Draw(object.output_points, blue)

```

## LINE CLIPPING 2

```
p1, p2 = (-7,9),(1, 1)
xmin = -10
xmax = 2
ymin = -5
ymax = 10
object = line_clipping.LineClipping(p1, p2, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)

screen.Draw(object.output_points, blue)
```

## LINE CLIPPING 3

```
p1, p2 = (-7,-6),(1, -8)
xmin = -10
xmax = 2
ymin = -5
ymax = 10
object = line_clipping.LineClipping(p1, p2, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)

screen.Draw(object.output_points, blue)
```

## POLYGON TRUNCATION 1

```
points = [(-5,20),(-3, -1),(5, -2)]
xmin = -1
xmax = 10
ymin = -9
ymax = 9

object = recorte_poligono.PolygonTruncation(points, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)
screen.Draw(object.output_points, blue)

#original_polygon = polilinha.Polyline(points, close=True)
#screen.Draw(original_polygon.output_points, blue)

```


## POLYGON TRUNCATION 2

```
points = [(-5,5),(-5, -5),(5, -5), (5, 5)]
xmin = -1
xmax = 10
ymin = -9
ymax = 9

object = recorte_poligono.PolygonTruncation(points, xmin, xmax, ymin, ymax)
screen.outlineWindow(xmin, xmax, ymin, ymax)
screen.Draw(object.output_points, blue)

#original_polygon = polilinha.Polyline(points, close=True)
#screen.Draw(original_polygon.output_points, blue)
```


##  TRANSFORMATION 1

```
square = [
    [0,0], [1,0], [2,0], [3,0],
    [3,1], [3,2], [3,3], [2,3],
    [1,3], [0,3], [0,2], [0,1]
]

object = transformation.Transformation(input_points=square)
object.translate(5,5)
object.scale(6, 6)
object.rotate([3, 3], 90)

screen.Draw(object.output_points, blue)
```

##  TRANSFORMATION 2

```
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
```

##  PROJECTION

```
cube = [
    [0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0],
    [0, 0, 4], [4, 0, 4], [4, 4, 4], [0, 4, 4]
]

#object = projection.Projection(input_points=cube, shift=-10)
#object.project()
#object.perspective(dist=-30)

screen.Draw(object.output_points, blue)
```
