from src.rasterization import Rasterization
from src.polyline import Polyline
from math import sin, cos, radians
import numpy as np


class Transformation(Rasterization):
    def __init__(self, input_points):
        super().__init__(input_points)
        self.output_points = input_points

    def translate(self, trans_x, trans_y):
        self.output_points = []
        for point in self.input_points:
            point[0] += trans_x
            point[1] += trans_y
            self.output_points.append(point)

    def scale(self, esc_x, esc_y):
        self.output_points = []
        for point in self.input_points:
            point[0] *= esc_x
            point[1] *= esc_y
            self.output_points.append(point)
        self.output_points.append(self.output_points[0])

        self.output_points = Polyline(self.output_points).output_points

    def rotate(self, pivot, angulo):
        self.output_points = []
        # de acordo com a distância pivot-origem, translate object para a origem
        trans_x = 0 - pivot[0]
        trans_y = 0 - pivot[1]
        translation = Transformation(self.input_points)
        translation.translate(trans_x, trans_y)
        self.input_points = translation.output_points

        # transformar para radianos
        radian_angle = radians(angulo)

        # montar a matriz de rotação
        rotation_matrix = [[cos(radian_angle), -sin(radian_angle)], [sin(radian_angle), cos(radian_angle)]]

        # multiplicação de matrizes entre a rotação e cada column da input_points
        for point in self.input_points:
            self.output_points.append([round(x) for x in np.dot(rotation_matrix, point)])

        # translate object back
        translation = Transformation(self.output_points)
        translation.translate(-trans_x, -trans_y)
        self.output_points = translation.output_points
