#!/usr/bin/env python3
"""
Coroutine that yields a random number between 0 and 10, ten times,
with a 1-second delay between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields a random float between 0 and 10 every second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
