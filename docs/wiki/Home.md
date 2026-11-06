# Speed Calc Decorator

**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

A Python decorator that measures how many seconds a function takes to run. It is the solution to a lecture exercise of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. This wiki explains what each lecture step taught. The [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator) is the short version.

The expected output of the finished program has this shape (the numbers differ on every machine):

```text
1695050908.1985211
fast_function run speed: 0.33974480628967285s
slow_function run speed: 2.9590742588043213s
```

| Page | Read when you want to |
| --- | --- |
| [Setup](Setup) | Create a local `.venv`, run the program and run the tests |
| [Step 1: the current time](Step-1-Current-Time) | Learn what `time.time()` returns and how to measure a duration |
| [Step 2: the decorator skeleton](Step-2-Decorator-Skeleton) | Learn what a decorator is and why `functools.wraps` matters |
| [Step 3: the timing wrapper](Step-3-Timing-Wrapper) | See how the wrapper times the call and how tests avoid real time |
| [Step 4: fast against slow](Step-4-Fast-vs-Slow) | Put it together and read the result |
