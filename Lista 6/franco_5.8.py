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
from scipy.linalg import solve

def jacobi(A,b,N=25,x=None):
    
    #Cria um chute inicial se necessário                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

                                                                                                                                                                         
    D = diag(A)
    R = A - diagflat(D)

    # Itera por N vezes                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

def main (argv):

    A = array([[10,   0,  0, 100,  0, 0],
               [10,-100,  0,   0,100, 0],
               [ 0,   0,100,-100,  0, 0],
               [ 1,   1,  0,   0,  0,-1],
               [-1,   0,  0,   1,  1, 0],
               [ 0,   1, -1,   0,  1, 0]])

    b = array([20,0,0,0,0,0])

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