import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Example data points
x_points = np.array([0, 1, 2, 3, 4, 5])
y_points = np.array([0, 1, 0, 1, 0, 1])

# Create a cubic spline interpolation of the data
cs = CubicSpline(x_points, y_points)

# Values to interpolate
x = np.linspace(0, 5, 100)
y = cs(x)

# Plot the result
plt.plot(x_points, y_points, 'o', label='data points')
plt.plot(x, y, label='cubic spline')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.show()