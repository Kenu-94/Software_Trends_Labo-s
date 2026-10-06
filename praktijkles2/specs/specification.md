# Specificatie: Student Grade Analyzer

Status: definitief (fase 1, alleen specificatie). Er is nog geen code en geen test.

## 1. Doel en scope

### Doel

De tool leest een CSV-bestand met de kolommen `name` en `score` in en toont:

- het aantal studenten
- de gemiddelde score
- de lijst met geslaagden
- de lijst met niet-geslaagden

Geslaagd is een score >= 10.

Aanroep:

```shell
python grade_analyzer.py pad/naar/bestand.csv
```

### Wat de tool NIET doet

- geen statistieken per klas (dit is een latere uitbreiding)
- geen mediaan, minimum of maximum
- geen grafieken of visualisaties
- geen webinterface of GUI
- geen database
- geen wijzigingen aan het CSV-bestand
- geen herstel of correctie van ongeldige data

## 2. Definities

| Term | Definitie |
|---|---|
| student | één rij in de CSV met een geldige naam en score |
| naam | de tekst in de kolom `name`, getoond zoals in de CSV |
| score | de numerieke waarde in de kolom `score` |
| geldige score | een getal (geheel of decimaal) tussen 0 en 20 (inclusief), bijvoorbeeld 14, 8.5 of 10.0 |
| ongeldige score | een waarde die geen getal is, een leeg veld, een negatief getal of een getal boven 20 |
| geslaagd | score >= 10 |
| niet geslaagd | score < 10 |
| gemiddelde score | de som van alle scores gedeeld door het aantal studenten |

## 3. Functionele requirements

- FR-1: de tool wordt aangeroepen met het pad naar de CSV als command line argument.
- FR-2: de tool leest het CSV-bestand in en behandelt de eerste rij als kopregel met de kolommen `name` en `score`.
- FR-3: de tool toont het aantal studenten.
- FR-4: de tool toont de gemiddelde score van alle studenten.
- FR-5: de tool toont de lijst met namen van geslaagden (score >= 10).
- FR-6: de tool toont de lijst met namen van niet-geslaagden (score < 10).
- FR-7: de tool schrijft de output naar stdout, in het formaat van sectie 4.
- FR-8: bij een onbestaand bestand stopt de tool met een foutmelding en een exit code ongelijk aan 0.
- FR-9: bij een leeg bestand of een bestand met alleen een kopregel stopt de tool met een foutmelding en een exit code ongelijk aan 0.
- FR-10: als de kolom `name` of `score` ontbreekt, stopt de tool met een foutmelding en een exit code ongelijk aan 0.
- FR-11: bij een ongeldige score stopt de tool met een foutmelding die de rij en de waarde vermeldt, en een exit code ongelijk aan 0.

## 4. Exact outputformaat

Voor een bestand met Alice=14, Bob=8 en Charlie=17 is de volledige output:

```text
Aantal studenten: 3
Gemiddelde score: 13.0

Geslaagd:
- Alice
- Charlie

Niet geslaagd:
- Bob
```

Regels:

- eerste regel: `Aantal studenten: ` gevolgd door het aantal
- tweede regel: `Gemiddelde score: ` gevolgd door het gemiddelde afgerond op één decimaal (standaard afronding: een tweede decimaal van 5 of meer rondt naar boven af)
- witregel
- regel `Geslaagd:` gevolgd door elke naam op een eigen regel, voorafgegaan door `- `
- witregel
- regel `Niet geslaagd:` gevolgd door elke naam op een eigen regel, voorafgegaan door `- `
- de tool print niets anders (geen headers, geen logging)
- de namen in de lijsten staan in dezelfde volgorde als in de CSV

## 5. Edge cases en foutafhandeling

| Geval | Gedrag |
|---|---|
| lege CSV (leeg bestand of alleen kopregel) | foutmelding, geen statistieken, exit code ongelijk aan 0 |
| score is 0 | geldige score, 0 < 10 dus niet geslaagd |
| score is het maximum (20) | geldige score, 20 >= 10 dus geslaagd |
| score boven het maximum (21 of meer) | ongeldig, foutmelding, exit code ongelijk aan 0 |
| ongeldige score (geen getal, leeg veld, negatief) | foutmelding met de rij en de waarde, exit code ongelijk aan 0 |
| kolom `name` of `score` ontbreekt | foutmelding, exit code ongelijk aan 0 |
| bestand bestaat niet | foutmelding, exit code ongelijk aan 0 |

## 6. Acceptatiecriteria

- AC-1: met de voorbeelddata (Alice=14, Bob=8, Charlie=17) is de volledige output exact gelijk aan het voorbeeld in sectie 4, inclusief witregels.
- AC-2: met de voorbeelddata toont de tool `Aantal studenten: 3`.
- AC-3: met de voorbeelddata toont de tool `Gemiddelde score: 13.0` (som 39 gedeeld door 3).
- AC-4: een gemiddelde van 3.25 (scores 3, 3, 3 en 4) wordt getoond als `3.3` (tweede decimaal 5 of meer rondt naar boven af).
- AC-5: de lijst `Geslaagd:` bevat exact de namen van alle studenten met score >= 10, in de volgorde van de CSV (bij de voorbeelddata: Alice en Charlie).
- AC-6: de lijst `Niet geslaagd:` bevat exact de namen van alle studenten met score < 10, in de volgorde van de CSV (bij de voorbeelddata: Bob).
- AC-7: een student met score 10 staat in de lijst `Geslaagd:`.
- AC-8: een student met score 0 staat in de lijst `Niet geslaagd:` en de tool geeft geen foutmelding.
- AC-9: een student met score 20 (het maximum) staat in de lijst `Geslaagd:`.
- AC-10: een student met score 21 (boven het maximum) geeft een foutmelding en een exit code ongelijk aan 0.
- AC-11: een ongeldige score (bijvoorbeeld `abc`, een leeg veld of `-3`) geeft een foutmelding en een exit code ongelijk aan 0.
- AC-12: een lege CSV (alleen kopregel) geeft een foutmelding en een exit code ongelijk aan 0.
- AC-13: een bestand met alleen de kolom `name` geeft een foutmelding en een exit code ongelijk aan 0.
- AC-14: een onbestaand bestand geeft een foutmelding en een exit code ongelijk aan 0.

