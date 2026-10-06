# Fase 2 — Acceptatiecriteria omzetten naar tests

Kopieer onderstaande prompt in Cline's chat. De agent schrijft **alleen tests**, nog geen implementatie.

---

## Prompt (NL)

```
Gebruik specs/specification.md als enige bron.

Schrijf pytest tests voor alle acceptatiecriteria uit de specificatie.

Regels:
- Eén test per acceptatiecriterium
- Nummer de tests zodat ze terug te koppelen zijn naar de criteria (bijv. AC3 in de docstring)
- Gebruik echte testdata in tests/, of maak tijdelijke CSV-bestanden in de test zelf (tmp_path)
- Test ook de edge cases uit de spec

Maak nog geen implementatie.
Geen src/grade_analyzer.py of andere broncode.
Schrijf de tests in tests/test_grade_analyzer.py.
```

---

## Prompt (EN, alternatief)

```
Use specs/specification.md as the single source of truth.

Write pytest tests covering every acceptance criterion.
One test per criterion; reference the criterion number in the docstring.
Cover the edge cases from the spec as well.

Do NOT write any implementation code yet.
Write the tests in tests/test_grade_analyzer.py.
```

---

## Na deze fase

Voer de harness uit:

```shell
bash harness/run_tests.sh
```

Alle tests **falen**: dat is rood, en dat is precies goed. De agent mag pas in fase 3 gaan implementeren.