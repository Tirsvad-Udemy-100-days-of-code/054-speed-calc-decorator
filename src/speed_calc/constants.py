"""!
@file constants.py
@brief Constants used by the speed calc package.
"""

## Number of loop iterations of fast_function.
FAST_ITERATIONS: int = 1_000_000

## Number of loop iterations of slow_function.
SLOW_ITERATIONS: int = 10_000_000

## Line format printed by the decorator: function name, then seconds.
RESULT_TEMPLATE: str = "{name} run speed: {seconds}s"
