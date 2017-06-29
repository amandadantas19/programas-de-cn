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

def f(x):
    return 7*x**5 - 3*x**2 - 1
def df(x):
    return x*(35*x**3 - 6)
def ddf(x):
    return 140*x**3 - 6
def dddf(x):
    return 420*x**2
def ddddf(x):
    return 840*x

def r3(x,x0,x1,x2,x3):
    derv = []

    derv.append(abs(ddddf(x0)))
    derv.append(abs(ddddf(x1)))
    derv.append(abs(ddddf(x2)))
    derv.append(abs(ddddf(x3)))
    

    maximo = max(derv)

    aux = ((abs(x - x0 ) * abs(x - x1) * abs(x-x2)*abs(x - x3))/24.) *maximo


    return abs(aux)

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
    
    x = np.array([-3,-2,-1,0,1,2,3])
    res = f(x)
    print "\t\tx   | ",
    for i in range(len(x)):
        print "\t %d"%x[i],
    print"  |"
    print"\t\t----|---------------------------------------------------------"
    print "\t\tf(x)|",
    for i in range(len(res)):
        print"\t%d"%res[i],
    print"|"
    
    pontos = np.array([[-2,-237],[-1,-11],[0,-1],[1,3]])
    P,Y = lagrange(pontos)
    print "Lagrange = ",
    print P
    
    aux = r3(-0.5,-3,-2,-1,0)
    print "R3 = " ,
    print aux

if __name__ == '__main__':
    main(sys.argv[1:])