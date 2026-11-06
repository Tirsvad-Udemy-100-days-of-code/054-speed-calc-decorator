# Trin 2: dekoratorens skelet

[English](Step-2-Decorator-Skeleton) · **Dansk** · [Bahasa Malaysia](Step-2-Decorator-Skeleton-ms)

En dekorator er en funktion, der tager en funktion og returnerer en anden funktion. Dette skelet melder blot kaldet:

```python
def skeleton(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"calling {function.__name__}")
        return function(*args, **kwargs)

    return wrapper
```

![Step 2: the decorator skeleton](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-2-decorator-skeleton.png)

Kør den med `python -m speed_calc.lecture_steps 2`.

## Hvad vi lærte

- Funktioner er værdier: du kan give dem videre til andre funktioner og returnere dem.
- Den indre `wrapper` er en closure; den husker `function`, efter at `skeleton` er returneret.
- `*args, **kwargs` lader wrapperen tage imod argumenterne fra enhver funktion og give dem videre.
- `functools.wraps` bevarer det oprindelige navn og docstring, så den dekorerede funktion stadig hedder `fast_function`.
- `@name` over en funktion er en genvej til `function = name(function)`.
