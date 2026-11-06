"""Tests for the speed calc decorator; a fake clock replaces real time."""

from collections.abc import Callable

import pytest

from speed_calc.decorator import make_speed_calc_decorator


def make_clock(*times: float) -> Callable[[], float]:
    values = iter(times)
    return lambda: next(values)


def test_prints_function_name_and_elapsed_seconds() -> None:
    lines: list[str] = []
    decorate = make_speed_calc_decorator(make_clock(10.0, 12.5), lines.append)

    @decorate
    def work() -> None:
        pass

    work()

    assert lines == ["work run speed: 2.5s"]


def test_returns_the_result_of_the_function() -> None:
    decorate = make_speed_calc_decorator(make_clock(0.0, 1.0), lambda _: None)

    @decorate
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, b=3) == 5


def test_keeps_name_and_docstring() -> None:
    decorate = make_speed_calc_decorator(make_clock(0.0, 1.0), lambda _: None)

    @decorate
    def documented() -> None:
        """Doc."""

    assert documented.__name__ == "documented"
    assert documented.__doc__ == "Doc."


def test_default_decorator_prints_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    from speed_calc import speed_calc_decorator

    @speed_calc_decorator
    def quick() -> None:
        pass

    quick()

    out = capsys.readouterr().out
    assert out.startswith("quick run speed: ")
    assert out.endswith("s\n")
