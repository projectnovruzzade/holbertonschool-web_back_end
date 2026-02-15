#!/usr/bin/env python3
"""
  this is external
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int  | float]) -> float:
    """
    this is internal
    """
    return float(sum(mxd_lst))
