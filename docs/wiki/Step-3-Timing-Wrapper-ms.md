# Langkah 3: pembungkus pemasaan

[English](Step-3-Timing-Wrapper) · [Dansk](Step-3-Timing-Wrapper-da) · **Bahasa Malaysia**

Pembungkus membaca jam sebelum dan selepas panggilan, lalu mencetak perbezaannya:

```python
start = clock()
result = function(*args, **kwargs)
seconds = clock() - start
output(RESULT_TEMPLATE.format(name=function.__name__, seconds=seconds))
return result
```

![Step 3: the timing wrapper](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-3-timing-wrapper.png)

Jalankannya dengan `python -m speed_calc.lecture_steps 3`.

## Apa yang kita peroleh

- Sebuah decorator boleh menjalankan kod sebelum dan selepas fungsi tanpa mengubah fungsi itu.
- Pembungkus memulangkan hasil fungsi, jadi fungsi yang didekorasi masih berfungsi seperti dahulu.
- `make_speed_calc_decorator(clock, output)` menerima jam dan output sebagai parameter. Ujian memberinya jam palsu, jadi ia menyemak nilai yang tepat dan tidak pernah menunggu masa sebenar.
- Format teks terletak dalam `constants.py`, satu-satunya tempat untuk pemalar.
