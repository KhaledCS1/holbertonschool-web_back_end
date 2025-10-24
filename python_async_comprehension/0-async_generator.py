#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.

The coroutine runs 10 times, waiting 1 second each time before yielding
a random float value.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random value between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
