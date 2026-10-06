# Uitbreiding — Statistieken per klas

Voor sterke studenten. De agent moet een nieuwe requirement verwerken **zonder bestaande functionaliteit te breken**.

---

## De nieuwe data

`data/students.csv` bevat de klasses:

```csv
name,class
Alice,A
Bob,B
Charlie,A
```

## De nieuwe requirement

```text
Bereken statistieken per klas.
```

De agent moet eerst zelf aangeven wat hij nodig heeft (welke statistieken? per klas welke kolommen?). De requirement wordt pas concreet als de student ze aanvult.

## Prompt voor de agent (na verduidelijking)

```
Breid de opdracht uit met data/students.csv (name,class).

Nieuwe functionaliteit:
- Bereken per klas: aantal studenten, gemiddelde score, minimum, maximum
- De output toont de statistieken per klas

Werk in deze volgorde en zonder bestaande functionaliteit te breken:
1. Pas specs/specification.md aan: voeg de nieuwe requirements
   en acceptatiecriteria toe
2. Schrijf nieuwe pytest-tests voor de nieuwe criteria
   (deze moeten eerst falen)
3. Pas de implementatie aan tot alle tests, oud en nieuw, groen zijn
4. Run harness/run_tests.sh en toon het resultaat

Bestaande CSV-modus blijft exact werken.
```

## Waarom dit de moeite is

- De bestaande tests zijn de vangnetten: als die breken, heeft de agent iets kapot gemaakt
- De agent leert werken in een bestaande codebase met spec en tests als contract
- Een goede structuur (spec → tests → code) maakt refactoring betaalbaar