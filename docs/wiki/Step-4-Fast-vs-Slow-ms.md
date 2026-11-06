# Langkah 4: pantas lawan perlahan

[English](Step-4-Fast-vs-Slow) · [Dansk](Step-4-Fast-vs-Slow-da) · **Bahasa Malaysia**

`@speed_calc_decorator` di atas kedua-dua fungsi tugasan memberikan output yang dijangka:

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

Jalankannya dengan `python -m speed_calc`.

## Apa yang kita peroleh

- Satu decorator mengukur masa mana-mana bilangan fungsi; kod pemasaan ditulis sekali sahaja.
- `slow_function` mengulang sepuluh kali lebih banyak daripada `fast_function`, jadi ia mengambil masa kira-kira sepuluh kali lebih lama. Nombornya berbeza pada setiap mesin, tetapi nisbahnya tidak.
- Susun atur yang kemas untuk latihan kecil: `src/` untuk kod, `tests/` untuk ujian, `docs/` untuk dokumen, `constants.py` untuk pemalar, dan komen Doxygen untuk API.
