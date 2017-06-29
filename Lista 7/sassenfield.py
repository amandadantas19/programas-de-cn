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
from numpy import array, zeros, diag, diagflat, dot,linalg

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
  
def main (argv):

    A = array([[10,-1,1],[1,-10,-1],[1,1,-5]])
    
    print "A:"
    pprint(A)

    bol = sassenfeld(A)
    if bol:
        print "\n A matriz A é convergente."
    else:
        print "\n A matriz A não é convergente."

if __name__ == '__main__':
    main(sys.argv[1:])