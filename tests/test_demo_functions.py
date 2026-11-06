"""Tests for the assignment's functions and the entry point."""

import re

import pytest

from speed_calc import constants, fast_function, slow_function
from speed_calc.__main__ import main

LINE = r"(fast|slow)_function run speed: \d+(\.\d+)?(e-?\d+)?s"


def test_function_names_match_the_assignment() -> None:
    assert fast_function.__name__ == "fast_function"
    assert slow_function.__name__ == "slow_function"


def test_constants_hold_the_loop_sizes() -> None:
    assert constants.FAST_ITERATIONS == 1_000_000
    assert constants.SLOW_ITERATIONS == 10_000_000


def test_main_prints_time_then_fast_then_slow(
    capsys: pytest.CaptureFixture[str],
) -> None:
    main()

    lines = capsys.readouterr().out.splitlines()

    assert len(lines) == 3
    assert float(lines[0]) > 0
    assert re.fullmatch(LINE, lines[1]) and lines[1].startswith("fast_function")
    assert re.fullmatch(LINE, lines[2]) and lines[2].startswith("slow_function")
