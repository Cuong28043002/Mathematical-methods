import numpy as np

def power_method(A, num_iterations=1000, tolerance=1e-10):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    
    # Initial guess for the eigenvector
    b_k = np.random.rand(n)
    
    for _ in range(num_iterations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Re-normalize the vector
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
        
        # Check for convergence
        if np.linalg.norm(np.dot(A, b_k) - b_k1_norm * b_k) < tolerance:
            break

    eigenvalue = b_k1_norm
    eigenvector = b_k
    
    return eigenvalue, eigenvector

# Example usage:
A = np.array([[4, 1],
              [2, 3]], dtype=float)

eigenvalue, eigenvector = power_method(A)
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)