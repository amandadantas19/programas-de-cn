# -*- coding: latin-1 -*-
import math
import sys

def g(x):
	return (2*x + 2) **(1/3.0)

def ponto_fixo(x,k):
	for i in range(k):
		print '\t\t',i,'\t', x,'\t', g(x)
		x = g(x)
	print 'A raiz é: ',
	return x

def main (argv):
	if (len(sys.argv) != 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <x> <k> ')

	print '\tTABELA:\n\n\t\ti\txi\tg(xi)\n'
	print ponto_fixo (float (sys.argv[1]), int (sys.argv[2]))

if __name__ == '__main__':
	main(sys.argv[1:])