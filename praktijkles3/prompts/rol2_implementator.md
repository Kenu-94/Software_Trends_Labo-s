# Rol 2 — Implementator: het audit-plan uitvoeren

Kopieer onderstaande prompt in een **nieuwe** Cline-sessie. De agent voert precies het audit-plan uit en niets anders.

---

## Prompt (NL)

```
Je rol is Implementator.

Lees eerst docs/ADR/002-audit-plan.md. Voer elk planpunt uit in de gegeven volgorde.

Voor elk planpunt geldt de heilige volgorde: spec → tests → code
1. update specs/specification.md zodat het planpunt daar toetsbaar staat
2. schrijf eerst de nieuwe of aangepaste tests (ze moeten falen: rood)
3. implementeer dan exact genoeg om ze groen te maken

Regels:
- niets doen dat niet in het audit-plan staat
- geef geen nieuwe features toe, ook niet als de code erom vraagt
- alleen standaard Python libraries, geen nieuwe dependencies
- type hints verplicht, docstrings Google-style
- na elke wijziging: voer harness/run_tests.sh uit
- bij failing tests: los op, max 3 retries, daarna stoppen en vragen
- bestaande tests moeten blijven slagen
- rapporteer per planpunt: gedaan, en de diff die erbij hoort
```

---

## Na deze rol

- `bash harness/run_tests.sh` geeft exit code 0
- de git-diff bevat alleen wijzigingen die traceerbaar zijn naar een planpunt
- jij hebt elke diff goedgekeurd vóór de agent verder ging
- noteer de token- en kostencijfers van deze sessie in `docs/eco_log.md`