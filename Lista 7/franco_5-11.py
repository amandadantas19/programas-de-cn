# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5.11 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_5-11.py 
*
* Parâmetros usados para teste:
*                              python franco_5-11.py
*
"""

import sys
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot,linalg,tril

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

    A = array([[50,-1,4],[1,50,9],[2,-3,-50]])
    b = [45,42,49]
    x = [1,1,1]
    n = 3

    print "A:"
    pprint(A)

    bol = sassenfeld(A)
    if bol:
        print "\n A matriz A é convergente por Sassenfeld."
    else:
        print "\n A matriz A não é convergente por Sassenfeld."
    
    res = gauss(A,b,x,n)

    print "x: "
    pprint(res)  

    
if __name__ == '__main__':
    main(sys.argv[1:])