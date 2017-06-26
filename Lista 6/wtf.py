from matrix import height

def gauss_seidel(m, x0=None, eps=1e-5, max_iteration=100):
  """
  Parameters
  ----------
  m  : list of list of floats : coefficient matrix
  x0 : list of floats : initial guess
  eps: float : error tolerance
  max_iteration: int
  
  Returns
  -------  
  list of floats
      solution to the system of linear equation
  
  Raises
  ------
  ValueError
      Solution does not converge
  """
  n  = len(m)
  x0 = [0] * n if x0 == None else x0
  x1 = x0[:]

  for __ in range(max_iteration):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j) 
      x1[i] = (m[i][n] + s) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1 
    x0 = x1[:]    
  raise ValueError('Solution does not converge')

def main (argv):

    A = array([[4,-1,0,-1,0,0],
               [-1,4,-1,0,-1,0],
               [0,-1, 4,0, 0,-1],
               [-1,0,0,4,-1,0],
               [0,-1,0,-1,4,-1],
               [0,0,-1,0,-1,4]])

    b = array([100,0,0,100,0,0])

    sol = gauss_seidel(A)

    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(sol)
    
if __name__ == '__main__':
    main(sys.argv[1:]