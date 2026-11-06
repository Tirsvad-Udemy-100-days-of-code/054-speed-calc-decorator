"""!
@file __init__.py
@brief Public API of the speed calc package.
"""

from speed_calc.decorator import make_speed_calc_decorator, speed_calc_decorator
from speed_calc.demo_functions import fast_function, slow_function

__all__ = [
    "fast_function",
    "make_speed_calc_decorator",
    "slow_function",
    "speed_calc_decorator",
]
