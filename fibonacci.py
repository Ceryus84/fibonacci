"""
Aidan Butcher
CS 3450 - Algorithms & Data Structures
Demonstrates inefficient recursion vs efficient recursion with the
Fibonacci Sequence.
"""


def bad_fibonacci(n: int):
    """Return the nth Fibonacci number"""
    if n <= 1:
        return n
    return bad_fibonacci(n-2) + bad_fibonacci(n-1)


def good_fibonacci(n: int):
    """Return a pair of Fibonacci numbers, F(n) and F(n-1)"""
    if n <= 1:
        return (n, 0)
    (a, b) = good_fibonacci(n-1)
    return (a+b, a)


# Hasn't seemed to slow down despite reaching near recursion limit
print(good_fibonacci(35))
print(bad_fibonacci(35))  # Started to slow down near 35-40
