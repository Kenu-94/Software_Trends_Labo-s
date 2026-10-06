# Specificatie — Student Grade Analyzer

## Overzicht

Een command line tool die een CSV-bestand met studentresultaten inleest, analyseert
en een overzicht toont van het aantal studenten, het gemiddelde en wie geslaagd is.

## Gebruik

```
python grade_analyzer.py <pad_naar_csv>
```

Voorbeeld:

```
python grade_analyzer.py data/results.csv
```

## Inputformaat

Het CSV-bestand heeft de volgende kolommen:

| Kolom | Type | Verplicht | Omschrijving |
|---|---|---|---|
| `name` | string | ja | Naam van de student |
| `score` | numeriek | ja | Score (0–20). Niet-numerieke waarden = ongeldig |

Accessoire kolommen worden genegeerd.

## Outputformaat

```
Aantal studenten: <aantal>
Gemiddelde score: <gemiddelde>

Geslaagd:
- <naam>
- <naam>

Niet geslaagd:
- <naam>
- <naam>
```

- Het gemiddelde is het **rekenkundig gemiddelde** van alle geldige scores,
  afgerond op **1 decimaal**.
- Een student is **geslaagd** als de score ≥ 10 is.
- Een student is **niet geslaagd** als de score < 10 is.
- Studenten zonder geldige score worden **niet meegeteld** in het gemiddelde
  en verschijnen niet in de geslaagd/niet-geslaagd-lijsten.

## Functionele vereisten

| ID | Omschrijving |
|---|---|
| F1 | Het programma leest een CSV-bestand met studentnamen en scores |
| F2 | Het programma toont het aantal studenten met een geldige score |
| F3 | Het programma berekent en toont het rekenkundig gemiddelde van alle geldige scores, afgerond op 1 decimaal |
| F4 | Het programma toont een lijst van geslaagde studenten (score ≥ 10) |
| F5 | Het programma toont een lijst van niet-geslaagde studenten (score < 10) |
| F6 | Het programma accepteert het bestandspad als command line argument |

## Niet-functionele vereisten

| ID | Omschrijving |
|---|---|
| NF1 | Het programma gebruikt enkel standaard Python-bibliotheken (csv, argparse, statistics) |
| NF2 | Het programma geeft exit code 0 bij succes, exit code 1 bij fouten |
| NF3 | Het programma schrijft foutmeldingen naar stderr |

## Edge cases

| ID | Omschrijving |
|---|---|
| EC1 | CSV-bestand bestaat niet → foutmelding + exit code 1 |
| EC2 | CSV-bestand is leeg → foutmelding + exit code 1 |
| EC3 | CSV-bestand bevat enkel de header → 0 studenten, geen gemiddelde, geen lijsten |
| EC4 | Score is leeg (lege cel) → ongeldig, niet meetellen |
| EC5 | Score is niet-numeriek (`absent`, `n/a`, etc.) → ongeldig, niet meetellen |
| EC6 | Score is negatief → ongeldig, niet meetellen |
| EC7 | Score is > 20 → ongeldig, niet meetellen |
| EC8 | Score is 0 → geldig, niet geslaagd |
| EC9 | Score is 10 → geldig, geslaagd (grens is inclusief) |
| EC10 | Score is 20 → geldig, geslaagd |

## Acceptatiecriteria

| AC# | Omschrijving | Toetsbaar via |
|---|---|---|
| AC1 | Normaal bestand met 3 studenten toont correct aantal, gemiddelde en geslaagd/niet-geslaagd | Test met `results_v3.csv` (3 studenten, scores 14, 8, 17) |
| AC2 | Bestand met 60 studenten uit `data/makkelijk/results_v3.csv` verwerkt foutloos | Test met volledige dataset |
| AC3 | Leeg bestand geeft foutmelding | Test met leeg tijdelijk CSV |
| AC4 | Bestand met alleen header toont 0 studenten | Test met header-only CSV |
| AC5 | Ongeldige scores (leeg, absent, n/a, negatief, >20) worden overgeslagen | Test per edge case |
| AC6 | Score 0 is geldig en resulteert in "niet geslaagd" | Test met score=0 |
| AC7 | Score 10 is geldig en resulteert in "geslaagd" | Test met score=10 |
| AC8 | Score 20 is geldig en resulteert in "geslaagd" | Test met score=20 |
| AC9 | Bestand bestaat niet → foutmelding op stderr, exit code 1 | Test met niet-bestaand pad |
| AC10 | Argument ontbreekt → foutmelding | Test zonder argument |