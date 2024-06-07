import numpy as np

def divided_diff(x_points, y_points):
    n = len(y_points)
    coef = np.zeros([n, n])
    coef[:, 0] = y_points

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_points[i + j] - x_points[i])

    return coef[0, :]

def newton_interpolation(x_points, y_points, x):
    coef = divided_diff(x_points, y_points)
    n = len(coef)
    y = coef[0]
    newton_poly = 1.0

    for i in range(1, n):
        newton_poly *= (x - x_points[i - 1])
        y += coef[i] * newton_poly

    return y

# Example usage:
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 0, 5])

# Interpolate at x = 1.5
x = 1.5
y = newton_interpolation(x_points, y_points, x)
print(f"The interpolated value at x = {x} is y = {y}")