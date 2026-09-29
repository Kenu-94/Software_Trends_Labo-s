# Agent Rules — cursus_ai_programming

## Taal & conventies
- Gebruik Python 3.12+
- Type hints verplicht
- Docstrings: Google-styles
- Tests: pytest

## Werkwijze
- Lees altijd eerst de relevante spec uit `specs/` voor je implementeert
- de map `course-text` bevat een zeer beknopte versie van het cursusmateriaal voor dit vak
- Lees `docs/ADR/` voor architectuur-beslissingen
- Schrijf tests **vóór** implementatie (Spec First!)
- Na elke wijziging: voer `harness/run_tests.sh` uit
- Bij failing tests: los op, herhaal tot alles groen is
- Voeg geen onnodige dependencies toe
- Gebruik minimaal externe libraries
- Overschrijf nooit bestaande code zonder overleg
- schrijf in het Nederlands tenzij expliciet anders gevraagd
- Raadpleeg `praktijkles1/karpathy.md` voor de volledige gedragsrichtlijnen

## Gedragsrichtlijnen (karpathy.md)
- **Denk voor je codeert:** benoem aannames, leg meerdere interpretaties voor, durf eenvoudigere aanpakken voor te stellen, vraag bij onduidelijkheid
- **Eenvoud eerst:** geen features buiten de vraag, geen abstracties voor eenmalige code, geen onnodige flexibiliteit
- **Chirurgische wijzigingen:** raak alleen aan wat nodig is, match bestaande stijl, refactor niets dat niet stuk is
- **Doelgericht werken:** formuleer toetsbare succescriteria, werk in plan/verifieer/plan-lussen

## context
- Lees de contextfiles in `/voorbereiding`

## Skills
- skills/mermaid-diagram: diagrammen maken als mermaid code fences (gebruik bij elke visuele uitleg)
- skills/slides-maken: Marp-slides maken of aanpassen op basis van een cursustekst
- Lees de relevante skill uit `skills/` voor je met die taak begint

## Constraints
- Budgetlimiet: vraag bij twijfel
- Max 3 retries per failing test, daarna escaleren naar developer
- Geen wijzigingen aan `.clinerules` zonder goedkeuring
- Alle suggesties tot verbetering bijhouden in `improvements.md`
- Alle code moet door de harness passen (tests + lint + type check)

## Niet doen
- vermijd em-dash
- vermijd een hoofdletter na een dubbelpunt, gebruik Nederlandstalig hoofdlettergebruik
- vermijd lange tekst
- nooit code runnen buiten de container

## Definitie van Done
- [ ] Alle tests in `tests/` slagen
- [ ] `harness/run_tests.sh` geeft exit code 0
- [ ] Type checker geeft geen fouten
- [ ] Geen ongebruikte imports of variabelen
- [ ] Code voldoet aan de specs in `specs/`