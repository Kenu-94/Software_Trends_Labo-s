# Skill: Acceptatiecriteria omzetten naar pytest-tests

name: tdd-tests
description: Zet acceptatiecriteria uit een spec om naar pytest-tests vóór de implementatie bestaat. Gebruik bij TDD of spec-first werk.

## Wanneer gebruiken

- Er bestaat een goedgekeurde spec met acceptatiecriteria in `specs/`
- Er bestaat nog geen implementatie voor de feature

## Instructies

1. Lees de spec in `specs/` volledig; de acceptatiecriteria zijn de bron van de tests
2. Schrijf één pytest-test per acceptatiecriterium, in `tests/test_<feature>.py`
3. Verwijs in de docstring van elke test naar het criterium (bv. "AC3: geslaagd bij score 10")
4. Test de edge cases uit de spec afzonderlijk
5. Gebruik `tmp_path` voor tijdelijke bestanden en houdtestdata klein en leesbaar
6. Regels voor de tests:
   - pytest, met duidelijke testnamen (`test_<gedrag>_ wanneer <conditie>`)
   - Arrange-Act-Assert structuur
   - geen implementatie-aannames: test het gedrag, niet de interne werking
7. Maak geen implementatie. Als de tests klaar zijn, moet de harness ze laten falen (rood): dit is goed

## Constraints

- Schrijf in het Nederlands, code en testnamen in het Engels
- Type hints verplicht, docstrings Google-style
- Alleen standaard libraries en pytest; geen nieuwe dependencies
- Verzin geen criteria die niet in de spec staan