# -*- coding: latin-1 -*-

"""
* Resolução do exercício 3 do capítulo 1.1 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python bisecao_1.1-3.py <letra> <a1> <b1> <a2> <b2> <a3> <b3> <numero de iterações>
*                 <letra> -> qual as letras o exercício (a, b ou c)
*                 <ai> e <bi> -> representam o intervalo [a,b] numero i
*
* Parâmetros usados para teste:
*                              python bisseccao_1.1-3.py a -2 -1 -1 0 1 2 20
*                              python bisseccao_1.1-3.py b -2 -1 -0.5 0.5 0.5 1.5 20
*                              python bisseccao_1.1-3.py c -1.7 -0.7 -0.7 0.3 0.3 1.3 20
*
"""

import sys
import math

def fa(x):
	return 2*x**3 - 6 * x - 1 #essa eh a funcao (a)

def fb(x):
	return math.exp(x-2) + x**3 - x #essa eh a funcao (b)

def fc(x):
	return 1 + 5*x - 6*x**3 - math.exp(2*x) #essa eh a funcao (c)

# a tolerancia eh o numero de casas finais
def bisseccao (letra,a,b,n):

	if(letra == 'a'):
		def f(x):
			return fa(x)
	elif (letra == 'b'):
		def f(x):
			return fb(x)
	else:
		def f(x):
			return fc(x)

	if f(a) * f(b) >= 0:
		print ('Erro! f(a)f(b) < 0 não ocorre')
		return None
	else:
		i = 1
		#while ((b-a)/2.0 > tolerancia):
		while (i <= n):
			c = (a+b)/2.0
			if f(c) == 0: 
				return c
			elif f(a)*f(c) < 0:
				b = c
				i = i +1
			else: 
				a = c
				i = i +1


		return c


def main (argv) :
	
	if(len(sys.argv) != 9):
		sys.exit("Parâmetros errados: bisecao_1.1-3.py <letra> <a1> <b1> <a2> <b2> <a3> <b3> <numero de iterações>")

	if(sys.argv[1] not in ['a','b','c']):
		sys.exit("Parâmetro de letra errado! São apenas válidos a, b ou c.")
	

	res1 = bisseccao (sys.argv[1], float(sys.argv[2]), float (sys.argv[3]), float(sys.argv[8]))
	if (res1 != None):
		print ('\n\tA primeira raiz é: '),
		print ("%.6f" % res1),
		print ('\n')
	
	res2 = bisseccao (sys.argv[1], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[8]))
	if (res2!= None):
		print ('\n\tA segunda raiz é: '),
		print ("%.6f" % res2),
		print ('\n')

	res3 = bisseccao (sys.argv[1], float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]))
	if (res3 != None):
		print ('\n\tA terceira raiz é: '),
		print ("%.6f" % res3),
		print ('\n')
	
	

if __name__== "__main__":
	main(sys.argv[1:])