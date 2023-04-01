import unittest
from Vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([1, 2, 3])
        self.v2 = Vector([4, 5, 6])
    
    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(result, Vector([5, 7, 9]))
        
    def test_subtract(self):
        result = self.v1 - self.v2
        self.assertEqual(result, Vector([-3, -3, -3]))
        
    def test_scalar_multiply(self):
        result = self.v1 * 2
        self.assertEqual(result, Vector([2, 4, 6]))
        
    def test_dot_product(self):
        result = self.v1.dot(self.v2)
        self.assertEqual(result, 32)
        
    def test_cross_product(self):
        result = self.v1.cross(self.v2)
        self.assertEqual(result, Vector([-3, 6, -3]))
        
if __name__ == '__main__':
    unittest.main()
