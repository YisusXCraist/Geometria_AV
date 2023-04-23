# Tests.py
#change

import unittest
from Vector import Vector
from Line import Line
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)
        self.line = Line([1, 2, 3], [4, 5, 6])

    def test_direction_vector(self):
        direction = self.line.direction_vector()
        self.assertEqual(direction.x, 3)
        self.assertEqual(direction.y, 3)
        self.assertEqual(direction.z, 3)

    def test_point(self):
        point = self.line.point(2)
        self.assertEqual(point.x, 7)
        self.assertEqual(point.y, 8)
        self.assertEqual(point.z, 9)

    def test_str(self):
        self.assertEqual(str(self.line), "Line: {} + t{}".format(self.v1, self.line.direction_vector()))

    def test_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])
        ax.set_zlim([0, 10])

        # plot line
        xs = [self.v1.x, self.v2.x]
        ys = [self.v1.y, self.v2.y]
        zs = [self.v1.z, self.v2.z]
        ax.plot(xs, ys, zs)

        # plot point on line
        p = self.line.point(2)
        ax.scatter(p.x, p.y, p.z, c='r', marker='o')

        plt.show()


if __name__ == '__main__':
    unittest.main()
