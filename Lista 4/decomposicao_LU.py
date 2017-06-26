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

 
def mult(M1, M2):

    truple = zip(*M2)

    return [[sum(em1*em2 for em1,em2 in zip(m1,m2)) for m2 in truple] for m1 in M1]
 
def permut(m):
    
    n = len(m)
    identidade = [[float(i == j) for i in xrange(n)] for j in xrange(n)]

    for j in xrange(n):
        row = max(xrange(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            identidade[j], identidade[row] = identidade[row], identidade[j]

    return identidade
 
def lu(A):
    
    n = len(A)

    L = [[0.0] * n for i in xrange(n)]
    U = [[0.0] * n for i in xrange(n)]

    p = permut(A)
    pA = mult(p, A)

    for j in xrange(n):

        L[j][j] = 1.0

        for i in xrange(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in xrange(i))
            U[i][j] = pA[i][j] - s1

        for i in xrange(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in xrange(j))
            L[i][j] = (pA[i][j] - s2) / U[j][j]

    return (L, U, p)

def main (argv):
    A = [[7,3,-1,2],[3,8,1,-4],[-1,1,4,-1],[2,-4,-1,6]]
    
    L,U,p = lu(A)

    print "A: "
    pprint.pprint(A)

    print "P: "
    pprint.pprint(p)

    print "L: "
    pprint.pprint(L)

    print "U: "
    pprint.pprint(U)


    """for part in lu(A):
        pprint(part, widentidadeth=19)
    print
    print
    B = [[11,9,24,2],[1,5,2,6],[3,17,18,1],[2,5,7,1]]
    for part in lu(B):
        pprint(part)
    print"""

if __name__ == '__main__':
    main(sys.argv[1:])
