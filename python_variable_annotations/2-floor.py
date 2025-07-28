#!/usr/bin/env python3
"""
This module provides a utility function for mathematical
operations using type annotations.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    The floor of a number is the greatest integer less than or equal to it.

    Parameters:
    n (float): A floating-point number.

    Returns:
    int: The floor value of the number.
    """
    return math.floor(n)
