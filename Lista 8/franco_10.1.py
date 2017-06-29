# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : newton_1.4-11.py 
*
* Parâmetros usados para teste:
*                              python newton_1.4-11.py
*
"""

import sys
import math
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

def main (argv):

    x =np.array([[1,0],[3,6],[4,24],[5,60]])
    P, Y = lagrange(x,3.5)
    print "\npolinômio de interpolação: ",
    print P
    print "f(3.5) = %f\n"%Y

    
if __name__ == '__main__':
    main(sys.argv[1:])