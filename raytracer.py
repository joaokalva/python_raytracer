# vector MAGNITUDE means vector length. You get that by applying the Pythagorian Theorem. Vlength = sqrt(exp(x,2)+exp(y,2)+exp(z,2)) 
# NORMALIZE vector means getting only the direction. normalizedV                                  = V / Vlength
# DOT PRODUCT      means a comparison of vectors. How much of V1 is pointing towards              = V2. V1 dot V2 = Vx1*Vx2 + Vy1*Vy2 + Vz1*Vz2 
# adition, subtraction, multiplication, division. 

## My attempt:
# import math as m

# A = [0,0,0]
# B = [3,4,5]

# def vectorMagnitude(A):
#     return m.sqrt(m.pow(A[0],2) + m.pow(A[1],2) + m.pow(A[2],2))

# def vectorNormalize(A):
#     magnitude = vectorMagnitude(A)
#     return [A[0] / magnitude, A[1] / magnitude, A[2] / magnitude]

# def vectorDot(A,B):
#     return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

# print(vectorDot(A,B))

import unittest
from vector import Vector
from image import Image

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)
    
    def testMagnitude(self):
        self.assertEqual(self.v1.magnitude(), 3.0)
        
    def testAddition(self):
        sum = self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 4.0)
        
    def testMultiplication(self):
        sum = self.v1 * 2
        self.assertEqual(getattr(sum, "x"), 2.0)
        
    def testDivision(self):
        sum = self.v1 / 2
        self.assertEqual(getattr(sum, "x"), 0.5)

if __name__ == "__main__":
    img = Image()
    img.buildImage()
    #unittest.main()