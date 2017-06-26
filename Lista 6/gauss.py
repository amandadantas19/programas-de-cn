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
import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
    	# x^(k+1) = L*^(-1)*(b-Ux^(k))
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        
    return x

def main (argv):
	A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
	b = [1.0, 2.0, 3.0]
	x = [1, 1, 1]

	n = 20

	print gauss(A, b, x, n)
	print solve(A, b)

if __name__ == '__main__':
    main(sys.argv[1:])