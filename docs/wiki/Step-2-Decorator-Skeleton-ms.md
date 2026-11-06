# Langkah 2: rangka decorator

[English](Step-2-Decorator-Skeleton) · [Dansk](Step-2-Decorator-Skeleton-da) · **Bahasa Malaysia**

Decorator ialah fungsi yang menerima sebuah fungsi dan memulangkan fungsi lain. Rangka ini hanya mengumumkan panggilan:

```python
def skeleton(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"calling {function.__name__}")
        return function(*args, **kwargs)

    return wrapper
```

![Step 2: the decorator skeleton](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator/raw/branch/main/docs/screenshots/step-2-decorator-skeleton.png)

Jalankannya dengan `python -m speed_calc.lecture_steps 2`.

## Apa yang kita peroleh

- Fungsi ialah nilai: anda boleh menghantarnya kepada fungsi lain dan memulangkannya.
- `wrapper` di dalam ialah satu closure; ia mengingati `function` selepas `skeleton` selesai dipulangkan.
- `*args, **kwargs` membolehkan pembungkus menerima argumen bagi sebarang fungsi dan meneruskannya.
- `functools.wraps` mengekalkan nama dan docstring asal, jadi fungsi yang didekorasi masih menyebut `fast_function`.
- `@name` di atas sebuah fungsi ialah singkatan bagi `function = name(function)`.
