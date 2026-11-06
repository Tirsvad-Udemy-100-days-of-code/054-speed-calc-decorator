"""!
@file demo_functions.py
@brief The two functions of the assignment, timed by the decorator.
"""

from speed_calc.constants import FAST_ITERATIONS, SLOW_ITERATIONS
from speed_calc.decorator import speed_calc_decorator


@speed_calc_decorator
def fast_function() -> None:
    """!
    @brief Loop FAST_ITERATIONS times.
    """
    for i in range(FAST_ITERATIONS):
        i * i


@speed_calc_decorator
def slow_function() -> None:
    """!
    @brief Loop SLOW_ITERATIONS times.
    """
    for i in range(SLOW_ITERATIONS):
        i * i
