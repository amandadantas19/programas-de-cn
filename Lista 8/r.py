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
    return 27 * np.exp(3*x) * (1+x)
def ddddf(x):
    return 840*x

def r2(x,x0,x1,x2):
    derv = []

    derv.append(abs(dddf(x0)))
    derv.append(abs(dddf(x1)))
    derv.append(abs(dddf(x2)))

    print derv

    maximo = max(derv)

    aux = ((abs(x - x0 ) * abs(x - x1) * abs(x-x2))/6.) *maximo


    return abs(aux)


def main (argv):
    
    aux = r2(0.25,0.2,0.3,0.4)
    print "R3 = " ,
    print aux

if __name__ == '__main__':
    main(sys.argv[1:])