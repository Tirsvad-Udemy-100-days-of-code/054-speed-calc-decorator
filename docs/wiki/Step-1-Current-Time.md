# Step 1: the current time

**English** · [Dansk](Step-1-Current-Time-da) · [Bahasa Malaysia](Step-1-Current-Time-ms)

The starting code of the lecture prints the current time:

```python
import time

print(time.time())  # seconds since Jan 1st, 1970
```

![Step 1: the current time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-1-current-time.png)

Run it with `python -m speed_calc.lecture_steps 1`. Run it again a little later and the number is larger.

## What we gained

- `time.time()` returns the seconds since January 1st, 1970 as a float.
- The difference between two readings is a duration in seconds: second run minus first run.
- That difference is all a timer needs. The next steps put it inside a decorator.
