# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : newton_1.4-10.py <x1> <x2> <x3> <x4> <x5> 
*                 <xi> -> representam o chute inicial xi
*
* Parâmetros usados para teste:
*                              python newton_1.4-10.py 0 1 -1.5 0.8 -0.5 
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
	return 54*x**6 + 45*x**5 - 102*x**4- 69*x**3 + 35*x**2 + 16*x - 4
def df(x):
	return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16
def ddf(x):
	return 2*(810*x**4 + 450*x**3 - 612*x**3 + 35*x**2 + 16*x)


def newton (x, tolerancia = 0.000000001):
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

def multiplicidade(x):

	derivada_primeira = df(x)
	
	if (derivada_primeira != 0):
		return 1
	elif (derivada_segunda !=0):
		return 2
	elif (derivada_terceira !=0):
		return 3
	else:
		return 0

def main (argv):
	
	if (len(sys.argv) != 6):

		sys.exit('Parâmetros errados: newton_1.4-7.py <x1> <x2> <x3> <x4> <x5>')
	
	graph()

	raiz1 = newton(float(sys.argv[1]))
	raiz2 = newton(float(sys.argv[2]))
	raiz3 = newton(float(sys.argv[3]))
	raiz4 = newton(float(sys.argv[4]))
	raiz5 = newton(float(sys.argv[5]))

	print '\nRaizes: '

	for i in range(1,6):

		if i == 1:
			aux = raiz1
		elif i ==2:
			aux = raiz2
		elif i == 3:
			aux = raiz3
		elif i == 4:
			aux = raiz4
		else:
			aux = raiz5


		mul = multiplicidade(aux)
		if mul == 1 :
			print "%.6f" %aux,
			print', convergência quadrada;'
		else:
			print aux,
			print',convergência linear e m=',mul

if __name__ == '__main__':
	main(sys.argv[1:])