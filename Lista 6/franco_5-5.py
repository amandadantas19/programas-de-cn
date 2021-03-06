# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5.5 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_5-5.py.py 
*
* Parâmetros usados para teste:
*                              python franco_5-5.py.py
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

    A = array([[-4, 1, 0, 1, 0, 0, 0, 0, 0],
               [ 1,-4, 1, 0, 1, 0, 0, 0, 0],
               [ 0, 1,-4, 0, 0, 1, 0, 0, 0],
               [ 1, 0, 0,-4, 1, 0, 1, 0, 0],
               [ 0, 1, 0, 1,-4, 1, 0, 1, 0],
               [ 0, 0, 1, 0, 1,-4, 0, 0, 1],
               [ 0, 0, 0, 0, 1, 0,-4, 1, 0],
               [ 0, 0, 0, 0, 1, 0, 1,-4, 1],
               [ 0, 0, 0, 0, 0, 1, 0, 1,-4]])

    b = array([-50,-50,-150,0,0,-100,-50,-50,-150])

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