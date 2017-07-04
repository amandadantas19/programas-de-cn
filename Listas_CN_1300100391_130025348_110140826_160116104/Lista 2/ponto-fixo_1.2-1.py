# -*- coding: latin-1 -*-
"""
* Resolução do exercício 1 do capítulo 1.2 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python ponto-fixo_1.2-1.py <letra> <x>
*                 <letra> -> qual as letras o exercício (a, b ou c)
*                 <x> -> representam o chute inicial xo
*
* Parâmetros usados para teste:
*                              python ponto-fixo_1.2-1.py a 1 
*                              python ponto-fixo_1.2-1.py b 1 
*                              python ponto-fixo_1.2-1.py c 1 
*
"""
import math
import sys


def ga(x):
	return (2*x + 2) **(1/3.0) #essa é a função (a)
def gb(x):
	return math.log(7-x) #essa é a função (b)
def gc(x):
	return math.log(4 - math.sin(x)) #essa é a função (c)

MAX = 200 #constante do número máximo de iterações

def ponto_fixo(letra,x):

	if (letra == 'a'):
		def g(x):
			return ga(x)
	elif (letra == 'b'):
		def g(x):
			return gb(x)
	else:
		def g(x):
			return gc(x)

	i = 0
	erro = 1
	x_novo = x

	while ((erro >.5E-8) and (i < MAX)):
		print '\t\t',i,'\t', x_novo,'\t', g(x_novo)
		x_antigo = x_novo
		x_novo = g(x_novo)
		i = i +1
		erro = abs(x_novo - x_antigo)/ (abs(x_novo) + 0.000000001)

	if (i == 200):
		print 'Limite de 200 iterações atingido'
	else:
		print 'A raiz é: ',
		print ("%.8f" % x_novo)

def main (argv):
	
	if (len(sys.argv) != 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <letra> <x>')

	print '\tTABELA:\n\n\t\ti\txi\tg(xi)\n'
	res = ponto_fixo (sys.argv[1], float (sys.argv[2]))


if __name__ == '__main__':
	main(sys.argv[1:])