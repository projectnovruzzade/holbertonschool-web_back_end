#!/usr/bin/env python3
"""
  this is external
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    ok
    """
    return [(i, len(i)) for i in lst]
