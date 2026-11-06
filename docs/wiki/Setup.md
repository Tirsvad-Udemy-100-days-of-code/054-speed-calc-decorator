# Setup

**English** · [Dansk](Setup-da) · [Bahasa Malaysia](Setup-ms)

## What you need

Python 3.13 or newer and `git`. The program has no runtime dependencies. `pytest` is needed only for the tests.

## Create and use a local `.venv`

A virtual environment keeps the project's packages apart from the rest of your system. Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip and install the project with its test tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## Run and test

```bash
python -m speed_calc
python -m pytest
```

Run one lecture step on its own with `python -m speed_calc.lecture_steps N` (N is 1 to 4).

## What we gained

- A repeatable setup: anyone can recreate the same environment in three commands.
- A habit of keeping a project's packages in its own `.venv`, ignored by git.
