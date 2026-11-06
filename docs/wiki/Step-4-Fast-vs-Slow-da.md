# Trin 4: hurtig mod langsom

[English](Step-4-Fast-vs-Slow) · **Dansk** · [Bahasa Malaysia](Step-4-Fast-vs-Slow-ms)

`@speed_calc_decorator` over begge opgavens funktioner giver det forventede output:

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

Kør den med `python -m speed_calc`.

## Hvad vi lærte

- Én dekorator tager tid på et vilkårligt antal funktioner; tidtagningskoden skrives kun én gang.
- `slow_function` gennemløber sin løkke ti gange så mange gange som `fast_function`, så den tager cirka ti gange så lang tid. Tallene er forskellige på hver maskine, men forholdet er det ikke.
- En ren struktur til en lille øvelse: `src/` til kode, `tests/` til tests, `docs/` til dokumenter, `constants.py` til konstanter og Doxygen-kommentarer til API'et.
