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
from numpy import array, zeros, diag, diagflat, dot,linalg,tril
from scipy.linalg import solve

def sassenfeld(A):

    n = len(A)
    soma = 0
    B = [1] * len(A)

    for i in range(n):
        j = i
        if j != 0:
            k = j-1
            while k >= 0:
                soma = abs(A[i][k])*B[k] + soma
                k = k -1

        if j != n-1:
            k = j+1
            while k <n:
                soma = abs(A[i][k])*B[k] + soma
                k = k+1
        B[i] = soma/float(abs(A[i][j]))
        
        if B[i] > 1:
            return False
            break
        soma = 0
    
    return True

def gauss(A, b, x, n):

    L = tril(A)
    U = A - L
    for i in range(n):
        # x^(k+1) = L*^(-1)*(b-Ux^(k))
        x = dot(linalg.inv(L), b - dot(U, x))
        
    return x

def main (argv):

    AI = array([[5,2,1],[2,4,1],[2,2,4]])
    bI = [0,2,1]
    x = [1,1,1]
    n = 5

    print "(I):"
    pprint(AI)

    bol = sassenfeld(AI)
    if bol:
        print "\n A matriz (I) é convergente por Sassenfeld."
        res = gauss(AI,bI,x,n)

        print "x para (I): "
        pprint(res)  
    
    else:
        print "\n A matriz (I) não é convergente por Sassenfeld."
    
    
    AII = array([[5,4,1],[3,4,1],[3,3,6]])
    bII = [2,2,-9]
    x = [1,1,1]
    n = 5

    print "(II):"
    pprint(AII)

    bol = sassenfeld(AII)
    if bol:
        print "\n A matriz (II) é convergente por Sassenfeld."
        res = gauss(AII,bII,x,n)

        print "x para (II): "
        pprint(res)  
    
    else:
        print "\n A matriz (II) não é convergente por Sassenfeld."
    
if __name__ == '__main__':
    main(sys.argv[1:])