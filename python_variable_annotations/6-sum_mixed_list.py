#!/usr/bin/env python3
"""
  this is external
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this is internal
    """
    return float(sum(mxd_lst))
