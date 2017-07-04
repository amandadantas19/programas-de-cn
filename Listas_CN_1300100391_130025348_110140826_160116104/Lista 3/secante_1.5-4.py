# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : secante_1.5-7.py <x1> <x2> <x3> <x4>
*                 <x> -> representam o chute inicial xo
*
* Parâmetros usados para teste:
*                              python secante_1.5-7.py -1 1.5 0 
*
"""

import math
import sys
import sympy
import numpy as np
import matplotlib.pyplot as plt

def graph ():
	x = np.arange(-2.0,2.1,0.5)
	y = f(x)
	plt.plot(x,y)
	plt.show()

def f(x):
	return 54*x**6 + 45*x**5 - 102*x**4 -69*x**3 + 35*x**2 + 16*x - 4

def secante(x0,x1, tolerancia=0.00000001, NMAX=200):

	n=1
	while n<=NMAX:
		x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))

		t = abs(x2 - x1)
		if t < tolerancia:
			return x2
		else:
			x0 = x1
			x1 = x2
	return False

def main (argv):
    
	graph()

	print "Raizes:"   
	raiz1 = secante (1.0,-1.0)
	print "(1) %.6f com os chutes iniciais 1 e -1" %raiz1
	raiz2 = secante (0.0,-1.0)
	print "(2) %.6f com os chutes iniciais 0 e -1" %raiz2
	raiz3 = secante (1.0,2.0)
	print "(3) %.6f com os chutes iniciais 1 e 2" %raiz3
	raiz4 = secante (0.0,0.4)
	print "(4) %.6f com os chutes iniciais 0 e 0.4" %raiz4
	raiz5 = secante (-2.0,-1.5)
	print "(5) %.6f com os chutes iniciais -2 e -1.5" %raiz5
if __name__ == '__main__':
    main(sys.argv[1:])
