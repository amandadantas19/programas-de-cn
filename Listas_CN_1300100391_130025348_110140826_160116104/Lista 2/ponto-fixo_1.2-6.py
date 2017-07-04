# -*- coding: latin-1 -*-
"""
* Resolução do exercício 6 do capítulo 1.2 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : python ponto-fixo_1.2-6.py <letra> <x>
*                 <letra> -> qual as letras o exercício (a, b ou c)
*                 <x> -> representam o chute inicial xo para todas as letras
*				ou
*				   python ponto-fixo_1.2-6.py <letra> <xa> <xb> <xc>
*				   <letra> -> qual das letras do exercícios (a, b ou c)
*                  <xi> -> chute para o exercício i
*
* Parâmetros usados para teste:
*                              python ponto-fixo_1.2-6.py a 1 
*                              python ponto-fixo_1.2-6.py b 0 2 0 
*                              python ponto-fixo_1.2-2.py c 0 0.5 0 
*
* PS: ga3 e ga2 retornam a mesma raiz!!!
*
"""
import math
import sys


# g(x)'s
def ga1(x):
	return ((6*x + 1)/ 2.0) ** (1/3.0) #essa é a primeira g(x) função (a)
def ga2(x):
	return (2*x**3 - 1)/6.0 #essa é a segunda g(x) função (a)
def ga3(x):
	return (x**3 +1 ) / (3*x**2 - 6)#essa é a terceira g(x) função (a)

def gb1(x):
	return (x - math.exp(x-2)) ** (1/3.0)#essa é a primeira g(x) função (b)
def gb2(x):
	return math.exp(x-2) + x**3 #essa é a segunda g(x) função (b)
def gb3(x): 
	return math.exp(x)/(math.exp(2)*(1-x**2)) #essa é a terceira g(x) função (b)

def gc1(x):
	return (6 *x**3 + math.exp(2*x)-1)/5#essa é a primeira g(x) função (c)
def gc2(x):
	return ((1 + 5 *x - math.exp(2*x))/ 6) ** (1/3.0)#essa é a segunda g(x) função (c)
def gc3(x): 
	return (math.exp(2*x) - 1)/(5-6*x**2)#essa é a terceira g(x) função (c)


# s(x)'s (derivada de g(x))
def sa1(x):
	return 1/((3*x + 1/2.0) ** (2/3.0)) 
def sa2(x):
	return x**2
def sa3(x):
	return (x*(x**3 - 6*x - 2))/(3*(x**2 - 2)**2)

def sb1(x):
	return (1 - math.exp(x - 2))/ (3 * (x - math.exp(x-2))**(2/3.0))
def sb2(x):
	return 3 * x**2 + math.exp(x-2)
def sb3(x):
	return (math.exp(x-2) * (-x**2 + 2*x + 1))/(x**2 -1) **2

def sc1(x):
	return (2 * (9*x**2 + math.exp(2*x)))/5
def sc2(x):
	return (5 - 2 * math.exp(2*x))/(3 * 6 ** (1/3.0)* (5*x - math.exp(2*x) + 1) ** (2/3.0))
def sc3(x):
	return (5-18 * x**2)/(-12*x**3 + 10*x + 2)

MAX = 200 #constante do número máximo de iterações

def ponto_fixo(letra,x,*outros):
	for k in range(3):
		if (letra == 'a'):
			if(k ==0):
				def g(x):
					return ga1(x)
				def s(x):
					return sa1(x)
			elif ( k == 1):
				def g(x):
					return ga2(x)
				def s(x):
					return sa2(x)
				if outros:
					x = outros[0]
			else:
				def g(x):
					return ga3(x)
				def s(x):
					return sa3(x)
				if outros:
					x = outros[1]
		elif (letra == 'b'):
			if(k ==0):
				def g(x):
					return gb1(x)
				def s(x):
					return sb1(x)
			elif ( k == 1):
				def g(x):
					return gb2(x)
				def s(x):
					return sb2(x)
				if outros:
					x = outros[0]
			else:
				def g(x):
					return gb3(x)
				def s(x):
					return sb3(x)
				if outros:
					x = outros[1]
		else:
			if(k ==0):
				def g(x):
					return gc1(x)
				def s(x):
					return sc1(x)
			elif ( k == 1):
				def g(x):
					return gc2(x)
				def s(x):
					return sc2(x)
				if outros:
					x = outros[0]
			else:
				def g(x):
					return gc3(x)
				def s(x):
					return sc3(x)
				if outros:
					x = outros[1]
		i = 0
		erro = 1
		erro_antigo = 0
		x_novo = x

		while ((erro >.5E-6) and (i < MAX)):
			print '\t\t',i,'\t', x_novo,'\t', g(x_novo)
			x_antigo = x_novo
			x_novo = g(x_novo)
			i = i +1
			erro_antigo = erro
			erro = abs(x_novo - x_antigo)/ (abs(x_novo) + 0.000000001)
			
		if (i > MAX):
			print 'Limite de 200 iterações atingido'
		#elif (erro == x_novo ):
			print 'g(x) diverge'
		else:
			print '\nA raiz é: ',
			print ("%.8f" % x_novo)
			print 'S por erros: ',
			print("%.4f" % (erro/erro_antigo))
			print 'S por calculo',
			print ("%.4f" % s(x_novo))
			print 'g(x) converge'

def main (argv):
	
	if (len(sys.argv) < 3):
		sys.exit('Parâmetros errados: ponto_fixo.py <letra> <x1> <x2> <x3>')

	if (len (sys.argv) == 3):
		print '\tTABELA:\n\n\t\ti\txi\tg(xi)\n'
		res = ponto_fixo (sys.argv[1], float (sys.argv[2]))
	else :
		print '\tTABELA:\n\n\t\ti\txi\tg(xi)\n'
		res = ponto_fixo (sys.argv[1], float (sys.argv[2]), float (sys.argv[3]),float (sys.argv[4]))

if __name__ == '__main__':
	main(sys.argv[1:])