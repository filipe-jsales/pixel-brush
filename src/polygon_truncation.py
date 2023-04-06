from src.rasterization import Rasterization
from src.polyline import *


class PolygonTruncation(Rasterization):
    def __init__(self, polygon_points: list, xmin, xmax, ymin, ymax):
        super().__init__([polygon_points, xmin, xmax, ymin, ymax])
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        left = self.sutherland_hodgman_left(polygon_points)
        up = self.sutherland_hodgman_up(left)
        right = self.sutherland_hodgman_right(up)
        down = self.sutherland_hodgman_down(right)

        new_polygon_vertices = down

        polygon = Polyline(new_polygon_vertices, close=True)
        self.output_points = polygon.output_points



    def sutherland_hodgman_left(self, pts):
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if x1 >= self.xmin:
                if x2 >= self.xmin:
                    # inside to inside 
                    new_polygon.append(list(p2))
                else:
                    # inside to outside
                    new_polygon.append([self.xmin, round(y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1))])

            else:
                if x2 >= self.xmin:
                    # outside to inside 
                    new_polygon.append([self.xmin, round(y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1))])
                    new_polygon.append(p2)
        return new_polygon

    def sutherland_hodgman_right(self, pts):
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if x1 <= self.xmax:
                if x2 <= self.xmax:
                    # inside to inside 
                    new_polygon.append(list(p2))
                else:
                    # inside to outside 
                    new_polygon.append([self.xmax, round(y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1))])

            else:
                if x2 <= self.xmax:
                    # outside to inside
                    new_polygon.append([self.xmax, round(y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1))])
                    new_polygon.append(p2)

        return new_polygon


    def sutherland_hodgman_down(self, pts):
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if y1 >= self.ymin:
                if y2 >= self.ymin:
                    # inside to inside 
                    new_polygon.append(list(p2))
                else:
                    # inside to outside 
                    new_polygon.append([round(x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)), self.ymin])

            else:
                if y2 >= self.ymin:
                    # outside to inside 
                    new_polygon.append([round(x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)), self.ymin])
                    new_polygon.append(p2)

        return new_polygon

    def sutherland_hodgman_up(self, pts):
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if y1 <= self.ymax:
                if y2 <= self.ymax:
                    # inside to inside 
                    new_polygon.append(list(p2))
                else:
                    # inside to outside 
                    new_polygon.append([round(x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)), self.ymax])

            else:
                if y2 <= self.ymax:
                    # outisde to inside
                    new_polygon.append([round(x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)), self.ymax])
                    new_polygon.append(p2)

        return new_polygon
