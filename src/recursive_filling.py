from src.rasterization import Rasterization
from src.screen import Screen

# recursive filling


class RecursiveFilling(Rasterization):
    def __init__(self, point, color, edge_color, screen: Screen):
        super().__init__([point, color, screen])
        self.screen = screen
        self.color = color
        self.edge_color = edge_color

        self.recursion(point)

    def recursion(self, point):
        current_point = point
        print(current_point)
        current_color = self.screen.checkMatrix(
            current_point[0], current_point[1])
        print(current_color)

        if current_color != self.color and current_color != self.edge_color:
            self.screen.DrawPixel(
                current_point[0], current_point[1], self.color)

            self.recursion((current_point[0] + 1, current_point[1]))
            self.recursion((current_point[0], current_point[1] + 1))
            self.recursion((current_point[0] - 1, current_point[1]))
            self.recursion((current_point[0], current_point[1] - 1))
