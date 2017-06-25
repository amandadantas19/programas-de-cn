# -*- coding: latin-1 -*-
"Falta olhar a divisão por zero. "
import math
import sys
import sympy

def f(x):
	return x**3 + x - 1
def df(x):
	return 3*x**2 + 1
def ddf(x):
	return 6*x

def modified_newton (x, tolerancia = 0.000001):
	while(True):
		aux = ((df(x) *df(x)) - (f(x) * ddf(x)))
		if(aux != 0):
			x1 = x - (f(x)* df(x))/((df(x)*df(x)) - (f(x) *ddf(x)))
			t = abs(x1 - x)
			"""print ("%.8f" % x1)"""

			if t < tolerancia:
				break
			x = x1
		else:
			print("Algoritmo interrompido. (divisão por zero)")
			break
	return x
def multiplicidade_quadrada (letra, x):

	derivada_primeira = df(x)

	if (derivada_primeira != 0):
		print '\nA raiz %f'%x,
		print' tem multiplicidade 1 já que f`(x) = %.12f' % derivada_primeira
	else:
		derivada_segunda = ddf(x)

		print '\nA raiz %f'%x
		print ' tem multiplicidade 2 já que a f`(x) = %.12f' % derivada_primeira 
		print 'e f``(x) = %f' %derivada_segunda


def main (argv):
	
	"""if (len(sys.argv) != 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <letra> <x>')"""

	res = modified_newton (-0.7) 


if __name__ == '__main__':
	main(sys.argv[1:])