# Step 4: fast against slow

**English** · [Dansk](Step-4-Fast-vs-Slow-da) · [Bahasa Malaysia](Step-4-Fast-vs-Slow-ms)

`@speed_calc_decorator` above both functions of the assignment gives the expected output:

```python
@speed_calc_decorator
def fast_function():
    for i in range(1_000_000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10_000_000):
        i * i
```

![Step 4: fast against slow](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-4-fast-vs-slow.png)

Run it with `python -m speed_calc`.

## What we gained

- One decorator times any number of functions; the timing code is written once.
- `slow_function` loops ten times as often as `fast_function`, so it takes about ten times as long. The numbers differ on every machine, but the ratio does not.
- A clean layout for a small exercise: `src/` for code, `tests/` for tests, `docs/` for documents, `constants.py` for constants, and Doxygen comments for the API.
