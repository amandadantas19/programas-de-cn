# -*- coding: latin-1 -*-
"""
* Resolução do exercício 3 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python newton_1.4-3.py <letra> <x>
*                 <letra> -> qual as letras o exercício (a, b ou c)
*                 <x> -> representam o chute inicial xo para todas as letras
*				
* Parâmetros usados para teste:
*                              python newnton_1.4-3.py a  
*                              python newnton_1.4-3.py b 
*                              python newnton_1.4-3.py c  
*
*
"""
import math
import sys

def fa(x):
	return 27*x**3 + 54*x**2 + 36*x + 8
def dfa(x):
	return 9*(3*x + 2)**2
def ddfa(x):
	return 54*(3*x + 2)

def fb(x):
	return 36*x**4 - 12*x**3 + 37*x**2 - 12*x + 1
def dfb(x):
	return 2*(72*x**3 - 18*x**2 + 37*x - 6)
def dffb(x):
	return 432*x**2 - 72*x + 74

def newton (letra,x):

	if(letra == 'a'):
		def f(x):
			return fa(x)
		def df(x):
			return dfa(x)
	else:
		def f(x):
			return fb(x)
		def df(x):
			return dfb(x)
	
	aux = 1;
	i = 0
	print '\t\t',i,'\t', x
	while(aux != 0):
		aux = df(x)
		if(aux != 0):
			x1 = x - f(x)/df(x)
			t = abs(x1 - x)
			i = i + 1
			print '\t\t',i,'\t', x1,'\t', t

			if t == 0:
				break
			x = x1
	return x

def multiplicidade (letra, x):

	if (letra == 'a'):
		def df(x):
			return dfa(x)
		def ddf(x):
			return ddfa(x)
	else:
		def df(x):
			return dfb(x)
		def ddf(x):
			return ddfb(x)

	derivada_primeira = df(x)

	if (derivada_primeira != 0):
		print '\nA raiz tem multiplicidade 1 já que f`(x) = %.12f' % derivada_primeira
	else:
		derivada_segunda = ddf(x)

		print '\nA raiz tem multiplicidade 2 já que a f`(x) = %.12f' % derivada_primeira 
		print 'e f``(x) = %f' %derivada_segunda

def modified_newton (letra,x, tolerancia = 0.00000001):
	i = 0
	if(letra == 'a'):
		def f(x):
			return fa(x)
		def df(x):
			return dfa(x)
		def ddf(x):
			return ddfa(x)
	else:
		def f(x):
			return fb(x)
		def df(x):
			return dfb(x)
		def ddf(x):
			return ddfb(x)
	
	while(True):
		aux = ((df(x) *df(x)) - (f(x) * ddf(x)))
		if(aux != 0):
			x1 = x - (f(x)* df(x))/((df(x)*df(x)) - (f(x) *ddf(x)))
			t = abs(x1 - x)
			i = i +1
			print '\t\t',i,'\t',x1,'\t',t

			if t < tolerancia:
				break
			x = x1
		else:
			break
		
	return x


def main (argv):
	
	if (len(sys.argv) != 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <letra> <x>')

	else :
		print '\tTABELA NEWTON:\n\n\t\ti\txi\terro\n'
		res_n = newton(sys.argv[1], float (sys.argv[2]))
		
		print'\n\tTABELA NEWTON MODIFICADO:\n\n\t\ti\txi\terro\n'
		res_m = modified_newton(sys.argv[1],float(sys.argv[2]))

		print'\n\nA raiz aproximada ao máximo pelo Método de Newton é ', "%f" % res_n
		multiplicidade(sys.argv[1],res_n)
		print '\nA raiz aproximada pelo Método de Newton Modificado é',"%f\n" %res_m

if __name__ == '__main__':
	main(sys.argv[1:])
