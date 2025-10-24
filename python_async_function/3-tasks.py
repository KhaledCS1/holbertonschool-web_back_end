#!/usr/bin/env python3
"""
Creates and returns an asyncio.Task for the wait_random coroutine.

Args:
    max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

Returns:
    asyncio.Task: The created asyncio task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Creates an asyncio.Task that runs wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
    
