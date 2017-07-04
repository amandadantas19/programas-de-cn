# -*- coding: latin-1 -*-
"""
* Resolução do método da Resolução de Sistemas Triangulares Superiores
* 
* Executado como : sistema_triangular_superior.py 
*
* Parâmetros usados para teste:
*                              python sistema_triangular_superior.py
*
"""
import math
import sys
import pprint
import numpy as np

def triangular_superior (U,b):
    n = np.size(b)
    x = []
    a = 0.
    while a<n:
        x.append(0.)
        a = a +1
    
    x[n-1] = b[n-1]/U[n-1][n-1]
    i = n - 1
    while i >= 0:
        s = b[i]
        j = i +1 
        while j < n:
            s = s - U[i][j]*x[j]
            j = j + 1
        x[i] = s/U[i][i]
        i = i -1
    
    return x

def main (argv):
    U = [[5.,2.,1.],
        [0.,-1/5.,17/5.],
        [0.,0.,13.]]

    b = [0.,-7.,-26.]

    res = triangular_superior(U,b)
    res = ["%.2f" % r for r in res]
    print "X:"
    pprint.pprint(res)

if __name__ == '__main__':
    main(sys.argv[1:])