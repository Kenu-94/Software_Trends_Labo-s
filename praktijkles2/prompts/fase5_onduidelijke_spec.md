# Fase 5 — Bewust falende specificatie

Deze prompt is **bewust slecht**. Het doel: de agent moet weigeren aannames te maken (dwz via `.clinerules`) en de student laten bijsturen.

---

## De vage requirement (geef deze aan de agent)

```text
Toon statistieken over de studenten.
```

**Verwachte reactie van de agent:** een verduidelijkende vraag, bijvoorbeeld "Welke statistieken?". Geen code.

Reageert de agent toch met code? Check dan of de regel "Maak GEEN aannames bij onduidelijke requirements" in `.clinerules` staat, en start een nieuwe sessie.

---

## De verduidelijking (info meegeven)

```text
Toon:
- gemiddelde
- mediaan
- minimum
- maximum
```

Daarna mag de agent verder:

```text
Pas specs/specification.md aan met de verduidelijkte requirement.
Voeg nieuwe acceptatiecriteria toe.
Schrijf eerst de nieuwe tests (die moeten falen), pas daarna de implementatie aan.
Run harness/run_tests.sh tot alles groen is.
```

---

## Inzichten na dit onderdeel

- De agent bouwde in eerste instantie precies wat er stond... maar wat er stond was onvoldoende.
- Vage requirement = gegarandeerd het verkeerde resultaat, hoe goed de agent ook is.
- De grootste verbetering zit in de specificatie, niet in de code.