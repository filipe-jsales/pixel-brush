from src.rasterization import Rasterization


class Circle(Rasterization):
    def __init__(self, input_points):
        super().__init__(input_points)

        self.center = self.input_points["center"]
        self.radius = round(self.input_points["radius"])

        self.middle_point()

    def middle_point(self):
        # initial parameters and first traces in octant
        x = 0
        y = self.radius
        e = -self.radius
        self.draw_octants(x, y)

        # draw in the second octant to others octants
        while x <= y:
            # adjuost the x error and increment to the right
            e = self.e_prox(x, y, e)
            x += 1

            # if is inside the circle decrements y, else keep y
            if e >= 0:
                e = self.e_fin(x, y, e)
                y -= 1

            self.draw_octants(x, y)

    def e_prox(self, x, y, e):
        return e + 2*x + 1

    def e_fin(self, x, y, e):
        return e - 2*y + 2

    def draw_octants(self, x, y):
        self.output_points.append([x + self.center[0], y + self.center[1]])
        self.output_points.append([y + self.center[0], x + self.center[1]])
        self.output_points.append([y + self.center[0], -x + self.center[1]])
        self.output_points.append([x + self.center[0], -y + self.center[1]])
        self.output_points.append([-x + self.center[0], -y + self.center[1]])
        self.output_points.append([-y + self.center[0], -x + self.center[1]])
        self.output_points.append([-y + self.center[0], x + self.center[1]])
        self.output_points.append([-x + self.center[0], y + self.center[1]])
