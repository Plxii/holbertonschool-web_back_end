#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays

