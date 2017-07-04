# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5.19 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_5-19.py 
*
* Parâmetros usados para teste:
*                              python franco_5-19.py
*
"""

import sys
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot,linalg,divide,amax


def converge_linha(A):

    n = len(A)
    diag = A.diagonal()
    x = [[0.0] * len(A) for _ in xrange(len(A))]
    
    for i in range(n):
        for j in range(n):
            x[i][j] = A[i][j]/float(diag[i])
            
    B = [0.0] * n 
    soma = 0

    for i in range(n):
        j = i
        if j != 0:
            k = j-1
            while k >= 0:
                soma = abs(x[i][k])+ soma
                k = k -1

        if j != n-1:
            k = j+1
            while k <n:
                soma = abs(x[i][k]) + soma
                k = k+1
        B[i] = soma
        soma = 0
    maior = amax(B)
    print B
    if maior < 1:
        return True
    else:
        return False

def main (argv):

    A = array([[-4,2,-2],[1,-4,1],[2,2,-4]])
    B = array([[4,2,-2],[1,4,1],[2,2,4]])
    C = array([[-5,2,-2],[1,-5,1],[2,2,-5]])
    D = array([[6,2,-2],[1,6,1],[2,2,6]])
    
    bolA= converge_linha(A)
    bolB = converge_linha(B)
    bolC = converge_linha(C)
    bolD = converge_linha(D)

    print "A:"
    pprint(A)
    if bolA:
        print "\n A matriz A é convergente pelo critério das linhas."
    else:
        print "\n A matriz A não é convergente pelo critério das linhas."

    print "B:"
    pprint(B)
    if bolB:
        print "\n A matriz B é convergente pelo critério das linhas."
    else:
        print "\n A matriz B não é convergente pelo critério das linhas."

    print "C:"
    pprint(C)
    if bolC:
        print "\n A matriz C é convergente pelo critério das linhas."
    else:
        print "\n A matriz C não é convergente pelo critério das linhas."

    print "D:"
    pprint(D)
    if bolD:
        print "\n A matriz D é convergente pelo critério das linhas."
    else:
        print "\n A matriz D não é convergente pelo critério das linhas."
        
if __name__ == '__main__':
    main(sys.argv[1:])