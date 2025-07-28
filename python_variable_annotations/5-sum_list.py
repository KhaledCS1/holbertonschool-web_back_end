#!/usr/bin/env python3
"""
This module provides a function to compute the sum of a list
of floating-point numbers using type annotations.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all the floating-point numbers in the input list.

    Parameters:
    input_list (List[float]): A list of float numbers to be summed.

    Returns:
    float: The total sum of the numbers in the list.
    """
    return sum(input_list)
