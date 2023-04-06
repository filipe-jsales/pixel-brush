from src.rasterization import Rasterization
from src.bresenham import Bresenham


class Polyline(Rasterization):
    def __init__(self, points:list, close=False):
        super().__init__(points)

        if close:
            points.append(points[0])
        
        for x in range(len(points)-1):
            line = Bresenham(points[x], points[x+1])
            
            for pt in line.output_points:
                self.output_points.append(pt)
            
        
        