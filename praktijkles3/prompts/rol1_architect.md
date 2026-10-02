# Rol 1 — Architect: de audit

Kopieer onderstaande prompt in een **nieuwe** Cline-sessie. De agent mag alleen analyseren en plannen: geen code, geen tests.

---

## Prompt (NL)

```
Je rol is Architect. Je analyseert en plant; je implementeert NIET.

Context: de Student Grade Analyzer (src/grade_analyzer.py, tests/, specs/specification.md)
is geleverd door een ander team. Wij zijn het nieuwe team en moeten hem verbeteren.

Je taak:
1. Lees specs/specification.md, src/grade_analyzer.py, tests/ en data/.
2. Zoek hiaten: ontbrekende edge cases in de spec, niet-gedekte code in de tests,
   code die de spec niet volgt, onduidelijke definities (bv. gemiddelde, geslaagd).
3. Schrijf een verbeterplan naar docs/ADR/002-audit-plan.md met:
   - het gevonden hiaat (concreet, met bestandsverwijzing)
   - de voorgestelde verbetering
   - hoe die toetsbaar is (welke test erbij komt)
   - prioriteit en volgorde

Regels:
- max 5 planpunten, uitvoerbaar in 40 minuten
- elk planpunt moet toetsbaar zijn
- geen features die niemand vroeg
- de bestaande tests moeten groen blijven: geen planpunt mag ze breken
- raadpleeg praktijkles1/karpathy.md voor de gedragsrichtlijnen
- bij onduidelijkheid: stop en vraag, maak geen aannames
```

---

## Na deze rol

- `docs/ADR/002-audit-plan.md` bestaat en elke aanpassing aan dit bestand is door jou gereviewd
- geen `src/`- of `tests/`-bestanden gewijzigd (check de git-status)
- jij hebt het plan goedgekeurd vóór je naar rol 2 gaat
- noteer alvast de token- en kostencijfers van deze sessie in `docs/eco_log.md`