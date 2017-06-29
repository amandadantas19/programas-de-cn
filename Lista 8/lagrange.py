from sympy import *
from sympy.matrices import *
import numpy as np


def lagrange(pontos, valor=None):
    x = Symbol("x")
    L = zeros(1, pontos.shape[0])
    i = 0

    for p in pontos:
        numerador = 1
        denominador = 1
        other_pontos = np.delete(pontos, i, 0)

        for other_p in other_pontos:
            numerador = numerador * (x - other_p[0])
            denominador = denominador * (p[0] - other_p[0])

        L[i] = numerador / denominador
        i = i+1
        
    #reduzir os problemas com floats
    P = horner(L.multiply(pontos[..., 1])[0])
    Y = None
    
    if valor != None :
        Y = lambdify(x, P, 'numpy')
        Y = Y(valor)
           
            
    return P,Y

if __name__ == '__main__':
    x =np.array([[-1,15],[0,8],[3,-1]])
    P, Y = lagrange(x,None)
    print P