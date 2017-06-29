# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5 do capítulo 1.4 (Timothy Sauer. Numerical Analysis. Pearson, 2ª Edição)
* 
* Executado como : newton_1.4-11.py 
*
* Parâmetros usados para teste:
*                              python newton_1.4-11.py
*
"""

import sys
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot,linalg,divide,amax

def converge_dominante(A):

    n = len(A)
    soma = 0
    for i in range(n):
        j = i
        if j != 0:
            k = j-1
            while k >= 0:
                soma = abs(A[i][k]) + soma
                k = k -1

        if j != n-1:
            k = j+1
            while k <n:
                soma = abs(A[i][k]) + soma
                k = k+1
        if soma >=  A[i][j]:
            return False
            break
        soma = 0
    return True

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

def converge_coluna(A):

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
                soma = abs(x[k][i])+ soma
                k = k -1

        if j != n-1:
            k = j+1
            while k <n:
                soma = abs(x[k][i]) + soma
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

    A = array([[10,2,1],[1,5,1],[2,3,10]])
    #bol = converge_dominante(A)
    
    print "A:"
    pprint(A)
    bol = False
    if bol:
        print "\n A matriz A é convergente porque é uma matriz dominante."
    else:
        print "\n A matriz A não é uma matriz dominante."

        bol = converge_linha(A)

        if bol:
            print "\n A matriz A é convergente pelo critério das linhas."
        else:
            print "\n A matriz A não é convergente pelo critério das linhas."

if __name__ == '__main__':
    main(sys.argv[1:])