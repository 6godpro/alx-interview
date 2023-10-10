#!/usr/bin/python3
"""
    This module contains a function that finds the minimum
    operation to perform a specific task.
"""


def largestFactor(n: int) -> int:
    ''' Returns the largest factor of n. '''
    if n % 2 == 0:
        return n // 2
    for i in range(n // 3, 0, -1):
        if n % i == 0:
            break
    return 1 if n == 1 else i


def minOperations(n: int) -> int:
    '''
        In a text file, there is a single character H.
        Your text editor can execute only two operations
        in this file: Copy All and Paste. Given a number n,
        write a method that calculates the fewest number of
        operations needed to result in exactly n H characters
        in the file.

        Example:
        n = 9

        H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
        Paste => HHHHHH => Paste => HHHHHHHHH

        Number of operations: 6
    '''
    if n <= 1 or n == float('inf'):
        return 0
    value = largestFactor(n)
    return n // value + minOperations(value)
