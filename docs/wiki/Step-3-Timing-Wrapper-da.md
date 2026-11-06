# Trin 3: tidtagnings-wrapperen

[English](Step-3-Timing-Wrapper) · **Dansk** · [Bahasa Malaysia](Step-3-Timing-Wrapper-ms)

Wrapperen aflæser uret før og efter kaldet og udskriver forskellen:

```python
start = clock()
result = function(*args, **kwargs)
seconds = clock() - start
output(RESULT_TEMPLATE.format(name=function.__name__, seconds=seconds))
return result
```

![Step 3: the timing wrapper](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-3-timing-wrapper.png)

Kør den med `python -m speed_calc.lecture_steps 3`.

## Hvad vi lærte

- En dekorator kan køre kode før og efter funktionen uden at ændre funktionen.
- Wrapperen returnerer funktionens resultat, så den dekorerede funktion stadig virker som før.
- `make_speed_calc_decorator(clock, output)` tager uret og outputtet som parametre. Testene giver den et falsk ur, så de kontrollerer præcise værdier og aldrig venter på rigtig tid.
- Tekstformatet ligger i `constants.py`, det ene sted for konstanter.
