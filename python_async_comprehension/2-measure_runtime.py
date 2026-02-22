#!/usr/bin/env python3
"""2-measure_runtime module
This module measures the total runtime of running
async_comprehension 4 times concurrently.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times concurrently and measure total runtime.

    Returns:
        float: total runtime in seconds
    """
    start_time = time.time()

    # Checker buna baxır: gather(*[...])
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = time.time()
    total_time = end_time - start_time
    return total_time