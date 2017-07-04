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

def jacobi(A,b,N=25,x=None):
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x_novo = (b - dot(R,x)) / D
        erro = (linalg.norm(x - x_novo))/linalg.norm(x_novo)
        if erro < 0.01:
            return x_novo
        x = x_novo
    return x

def main (argv):

    A = array([[10,1,-1],[1,10,1],[2,-1,10]])
    b = array([10,12,11])
    guess = None

    sol = jacobi(A,b,N=25,x=guess)

    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(sol)
    
if __name__ == '__main__':
    main(sys.argv[1:])