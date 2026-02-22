#!/usr/bin/env python3
"""
oka
"""

from 0-async_generator import async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """
    oka
    """
    return [i async for i in async_generator()]
