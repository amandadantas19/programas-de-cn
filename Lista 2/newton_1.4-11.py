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


def f(x):
	return (15 + (1.36 / x**2)) * (x - 0.003183) - (0.0820578*320)
def df(x):
	return (15*(x**3 - 0.0906667*x + 0.000577184))/x**3

def newton (x, tolerancia = 0.0001):
	while(True):
		aux = df(x)
		if(aux != 0):
			x1 = x - f(x)/df(x)
			t = abs(x1 - x)/(abs(x1) + 0.000001)
			

			if t < tolerancia:
				break
			x = x1
		else:
			print("Algoritmo interrompido. (divisão por zero) ")
			break
	return x


def main (argv):
	
	x = (0.0820578*320)/15
	raiz = newton(x)
	print "\nChute inicial = %f" % x,
	print " e raiz = %.6f"%raiz
	


if __name__ == '__main__':
	main(sys.argv[1:])
