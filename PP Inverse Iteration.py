import numpy as np

def inverse_iteration(A, mu, num_iterations=1000, tolerance=1e-10):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    
    # Initial guess for the eigenvector
    b_k = np.random.rand(n)
    
    # Shifted matrix
    A_shifted = A - mu * np.eye(n)
    
    for _ in range(num_iterations):
        # Solve (A - mu*I) * y = b_k
        try:
            y_k = np.linalg.solve(A_shifted, b_k)
        except np.linalg.LinAlgError:
            raise ValueError("Matrix A_shifted is singular")

        # Re-normalize the vector
        y_k_norm = np.linalg.norm(y_k)
        b_k = y_k / y_k_norm
        
        # Rayleigh quotient for eigenvalue approximation
        mu = np.dot(b_k.T, np.dot(A, b_k))
        
        # Check for convergence
        if np.linalg.norm(np.dot(A, b_k) - mu * b_k) < tolerance:
            break
    
    eigenvalue = mu
    eigenvector = b_k
    
    return eigenvalue, eigenvector

# Example usage:
A = np.array([[4, 1],
              [2, 3]], dtype=float)
mu_initial = 2.5  # Initial guess for eigenvalue

eigenvalue, eigenvector = inverse_iteration(A, mu_initial)
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)