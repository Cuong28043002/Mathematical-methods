import numpy as np

def jacobi(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    x_new = np.zeros_like(b, dtype=np.double)

    for k in range(max_iterations):
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            break
        
        x = x_new.copy()
        
    return x

# Example usage:
A = np.array([[10, 1, 1],
              [1, 10, 1],
              [1, 1, 10]], dtype=float)
b = np.array([6, 6, 6], dtype=float)

solution = jacobi(A, b)
print("Solution:", solution)