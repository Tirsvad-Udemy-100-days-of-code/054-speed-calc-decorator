# Opsætning

[English](Setup) · **Dansk** · [Bahasa Malaysia](Setup-ms)

## Det skal du bruge

Python 3.13 eller nyere og `git`. Programmet har ingen afhængigheder ved kørsel. `pytest` skal kun bruges til testene.

## Opret og brug en lokal `.venv`

Et virtuelt miljø holder projektets pakker adskilt fra resten af dit system. Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Opgradér pip og installér projektet med dets testværktøjer:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Forlad miljøet med `deactivate`.

## Kør og test

```bash
python -m speed_calc
python -m pytest
```

Kør ét lektionstrin for sig med `python -m speed_calc.lecture_steps N` (N er 1 til 4).

## Hvad vi lærte

- En gentagelig opsætning: alle kan genskabe det samme miljø med tre kommandoer.
- En vane med at holde et projekts pakker i sin egen `.venv`, som git ignorerer.
