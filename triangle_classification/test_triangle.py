'''
Created on Sep 1, 2018
@author: Oscar Tavara
'''
import unittest
import math
from triangle_classification import triangle

class TestTriangles(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_RightTriangle(self):
        self.assertEqual(triangle.classifyTriangle([3.0,4.0,5.0]),'Right Scalene Triangle')
        self.assertEqual(triangle.classifyTriangle([5,5,5*math.sqrt(2)]),'Right Isosceles Triangle')
        
    def test_NonRightTriangle(self): 
        self.assertEqual(triangle.classifyTriangle([1,1,1]),'Equilateral Triangle')
        self.assertNotEqual(triangle.classifyTriangle([20,20,20]),'Isoceles Triangle')
        self.assertEqual(triangle.classifyTriangle([15,215,10]),'Scalene Triangle')
    
    def test_validSide(self): 
        self.assertTrue(triangle.validSide(5.0))
        self.assertFalse(triangle.validSide(-1))
    
    def test_validTriangle(self): 
        self.assertTrue(triangle.validTriangle([2.0,2.0,2.0]))
        self.assertFalse(triangle.validTriangle([1,1.0,1.0,1.0]))
        self.assertFalse(triangle.validTriangle([1]))

if __name__ == '__main__':  
    unittest.main(exit=False)