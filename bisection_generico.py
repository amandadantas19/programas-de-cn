# -*- coding: latin-1 -*-
import sys
import math

def f(x):
	return x**2 - 2 #essa eh a funcao

# a tolerancia eh o numero de casas finais
def bisseccao (a,b,tolerancia):
	if f(a) * f(b) >= 0:
		print ('Erro! f(a)f(b) < 0 não ocorre')
		return None
	else:
		while ((b-a)/2.0 > tolerancia):
			c = (a+b)/2.0
			if f(c) == 0: 
				return c
			elif f(a)*f(c) < 0:
				b = c
			else: 
				a = c

		return c


def main (argv) :
	if(len(sys.argv) != 4):
		sys.exit("Parâmetros errados: bisection.py <a> <b> <tolerancia>")

	res = bisseccao (int(sys.argv[1]), int (sys.argv[2]), float(sys.argv[3]))

	if (res != None):
		print ('\n\tA raiz é: '),
		print res,
		print ('\n')
	
if __name__== "__main__":
	main(sys.argv[1:])