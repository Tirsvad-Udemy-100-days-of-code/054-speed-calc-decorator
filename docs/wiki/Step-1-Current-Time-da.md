# Trin 1: det aktuelle tidspunkt

[English](Step-1-Current-Time) · **Dansk** · [Bahasa Malaysia](Step-1-Current-Time-ms)

Lektionens startkode udskriver det aktuelle tidspunkt:

```python
import time

print(time.time())  # seconds since Jan 1st, 1970
```

![Step 1: the current time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-1-current-time.png)

Kør den med `python -m speed_calc.lecture_steps 1`. Kør den igen lidt senere, og tallet er større.

## Hvad vi lærte

- `time.time()` returnerer sekunderne siden 1. januar 1970 som et flydende tal (float).
- Forskellen mellem to aflæsninger er en varighed i sekunder: anden kørsel minus første kørsel.
- Den forskel er alt, en timer behøver. De næste trin lægger den ind i en dekorator.
