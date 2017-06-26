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
from numpy import array, zeros, diag, diagflat, dot

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
        x = (b - dot(R,x)) / D
    return x

def main (argv):

    A = array([[2.0,1.0],[5.0,7.0]])
    b = array([11.0,13.0])
    guess = array([1.0,1.0])

    sol = jacobi(A,b,N=25,x=guess)

    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(sol)
if __name__ == '__main__':
    main(sys.argv[1:])