# Speed Calc Decorator

[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

En Python-dekorator, der måler, hvor mange sekunder en funktion er om at køre. Den er løsningen på en øvelse fra Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp*. Denne wiki forklarer, hvad hvert trin i lektionen lærte. [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-speed-calc-decorator) er den korte version.

Det forventede output fra det færdige program har denne form (tallene er forskellige på hver maskine):

```text
1695050908.1985211
fast_function run speed: 0.33974480628967285s
slow_function run speed: 2.9590742588043213s
```

| Side | Læs den, når du vil |
| --- | --- |
| [Opsætning](Setup-da) | Oprette en lokal `.venv`, køre programmet og køre testene |
| [Trin 1: det aktuelle tidspunkt](Step-1-Current-Time-da) | Lære, hvad `time.time()` returnerer, og hvordan man måler en varighed |
| [Trin 2: dekoratorens skelet](Step-2-Decorator-Skeleton-da) | Lære, hvad en dekorator er, og hvorfor `functools.wraps` er vigtig |
| [Trin 3: tidtagnings-wrapperen](Step-3-Timing-Wrapper-da) | Se, hvordan wrapperen tager tid på kaldet, og hvordan testene undgår rigtig tid |
| [Trin 4: hurtig mod langsom](Step-4-Fast-vs-Slow-da) | Samle det hele og læse resultatet |
