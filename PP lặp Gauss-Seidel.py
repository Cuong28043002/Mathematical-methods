import numpy as np

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            break                                                                                       
              
    return x

A = np.array([[2, 1, 2, 3],
              [3, 5, 1, 4],
              [3, 7, 8, 4],
              [1, 1, 3, 5]], dtype=float)
b = np.array([4, 7, 3, 12], dtype=float)

solution = gauss_seidel(A, b)
print("Solution:", solution)