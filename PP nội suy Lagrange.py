import numpy as np

def lagrange_interpolation(x_points, y_points, x):
    def L(k, x):
        terms = [(x - x_points[j]) / (x_points[k] - x_points[j]) for j in range(len(x_points)) if j != k]
        return np.prod(terms)

    y = sum(y_points[k] * L(k, x) for k in range(len(x_points)))
    return y

# Example usage:
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 0, 5])

# Interpolate at x = 1.5
x = 5
y = lagrange_interpolation(x_points, y_points, x)
print(f"The interpolated value at x = {x} is y = {y}")