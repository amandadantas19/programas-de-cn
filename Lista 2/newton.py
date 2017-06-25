# -*- coding: latin-1 -*-
"Falta olhara a divisão por zero"
import math
import sys
import sympy

def f(x):
	return x**3 + x - 1
def df(x):
	return 3*x**2 + 1


def newton (x, tolerancia = 0.000001):
	while(True):
		aux = df(x)
		if(aux):
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
	
	"""if (len(sys.argv) != 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <letra> <x>')"""

	res = newton (-0.7) 


if __name__ == '__main__':
	main(sys.argv[1:])