#!/usr/bin/env python3
"""measures the total execution time for wait_n(n, max_delay), and returns 
total_time / n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """measure time exec of func wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

