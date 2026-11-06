# Step 2: the decorator skeleton

**English** · [Dansk](Step-2-Decorator-Skeleton-da) · [Bahasa Malaysia](Step-2-Decorator-Skeleton-ms)

A decorator is a function that takes a function and returns another function. This skeleton only announces the call:

```python
def skeleton(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"calling {function.__name__}")
        return function(*args, **kwargs)

    return wrapper
```

![Step 2: the decorator skeleton](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-2-decorator-skeleton.png)

Run it with `python -m speed_calc.lecture_steps 2`.

## What we gained

- Functions are values: you can pass them to other functions and return them.
- The inner `wrapper` is a closure; it remembers `function` after `skeleton` has returned.
- `*args, **kwargs` let the wrapper accept the arguments of any function and pass them on.
- `functools.wraps` keeps the original name and docstring, so the decorated function still says `fast_function`.
- `@name` above a function is shorthand for `function = name(function)`.
