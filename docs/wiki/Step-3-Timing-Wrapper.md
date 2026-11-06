# Step 3: the timing wrapper

**English** · [Dansk](Step-3-Timing-Wrapper-da) · [Bahasa Malaysia](Step-3-Timing-Wrapper-ms)

The wrapper reads the clock before and after the call and prints the difference:

```python
start = clock()
result = function(*args, **kwargs)
seconds = clock() - start
output(RESULT_TEMPLATE.format(name=function.__name__, seconds=seconds))
return result
```

![Step 3: the timing wrapper](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-3-timing-wrapper.png)

Run it with `python -m speed_calc.lecture_steps 3`.

## What we gained

- A decorator can run code before and after the function without changing the function.
- The wrapper returns the function's result, so the decorated function still works as before.
- `make_speed_calc_decorator(clock, output)` takes the clock and the output as parameters. The tests give it a fake clock, so they check exact values and never wait for real time.
- The text format lives in `constants.py`, the one place for constants.
