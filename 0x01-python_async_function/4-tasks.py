#!/usr/bin/env python3
"""new Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return lst """
    waitList = [task_wait_random(max_delay) for i in range(n)]
    spawnList = [await i for i in asyncio.as_completed(waitList)]
    return spawnList
