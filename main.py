import numpy as np


"""
Returns a numpy array of the rows of A such that Ax = b
"""
def getBasis(A, b, x, m, n):
    #first find basis formed by the current BFS
    Ax = A @ x # produces an m x 1 vector
    tight = (Ax == b)
    basis = []
    nonbasis = []
    for i in range(m):
        if tight[i]:
            basis.append(i)
        else:
            nonbasis.append(i)
    return (np.array(basis), np.array(nonbasis))


"""
Input
    A: m x n matrix A
    b: 1 x m vector b
    c: 1 x n vector c
    x: 1 x n vector representing a BFS
    m: real number
    n: real number
Requires:
    {x: Ax <= b} is pointed
    All BFS are non-degenerate, meaning there are n tight linearly independent
        constraints at each BFS.
"""
def solve(A, b, c, x, m, n):
    while True:
        # first find basis formed by the current BFS
        basis, nonbasis = getBasis(A, b, x, m, n) 
        A_basis = A[basis]
        A_nonbasis = A[nonbasis]
        A_basis_inv = np.linalg.inv(A_basis) # should be invertible since A nondegenerate
        opt_condition = np.transpose(A_basis_inv) @ c
        optimal = True
        for j in range(n):
            if opt_condition[j] < 0:
                optimal = False
                d = -1 * (A_basis_inv[:,j])
                unbounded_condition = A_nonbasis @ d
                distancelist = []
                for i in range(m - n):
                    if unbounded_condition[i] > 0:
                        index = nonbasis[i]
                        distancelist.append((b[index] - A[index] @ x)
                                            / unbounded_condition[i])

                if len(distancelist) == 0:
                    raise("unbounded LP")
                else:
                    theta = min(distancelist)
                    break
        if optimal:
            return(x)
        else:
            x = x + theta * d


    """
    x = A_b_inverse * b_b
    if A_n * x < b_n:
        it is a BFS
        if A_b_inverse_transpose * c >= 0 we are optimal
    """



if __name__ == "__main__":
    I2 = np.array([[1,0],[0,1],[0,-1]])
    b = np.array([2,3,0])
    c = np.array([1,1])
    x = np.array([2,0])
    m = 3
    n = 2
    answer = solve(I2, b, c, x, m, n) # solution should be [2,3]
    print(answer)