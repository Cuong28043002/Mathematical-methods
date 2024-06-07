def bisection_method(f, a, b, tol):
    """
    Solve f(x) = 0 using the Bisection method.

    Parameters:
    f: the function for which we want to find a root
    a: the lower bound of the interval
    b: the upper bound of the interval
    tol: the tolerance for the solution

    Returns:
    The approximate root of f(x) = 0
    """
    if f(a) * f(b) > 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint  # The midpoint is the root
        elif f(a) * f(midpoint) < 0:
            b = midpoint  # The root is in the left half
        else:
            a = midpoint  # The root is in the right half

    return (a + b) / 2.0

# Example usage
def example_function(x):
    return x**3 - x - 2  # Example function f(x) = x^3 - x - 2

a = 1.0  # Lower bound of the interval
b = 2.0  # Upper bound of the interval
tol = 0.2  # Tolerance for the solution

root = bisection_method(example_function, a, b, tol)
print(f"The root is approximately: {root}")