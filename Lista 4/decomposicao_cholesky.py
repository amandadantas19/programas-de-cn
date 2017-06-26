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
import math
import sys
import pprint

 
def cholesky(A):

    L = [[0.0] * len(A) for _ in xrange(len(A))]

    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = math.sqrt(A[i][i] - s) if (i == j) else \
                      (1.0 / L[j][j] * (A[i][j] - s))
    return L

def main (argv):
    m1 = [[4, 2, -4],
          [2, 10,  4],
          [-4,  4, 9]]
    g = cholesky(m1)
    gt = zip(*g)

    print "M1:"
    pprint.pprint(m1)
    print "G:"
    pprint.pprint(g)
    print "Gt:"/
    pprint.pprint(gt)

if __name__ == '__main__':
    main(sys.argv[1:])