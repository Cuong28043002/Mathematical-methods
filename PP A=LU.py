import numpy as np

def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        
        L[i, i] = 1  # Diagonal as 1

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    
    return L, U

# Example usage:
A = np.array([[4, 3, 2, 1],[3, 7, 2, 5],[2, 2, 5, 3],[1, 5, 3, 10]], dtype=float)

L, U = lu_decomposition(A)
print("L:\n", L)
print("U:\n", U)