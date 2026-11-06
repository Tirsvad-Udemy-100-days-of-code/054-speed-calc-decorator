"""!
@file lecture_steps.py
@brief The four lecture steps, each runnable on its own.

Run one with `python -m speed_calc.lecture_steps N` (N is 1 to 4).
"""

import functools
import sys
import time
from collections.abc import Callable
from typing import Any

from speed_calc.decorator import make_speed_calc_decorator
from speed_calc.demo_functions import fast_function

## The undecorated fast_function; functools.wraps keeps it in `__wrapped__`.
_fast = fast_function.__wrapped__  # type: ignore[attr-defined]


def step_1() -> None:
    """!
    @brief Step 1: print the seconds since Jan 1st, 1970.
    """
    print(time.time())


def step_2() -> None:
    """!
    @brief Step 2: a decorator skeleton that only announces the call.
    """

    def skeleton(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"calling {function.__name__}")
            return function(*args, **kwargs)

        return wrapper

    skeleton(_fast)()
    print(f"name kept by functools.wraps: {skeleton(_fast).__name__}")


def step_3() -> None:
    """!
    @brief Step 3: the wrapper reads the clock before and after the call.
    """
    make_speed_calc_decorator()(_fast)()


def step_4() -> None:
    """!
    @brief Step 4: the finished program, fast_function against slow_function.
    """
    from speed_calc.__main__ import main

    main()


STEPS: dict[int, Callable[[], None]] = {1: step_1, 2: step_2, 3: step_3, 4: step_4}


def main(argv: list[str]) -> int:
    """!
    @brief Run the lecture step named in @p argv.
    @param argv Command line arguments without the program name.
    @return Exit code: 0 on success, 2 on a bad step number.
    """
    if len(argv) != 1 or not argv[0].isdigit() or int(argv[0]) not in STEPS:
        print("usage: python -m speed_calc.lecture_steps N  (N is 1 to 4)")
        return 2
    STEPS[int(argv[0])]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
