from sympy import *
from sympy.matrices import *
import numpy as numpy
import pylab

def Lagrange_interpolation(points, variable=None):
    x = Symbol("x")
    L = zeros(1, points.shape[0])
    i = 0

    for p in points:
        numerator = 1
        denominator = 1
        other_points = np.delete(points, i, 0)

        for other_p in other_points:
            numerator = numerator * (x - other_p[0])
            denominator = denominator * (p[0] - other_p[0])

        L[i] = numerator / denominator
        i = i+1
        
    #reduzir os problemas com floats
    P = horner(L.multiply(points[..., 1])[0])
    Y = None
    
    if variable != None 
        Y = lambdify(x, P, 'numpy')
        Y = Y(variable)
           
            
    return P,Y

def test_Lagrange(sets):
    for points in sets:
        x = numpy.linspace(0, 100)
        P, Y = Lagrange_interpolation(points, x)
    
        print(P)
        pylab.plot(x, Y)
        

if __name__ == '__main__':
    x =numpy.array([[-1,15],[0,8],[3,-1]])
    P, Y = Lagrange_interpolation(x,None)
    print P