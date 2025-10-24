#!/usr/bin/env python3
"""
Collects 10 random numbers from the async_generator using async comprehension.

This coroutine asynchronously iterates over async_generator
and returns a list containing 10 random float values.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random float values between 0 and 10.
    """
    return [value async for value in async_generator()]
