def runge_kutta_method(f, x0, y0, h, n):
    """
    Solve a first-order ordinary differential equation using the 4th order Runge-Kutta method.

    Parameters:
    f: the function defining the ODE dy/dx = f(x, y)
    x0: the initial value of x
    y0: the initial value of y at x0
    h: the step size
    n: the number of steps

    Returns:
    Two lists containing the x and y values of the solution
    """
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_values.append(x + h)
        y_values.append(y_next)
    
    return x_values, y_values

# Example usage
def f(x, y):
    return x * y  # Example ODE: dy/dx = x * y

x0 = 0  # initial value of x
y0 = 1  # initial value of y at x0
h = 0.1  # step size
n = 10  # number of steps

x_values, y_values = runge_kutta_method(f, x0, y0, h, n)
for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")