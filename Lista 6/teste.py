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
    A = np.array([[[10,   0,  0, 100,  0, 0],
               [10,-100,  0,   0,100, 0],
               [ 0,   0,100,-100,  0, 0],
               [ 1,   1,  0,   0,  0,-1],
               [-1,   0,  0,   1,  1, 0],
               [ 0,   1, -1,   0,  1, 0]]])
    b = [20,0,0,0,0,0]
    x = [1, 1,1,1,1,1]

    n = 20

    print gauss(A, b, x, n)
    print solve(A, b)

if __name__ == '__main__':
    main(sys.argv[1:])