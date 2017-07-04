# -*- coding: latin-1 -*-
"""
* Resolução do exercício 5.2 (Neide Maria B. Franco. Cálculo Numérico. Pearson. 1ª Edição.)
* 
* Executado como : franco_5-2.py.py 
*
* Parâmetros usados para teste:
*                              python franco_5-2.py.py
*
"""

import sys
import numpy as np
from scipy.linalg import solve


def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    m = len(x)
    x_novo = x[1]
    for i in range(n):
        # x^(k+1) = L*^(-1)*(b-Ux^(k))
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))

        x_antigo = x_novo
        for k in range(m):
            if x[k] > x_novo:
                x_novo = x[k]
        t = abs(x_novo - x_antigo)/abs(x_novo)
        if(t < 0.001):
            break
    return x

def main (argv):
    A = np.array([[20,-10,-4],[-10,25,-5],[-4,5,10]])
    b = [26,0,7]
    x = [1, 1, 1]
    n = 20
    print gauss(A, b, x, n)
    


if __name__ == '__main__':
    main(sys.argv[1:])