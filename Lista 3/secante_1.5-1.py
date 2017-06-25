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

import math
import sys
import sympy

def f1(x):
	return 2*x + 2 - x**3
def f2(x):
	return math.exp(x) + x - 7 
def f3(x):
	return math.exp(x) + math.sin(x) - 4

def secante(numero,x0,x1, tolerancia=0.00000001, NMAX=200):

	aux = "f" + str(numero) +"("
	

	n=1
	while n<=NMAX:
		x2 = x1 - ((eval(aux + str(x1) + ")")*(x1-x0))/(eval(aux + str(x1)+")")-eval(aux + str(x0) + ")")))

		t = abs(x2 - x1)
		if t < tolerancia:
			return x2
		else:
			x0 = x1
			x1 = x2
	return False

def main (argv):
	
	raiz1 = secante (1,float(sys.argv[1]),float(sys.argv[2]))
	raiz2 = secante (2,float(sys.argv[1]),float(sys.argv[2]))
	raiz3 = secante (3,float(sys.argv[1]),float(sys.argv[2]))

	print "\n(a) raiz = %.6f"%raiz1
	print "(b) raiz = %.6f"%raiz2
	print "(c) raiz = %.6f"%raiz3
	


if __name__ == '__main__':
	main(sys.argv[1:])
