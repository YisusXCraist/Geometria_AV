import unittest
from Vector import Vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)

    def test_add(self):
        v = self.v1 + self.v2
        self.assertEqual(v.x, 5)
        self.assertEqual(v.y, 7)
        self.assertEqual(v.z, 9)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)
        ax.quiver(0, 0, 0, self.v1.x, self.v1.y, self.v1.z, color='red')
        ax.quiver(self.v1.x, self.v1.y, self.v1.z, self.v2.x, self.v2.y, self.v2.z, color='blue')
        ax.quiver(0, 0, 0, v.x, v.y, v.z, color='green')
        plt.show()

    def test_subtract(self):
        v = self.v1 - self.v2
        self.assertEqual(v.x, -3)
        self.assertEqual(v.y, -3)
        self.assertEqual(v.z, -3)

    def test_scalar_multiply(self):
        v = self.v1 * 2
        self.assertEqual(v.x, 2)
        self.assertEqual(v.y, 4)
        self.assertEqual(v.z, 6)

    def test_dot_product(self):
        result = self.v1.dot(self.v2)
        self.assertEqual(result, 32)

    def test_cross_product(self):
        v = self.v1.cross(self.v2)
        self.assertEqual(v.x, -3)
        self.assertEqual(v.y, 6)
        self.assertEqual(v.z, -3)
        
    
if __name__ == '__main__':
    unittest.main()
