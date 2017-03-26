# -*- coding: latin-1 -*-

"""
* Resolução do exercício 1 do capítulo 1.1 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python bisseccao_1.1-1.py <letra> <a> <b> <numero_de_iterações>
*                 <letra> -> qual as letras o exercício (a, b ou c)
*                 <a> e <b> -> representam o intervalo [a,b]
*
* Parâmetros usados para teste:
*                              python bisseccao_1.1-1.py a 2 3 20
*                              python bisseccao_1.1-1.py b 1 2 20
*                              python bisseccao_1.1-1.py c 6 7 20
*
"""

import sys
import math

def fa(x):
	return x**3 - 9 #essa eh a funcao (a)

def fb(x):
	return 3*x**3 + x**2 - x - 5 #essa eh a funcao (b)

def fc(x):
	return (math.cos(x) * math.cos(x)) + 6 -x #essa eh a funcao (c)

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
	
	if(len(sys.argv) != 5):
		sys.exit("Parâmetros errados: bisecao_1.1-1.py <letra> <a> <b> <numero de iterações>")

	if(sys.argv[1] not in ['a','b','c']):
		sys.exit("Parâmetro de letra errado! São apenas válidos a, b ou c.")
	

	res = bisseccao (sys.argv[1], int(sys.argv[2]), int (sys.argv[3]), int(sys.argv[4]))
	if (res != None):
		print ('\n\tA raiz da letra é: '),
		print res,
		print ('\n')
	

if __name__== "__main__":
	main(sys.argv[1:])