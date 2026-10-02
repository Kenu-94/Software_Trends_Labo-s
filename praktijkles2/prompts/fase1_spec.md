# Fase 1 — Alleen de specificatie

Kopieer onderstaande prompt in Cline's chat. De agent mag **alleen de spec schrijven**, nog geen tests en nog geen code.

---

## Prompt (NL)

```
Maak eerst een volledige specificatie voor de opdracht Student Grade Analyzer.

De opdracht: een command line tool die een CSV met studentresultaten analyseert.

Voorbeeld van de input (data/results.csv):

name,score
Alice,14
Bob,8
Charlie,17

Gebruik:

python grade_analyzer.py results.csv

Verwachte output:

Aantal studenten: 3
Gemiddelde score: 13.0

Geslaagd:
- Alice
- Charlie

Niet geslaagd:
- Bob

Geef in de specificatie:
- functionele requirements
- niet-functionele requirements
- edge cases
- acceptatiecriteria (genummerd, elk toetsbaar)

Maak nog geen code en nog geen tests.
Schrijf de specificatie naar specs/specification.md.
Gebruik data/results.csv als voorbeelddata.
```

---

## Prompt (EN, alternatief)

```
First create a complete specification for the "Student Grade Analyzer" assignment.

Give:
- functional requirements
- non-functional requirements
- edge cases
- acceptance criteria (numbered, each testable)

Do NOT write any code or tests yet.
Write the specification to specs/specification.md.
```

---

## Na deze fase

Review de spec met de checklist in `instructions.md` (Deel 1). Controleer dat:

1. `specs/specification.md` bestaat
2. er **geen** `src/`- of `tests/`-bestanden zijn aangemaakt
3. elke acceptatiecriteria toetsbaar is

---

## Tips

- Staan de edge cases er echt in? Denk aan: lege CSV, score 0, score 100, negatieve score, niet-numerieke score, missende kolommen, bestand bestaat niet, bestand met alleen een header.
- Is "gemiddelde" gedefinieerd (aritmetisch, afronding)?
- Is "geslaagd" gedefinieerd (score >= 10)? Is 10 geslaagd?