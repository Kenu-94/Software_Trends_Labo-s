# Coding Standards: Taakbeheer-CLI

Geldig voor alle code in dit project. Deze standaarden zijn voor de AI-agent én voor de menselijke reviewer.

## Taal

- Code-identifiers in het Engels, bijvoorbeeld `description` in plaats van `beschrijving`
- Commentaar en docstrings in het Nederlands

## Python

- Python 3.12+
- Type hints verplicht op parameters, returnwaarden en attributen
- Google-stijl docstrings voor publieke functies en klassen:

```python
def add(description: str) -> int:
    """Voeg een taak toe en geef het nieuwe id terug.

    Args:
        description: de beschrijving van de taak.

    Returns:
        het toegekende id.
    """
```

- Maximaal 20 regels per functie
- `snake_case` voor functies en variabelen, `UPPER_SNAKE_CASE` voor constanten
- Volg PEP 8 en gebruik `pathlib` voor pad- en bestandsbewerkingen

## Tests

- Testraamwerk: pytest
- Eén scenario per test, de testnaam beschrijft het scenario
- Spec-first: schrijf eerst een rode test, implementeer daarna tot de test groen is
- Tests mogen de echte CLI aanroepen via subprocess zolang ze in een tijdelijke werkmap draaien

## Kwaliteit

- Geen ongebruikte imports, variabelen of dode code
- Geen tracebacks naar de eindgebruiker, vang problemen af met een duidelijke melding
- Elke wijziging is terug te voeren op een regel in `specs/spec-task-manager.md`
- Overschrijf nooit bestaande code zonder overleg