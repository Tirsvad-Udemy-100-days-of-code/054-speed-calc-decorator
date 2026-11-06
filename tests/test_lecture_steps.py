"""Tests for the lecture steps."""

import pytest

from speed_calc.lecture_steps import main


def test_step_1_prints_the_current_time(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["1"]) == 0
    assert float(capsys.readouterr().out) > 0


def test_step_2_announces_the_call_and_keeps_the_name(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["2"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines == [
        "calling fast_function",
        "name kept by functools.wraps: fast_function",
    ]


def test_step_3_prints_one_timing_line(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["3"]) == 0
    assert capsys.readouterr().out.startswith("fast_function run speed: ")


def test_step_4_prints_three_lines(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["4"]) == 0
    assert len(capsys.readouterr().out.splitlines()) == 3


def test_bad_step_number_is_refused(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["9"]) == 2
    assert "usage" in capsys.readouterr().out
