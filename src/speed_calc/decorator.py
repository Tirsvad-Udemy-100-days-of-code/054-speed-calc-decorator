"""!
@file decorator.py
@brief The speed calc decorator: prints how long a function takes to run.
"""

import functools
import time
from collections.abc import Callable
from typing import Any  # Any: a decorator must accept the arguments of any function

from speed_calc.constants import RESULT_TEMPLATE


def make_speed_calc_decorator(
    clock: Callable[[], float] = time.time,
    output: Callable[[str], None] = print,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """!
    @brief Build a speed calc decorator with its own clock and output.

    Tests pass a fake clock, so they never depend on real elapsed time.

    @param clock Returns the current time in seconds.
    @param output Receives the result line.
    @return A decorator that times the function it wraps.
    """

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = clock()
            result = function(*args, **kwargs)
            seconds = clock() - start
            output(RESULT_TEMPLATE.format(name=function.__name__, seconds=seconds))
            return result

        return wrapper

    return decorator


def speed_calc_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
    """!
    @brief Print the seconds that the decorated function takes to run.

    Use it as `@speed_calc_decorator` above a function definition.

    @param function The function to time.
    @return A wrapper that behaves like @p function and prints its run time.
    """
    return make_speed_calc_decorator()(function)
