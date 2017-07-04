# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5.9 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_5-9.py 
*
* Parâmetros usados para teste:
*                              python franco_5-9.py
*
"""

import sys
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot,linalg

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
  
def main (argv):

    A = array([[1,-0.5,0],[-0.5,1,-0.5],[0,-0.5,1]])
    B = array([[1,0.5,0],[0.5,1,0.5],[0,0.5,1]])
    bol = converge_dominante(A)
    bol2 = converge_dominante(B)

    print "A:"
    pprint(A)

    if bol:
        print "\n A matriz A é convergente."
    else:
        print "\n A matriz A não é convergente."

    print "B:"
    pprint(B)

    if bol2:
        print "\n A matriz B é convergente."
    else:
        print "\n A matriz B não é convergente."

    
    
if __name__ == '__main__':
    main(sys.argv[1:])