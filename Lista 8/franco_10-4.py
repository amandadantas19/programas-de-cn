# -*- coding: latin-1 -*-
"""
* Resolução do exercício 10.4 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_10-4.py 
*
* Parâmetros usados para teste:
*                              python franco_10-4.py
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

    x =np.array([[2.8,16.44],[3.0,20.08],[3.2,24.53]])
    P, Y = lagrange(x,3.1)
    print "\npolinômio de interpolação: ",
    print P
    print "e^3.1 = %f\n"%Y

    
if __name__ == '__main__':
    main(sys.argv[1:])