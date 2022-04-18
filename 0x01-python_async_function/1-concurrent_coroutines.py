#!/usr/bin/env python3
"""takes in 2 int arguments (in this order): n and max_delay and
spawns wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values)
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """spawns wait_random n times with the specified max_delay and return lst"""
    waitList = [wait_random(max_delay) for i in range(n)]
    spawnList = asyncio.as_completed(waitList)
    spawnList = [await i for i in spawnList]
    return spawnList
