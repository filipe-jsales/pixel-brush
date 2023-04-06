from src.rasterization import Rasterization
from src.polyline import Polyline
from src.bresenham import Bresenham
import numpy as np


class Projection(Rasterization):
    def __init__(self, input_points, shift):
        for coordinate in input_points:
            coordinate[2] += shift
        super().__init__(input_points)

    def project(self):
        for point in self.input_points:
            point.append(1)

        matrix_projection = [[0 for i in range(
            len(self.input_points[0]))] for i in range(len(self.input_points[0]))]

        missed_diagonal = 2
        x_output = 0
        y_output = 1

        for i in range(0, len(self.input_points[0])):
            if i != missed_diagonal:
                matrix_projection[i][i] = 1

        for point in self.input_points:
            projection = np.dot(matrix_projection, point)
            self.output_points.append(
                [projection[x_output], projection[y_output]])

        self.output_points = Polyline(
            self.output_points, close=True).output_points

    def perspective(self, dist):
        for point in self.input_points:
            point.append(1)

        matrix_perspective = [[0 for i in range(
            len(self.input_points[0]))] for i in range(len(self.input_points[0]))]

        for i in range(0, len(self.input_points[0])):
            if i != len(self.input_points[0])-1:
                matrix_perspective[i][i] = dist

        matrix_perspective[len(matrix_perspective) -
                           1][len(matrix_perspective)-2] = 1

        for point in self.input_points:
            projection = np.dot(matrix_perspective, point)
            projection = np.multiply(projection, 1/point[2])
            self.output_points.append(
                [round(projection[0]), round(projection[1])])

        self.output_points = Polyline(
            self.output_points, close=True).output_points

        uniques = []

        for point in self.output_points:
            if point[0] == point[1]:
                if [point[0], point[1]] not in uniques:
                    uniques.append([point[0], point[1]])

        uniques.pop(0)

        self.output_points += Bresenham(uniques[0], uniques[1]).output_points
