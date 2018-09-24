# Simplike

An algorithm based on the simplex method for solving linear programs. Unlike the standard simplex method, which works on linear programs in standard equality form (Ax = b, x >= 0), this method works on polyhedra of the form Ax <= b.

I developed the algorithm while taking an Introduction to Optimization class in order to better understand the Simplex algorithm.

The algorithm is similar to the Simplex algorithm in its structure:

We start with a basic feasible solution (BFS).
At each iteration of the algorithm we check if the current BFS is optimal.
If it is not optimal, we either move to a better BFS or say that the problem is unbounded.

The differences lie in the details of implementing the above steps.
