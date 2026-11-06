# Langkah 1: masa semasa

[English](Step-1-Current-Time) · [Dansk](Step-1-Current-Time-da) · **Bahasa Malaysia**

Kod permulaan kuliah mencetak masa semasa:

```python
import time

print(time.time())  # seconds since Jan 1st, 1970
```

![Step 1: the current time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-1-current-time.png)

Jalankannya dengan `python -m speed_calc.lecture_steps 1`. Jalankan sekali lagi sebentar kemudian dan nombornya lebih besar.

## Apa yang kita peroleh

- `time.time()` memulangkan bilangan saat sejak 1 Januari 1970 sebagai float.
- Perbezaan antara dua bacaan ialah tempoh dalam saat: larian kedua tolak larian pertama.
- Perbezaan itu sahaja sudah cukup untuk sebuah pemasa. Langkah seterusnya meletakkannya di dalam decorator.
