def fixed_point_iteration(g, x0, tol, max_iter):
    """
    Solve x = g(x) using the Fixed Point Iteration method.

    Parameters:
    g: the function g(x) such that x = g(x)
    x0: the initial guess
    tol: the tolerance for the solution
    max_iter: the maximum number of iterations

    Returns:
    The approximate fixed point of g(x)
    """
    x = x0
    for i in range(max_iter):
        x_next = g(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    raise ValueError("Fixed Point Iteration did not converge within the maximum number of iterations")

# Example usage
def g(x):
    return (x**2 + 2) / 3  # Example function rearranged from x^3 - x - 2 = 0 to x = g(x)

x0 = 1.5  # Initial guess
tol = 1e-5  # Tolerance for the solution
max_iter = 100  # Maximum number of iterations

root = fixed_point_iteration(g, x0, tol, max_iter)
print(f"The fixed point is approximately: {root}")