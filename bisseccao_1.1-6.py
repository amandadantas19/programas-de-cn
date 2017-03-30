# -*- coding: latin-1 -*-

"""
* Resolução do exercício 6 do capítulo 1.1 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python bisseccao_1.1-6.py <a> <b> <numero_de_iterações>
*                 <a> e <b> -> representam o intervalo [a,b]
*
* Parâmetros usados para teste:
*                              python bisseccao_1.1-6.py a 0 1 20
*                              
"""

import sys
import math

def f(x):
	return math.cos(x) - math.sin(x) #essa eh a funcao

# a tolerancia eh o numero de casas finais
def bisseccao (a,b,n):
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
	if(len(sys.argv) != 4):
		sys.exit("Parâmetros errados: bisection.py <a> <b> <número_de_iterações>")

	res = bisseccao (int(sys.argv[1]), int (sys.argv[2]), int(sys.argv[3]))

	if (res != None):
		print ('\n\tA raiz é: '),
		print res,
		print ('\n')
	
if __name__== "__main__":
	main(sys.argv[1:])