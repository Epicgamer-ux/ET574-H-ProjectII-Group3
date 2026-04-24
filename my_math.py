# my_math.py
# Group Member: Kristian
# Functions: factorial(x), floor(x), area_of_circle(r), is_perfect_number(n)


def factorial(x):
    """
    Function: factorial
    Purpose: Computes the factorial of a non-negative integer x (x!)
             without using the math module.
    Parameters: x (int) - a non-negative integer
    Returns: int - the factorial of x
    Raises: TypeError if x is not an integer
            ValueError if x is negative
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be a non-negative integer")
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def floor(x):
    """
    Function: floor
    Purpose: Returns the largest integer less than or equal to x,
             without using the math module.
    Parameters: x (float or int) - any real number
    Returns: int - the floor of x
    Raises: TypeError if x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if x >= 0:
        return int(x)
    else:
        truncated = int(x)
        return truncated if truncated == x else truncated - 1


def area_of_circle(r):
    """
    Function: area_of_circle
    Purpose: Computes the area of a circle given its radius,
             using an internal approximation of pi.
    Parameters: r (float or int) - the radius of the circle, must be >= 0
    Returns: float - the area of the circle (pi * r^2)
    Raises: TypeError if r is not a number
            ValueError if r is negative
    """
    if not isinstance(r, (int, float)):
        raise TypeError("r must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.141592653589793
    return pi * r * r


def is_perfect_number(n):
    """
    Function: is_perfect_number
    Purpose: Determines whether a number is a perfect number.
             A perfect number equals the sum of its proper divisors.
             Example: 6 = 1 + 2 + 3
    Parameters: n (int) - a positive integer
    Returns: bool - True if n is perfect, False otherwise
    Raises: TypeError if n is not an integer
            ValueError if n is less than 1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return False
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n