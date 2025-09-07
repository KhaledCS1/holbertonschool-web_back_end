#!/usr/bin/env python3
"""
Pagination Helper Functions Module

This module provides utility functions for calculating pagination indices.
Implements basic mathematical operations for page-based data retrieval.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indices for pagination.

    Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for the given pagination parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing (start_index, end_index).

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
