# Persediaan

[English](Setup) · [Dansk](Setup-da) · **Bahasa Malaysia**

## Apa yang anda perlukan

Python 3.13 atau lebih baharu dan `git`. Program ini tidak mempunyai kebergantungan masa jalan. `pytest` hanya diperlukan untuk ujian.

## Cipta dan gunakan `.venv` setempat

Persekitaran maya mengasingkan pakej projek daripada bahagian lain sistem anda. Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Naik taraf pip dan pasang projek bersama alat ujiannya:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Keluar daripada persekitaran dengan `deactivate`.

## Jalankan dan uji

```bash
python -m speed_calc
python -m pytest
```

Jalankan satu langkah kuliah secara berasingan dengan `python -m speed_calc.lecture_steps N` (N ialah 1 hingga 4).

## Apa yang kita peroleh

- Persediaan yang boleh diulang: sesiapa sahaja boleh mencipta semula persekitaran yang sama dengan tiga arahan.
- Tabiat menyimpan pakej projek dalam `.venv` tersendiri, yang diabaikan oleh git.
