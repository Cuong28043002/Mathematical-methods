import math

def taylor_series_expansion(func, x0, n, x):
    """
    Calculate the Taylor series expansion of a function at a point.

    Parameters:
    func: the function to expand
    x0: the point at which to expand the function
    n: the number of terms in the Taylor series
    x: the point at which to evaluate the Taylor series

    Returns:
    The value of the Taylor series expansion at x
    """
    def derivative(f, x, order):
        """
        Calculate the nth derivative of a function at a point x.

        Parameters:
        f: the function to differentiate
        x: the point at which to evaluate the derivative
        order: the order of the derivative

        Returns:
        The nth derivative of f at x
        """
        h = 1e-5
        if order == 0:
            return f(x)
        elif order == 1:
            return (f(x + h) - f(x - h)) / (2 * h)
        else:
            return (derivative(f, x + h, order - 1) - derivative(f, x - h, order - 1)) / (2 * h)
    
    taylor_sum = 0
    for i in range(n):
        term = (derivative(func, x0, i) * (x - x0)**i) / math.factorial(i)
        taylor_sum += term
    
    return taylor_sum

# Example usage
func = math.sin  # sin(x)
x0 = math.pi / 4  # expansion point
n = 5  # number of terms in the Taylor series
x = math.pi / 3  # point at which to evaluate the Taylor series

approximation = taylor_series_expansion(func, x0, n, x)
print(f"The Taylor series approximation of sin(x) at x = {x} is {approximation}")