#!/usr/bin/env python3
"""
  this is external
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    ok
    """
    def multiply(value: float) -> float:
        """
         ok
        """
        return value * multiplier
    return multiply
