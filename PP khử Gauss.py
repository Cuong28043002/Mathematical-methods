import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    
    # Augment matrix A with vector b
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        # Find the pivot row
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        
        # Swap the current row with the pivot row
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            factor = Ab[k, i] / Ab[i, i]
            Ab[k, i:] -= factor * Ab[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:])) / Ab[i, i]
    
    return x

A = np.array([[1, 2, -3, -1], [3, 7, 1, 2],[4, 5, 9, 1],[2, 3, 2, -1]], dtype=float)
b = np.array([2, 5, 6, 2], dtype=float)

solution = gaussian_elimination(A, b)
print("Solution:", solution)
