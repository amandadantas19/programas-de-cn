# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : newton_1.4-7.py <x1> <x2> <x3> <x4>
*                 <x> -> representam o chute inicial xo
*
* Parâmetros usados para teste:
*                              python newton_1.4-7.py -1 1.5 0 
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
	return np.exp(np.sin(x)**3) + x**6 - 2*x**4 - x**3 - 1
def df(x):
	return (6*x**3- 8*x - 3)*x**2 + 3*np.exp(np.sin(x)**3)*(np.sin(x)**2)*np.cos(x)
def ddf(x):
	return (6*x*(5*x**3 - 4*x-1) - 3*np.exp(np.sin(x))**3)*(np.sin(x)**3) + 3*np.exp(np.sin(x)**3)*(3*(np.sin(x)**3) + 2)*np.sin(x)*np.cos(x)**2
def dddf(x):
	return 3*(2*(20*x**3 - 8*x - 1)*np.sin(x)**3 - np.sin(x)**2*(6*x*(-5*x**3 + 4*x +1) + 9 * np.exp(np.sin(x)**3) * np.sin*(x)**3 + 7*np.exp(np.sin(x)**3))*np.cos(x)
	       + np.exp(np.sin(x)**3)(9*np.sin(x)**6 + 18*np.sin(x)**3+2)*np.cos(x)**3)

def newton (x, tolerancia = 0.000001):
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

def multiplecidade():
	print ok


def multiplicidade_quadrada (x):

	derivada_primeira = df(x)
	derivada_segunda = ddf(x)

	if (derivada_primeira != 0):
		return 1

def multiplicidade_linear(x):
	derivada_segunda = ddf(x)
	derivada_terceira = dddf(x)

	if (derivada_segunda !=0):
		return 2
	else:
		return 3

def main (argv):
	
	if (len(sys.argv) != 4):

		sys.exit('Parâmetros errados: newton_1.4-7.py <x1> <x2> <x3>')

	graph()

	raiz1 = newton(float(sys.argv[1]))
	raiz2 = newton(float(sys.argv[2]))
	raiz3 = newton(float(sys.argv[3]))

	print 'Raizes: '

	for i in range(1,4):

		if i == 1:
			aux = raiz1
		elif i ==2:
			aux = raiz2
		else:
			aux = raiz3


		mul = multiplicidade_quadrada(aux)
		if mul == 1 :
			print "%.6f" %aux,
			print', convergência quadrada;'
		else:
			print aux,
			print',convergência linear e m=',mul
	
if __name__ == '__main__':
	main(sys.argv[1:])