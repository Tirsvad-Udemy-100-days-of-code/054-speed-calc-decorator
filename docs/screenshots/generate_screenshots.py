"""Render the real output of each lecture step to a PNG file.

Dev-only tool (needs Pillow, installed by `pip install -e ".[dev]"`). It runs
each step in-process, captures its output and draws it as a terminal image, so no
screen is captured and the desktop is never touched.

Usage, from the project root:  python docs/screenshots/generate_screenshots.py
"""

import contextlib
import io
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from speed_calc.__main__ import main as speed_calc_main
from speed_calc.lecture_steps import main as lecture_steps_main

OUTPUT_DIR = Path(__file__).resolve().parent
ROOT = OUTPUT_DIR.parent.parent

# (file name, command shown in the prompt, lecture step to run; None = the program)
SHOTS = [
    ("step-1-current-time.png", "python -m speed_calc.lecture_steps 1", ["1"]),
    ("step-2-decorator-skeleton.png", "python -m speed_calc.lecture_steps 2", ["2"]),
    ("step-3-timing-wrapper.png", "python -m speed_calc.lecture_steps 3", ["3"]),
    ("step-4-fast-vs-slow.png", "python -m speed_calc", None),
]

BACKGROUND, FOREGROUND, PROMPT = "#1e1e2e", "#cdd6f4", "#a6e3a1"
FONT_CANDIDATES = [
    "C:/Windows/Fonts/consola.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/System/Library/Fonts/Menlo.ttc",
]


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def run(step: list[str] | None) -> str:
    """Run a step in this process and return what it printed."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        if step is None:
            speed_calc_main()
        else:
            lecture_steps_main(step)
    return buffer.getvalue().strip()


def render(path: Path, command: str, output: str) -> None:
    font = load_font(20)
    lines = [f"$ {command}", *output.splitlines()]
    width = int(max(font.getlength(line) for line in lines)) + 48
    height = 28 * len(lines) + 48
    image = Image.new("RGB", (max(width, 640), height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    for index, line in enumerate(lines):
        colour = PROMPT if index == 0 else FOREGROUND
        draw.text((24, 24 + 28 * index), line, font=font, fill=colour)
    image.save(path)


def main() -> None:
    for name, command, step in SHOTS:
        render(OUTPUT_DIR / name, command, run(step))
        print("wrote", name)


if __name__ == "__main__":
    main()
