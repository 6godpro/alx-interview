#!/usr/bin/python3
""""
This module contains a function that returns
a list of integers representing the Pascal's
triangle of a given number.
"""


def pascal_triangle(n):
    """Returns a list of integers representing
    the Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        temp = [1]
        for i in range(len(triangle[-1]) - 1):
            temp.append(triangle[-1][i] + triangle[-1][i + 1])
        temp.append(1)
        triangle.append(temp)

    return triangle
