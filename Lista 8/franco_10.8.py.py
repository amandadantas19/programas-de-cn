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

def ddddf(x):
    return np.cos(x)

def r3(x,x0,x1,x2,x3):
    derv = []

    derv.append(abs(ddddf(x0)))
    derv.append(abs(ddddf(x1)))
    derv.append(abs(ddddf(x2)))
    derv.append(abs(ddddf(x3)))
    

    maximo = max(derv)

    aux = ((abs(x - x0 ) * abs(x - x1) * abs(x-x2)*abs(x - x3))/24.) *maximo


    return abs(aux)

def main (argv):
    
    aux = r3(1.05,1,1.1,1.3,1.5)
    print "R3 = " ,
    print aux

if __name__ == '__main__':
    main(sys.argv[1:])