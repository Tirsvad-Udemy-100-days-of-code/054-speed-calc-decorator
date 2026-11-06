"""!
@file __main__.py
@brief Entry point: python -m speed_calc.
"""

import time

from speed_calc.demo_functions import fast_function, slow_function


def main() -> None:
    """!
    @brief Print the current time, then the run time of both functions.
    """
    print(time.time())  # seconds since Jan 1st, 1970
    fast_function()
    slow_function()


if __name__ == "__main__":
    main()
