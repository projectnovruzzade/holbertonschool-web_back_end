#!/usr/bin/env python3
"""
  this is external
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        this is external
    """
    return (k, float(v * v))
