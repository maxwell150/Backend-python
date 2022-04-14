#!/usr/bin/env python3
"""complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return func that multiplies'''
    def multiply(multiple: float) -> float:
        return multiple * multiplier
    return multiply
