#!/usr/bin/env python3
"""
okay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    ok
    """
    rndm = random.random() * max_delay
    await asyncio.sleep(rndm)
    return rndm
