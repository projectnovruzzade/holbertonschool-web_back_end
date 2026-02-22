#!/usr/bin/env python3
"""Module that runs multiple task_wait_random concurrently."""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
     oka
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
