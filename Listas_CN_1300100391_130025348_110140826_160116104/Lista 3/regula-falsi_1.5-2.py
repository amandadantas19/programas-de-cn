# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : regula-falsi_1.5-2.py 
*
* Parâmetros usados para teste:
*                              regula-falsi_1.5-2.py
*
"""

import math
import sys
import sympy

def f1(x):
    return 2*x + 2 - x**3
def f2(x):
    return math.exp(x) + x - 7 
def f3(x):
    return math.exp(x) + math.sin(x) - 4

def regula_falsi(numero,a, b, max_steps = 3):  

    aux = "f" + str(numero) +"("

    for i in range(max_steps):
        
        c = (b*eval(aux + str(a) + ")") - a*eval(aux + str(b) + ")"))/float(eval(aux + str(a)+ ")") - eval(aux + str(b) + ")"))
        
        if eval(aux + str(c) + ")") == 0.0:
            break
        elif (eval(aux + str(a) + ")") * eval(aux + str(c) + ")")) < 0:
            b = c
        else:
            a = c
    return c

def main (argv):
    
    raiz1 = regula_falsi(1,1,2)
    raiz2 = regula_falsi(2,1,2)
    raiz3 = regula_falsi(3,1,2)

    print "\n(a) raiz = %.6f"%raiz1
    print "(b) raiz = %.6f"%raiz2
    print "(c) raiz = %.6f"%raiz3
    
    

if __name__ == '__main__':
    main(sys.argv[1:])
