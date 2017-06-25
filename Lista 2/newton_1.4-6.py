# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : newton_1.4-6.py <x>
*                 <x> -> representam o chute inicial xo
*
* Parâmetros usados para teste:
*                              python newton_1.4-6.py 1 
*
"""

import math
import sys
import sympy

def f(x):
	return math.pi*x**2*10 + 2/3.0 * math.pi * x**3 - 60
def df(x):
	return x*(6.28319*x+62.8319)


def newton (x, tolerancia = 0.00001):
	while(True):
		aux = df(x)
		if(aux != 0):
			x1 = x - f(x)/df(x)
			t = abs(x1 - x)
			print ("%.8f" % x1)

			if t < tolerancia:
				break
			x = x1
		else:
			print("Algoritmo interrompido. (divisão por zero) ")
			break
	return x


def main (argv):
	
	if (len(sys.argv) != 2):
		sys.exit('Parâmetros errados: newton_1.4-6.py <x>')

	res = newton (float(sys.argv[1])) 
	print 'Resposta : %0.4f' % res


if __name__ == '__main__':
	main(sys.argv[1:])