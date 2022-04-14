#!/usr/bin/env python3
"""Complex types-mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns sum of float'''
    return sum(mxd_lst)
