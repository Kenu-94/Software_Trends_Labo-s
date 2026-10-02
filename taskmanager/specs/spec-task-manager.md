# Spec: Taakbeheer-CLI

Status: concept, wacht op review van de opdrachtgever
Versie: 1

## Overzicht

Een CLI-applicatie die taken bijhoudt in een JSON-bestand met drie commando's: `add`, `list` en `done`.

## Commando's

### add

- aanroep: `python task_manager.py add "<beschrijving>"`
- gedrag: voegt een nieuwe taak toe met een nieuw uniek id en `done: false`
- output: een bevestiging met de beschrijving en het toegekende id
- fout: een lege beschrijving wordt geweigerd met een duidelijke melding

### list

- aanroep: `python task_manager.py list`
- gedrag: toont alle taken met id, beschrijving en status
- output: minimaal de beschrijving van elke taak; een afgevinkte taak is herkenbaar als klaar, bijvoorbeeld `[x]` of het woord `done`
- fout: bestaat niet, een lege lijst toont gewoon niets

### done

- aanroep: `python task_manager.py done <id>`
- gedrag: zet de status van de taak met dat id op `done: true`
- output: een bevestiging dat de taak is afgevinkt
- fout: een onbekend id geeft een foutmelding en een exit code ongelijk aan 0

## Data

- bestand: `tasks.json` in de huidige werkmap
- formaat: een JSON-lijst van taakobjecten
- taakobject: `{ "id": int, "description": str, "done": bool }`
- id: oplopend, start bij 1 en wordt nooit hergebruikt

## Randvoorwaarden

- Alleen de standaardbibliotheek van Python, geen externe packages
- Geen tracebacks naar de gebruiker
- Exit code 0 bij succes en ongelijk aan 0 bij een opdracht die faalt

## Acceptatiecriteria

- [ ] `add "boodschappen"` geeft exit 0, een bevestiging, en de taak staat daarna in `list`
- [ ] `list` na een toevoeging toont de beschrijving
- [ ] `done 1` na een toevoeging maakt de taak herkenbaar als klaar in `list`
- [ ] `done 999` geeft een foutmelding en een exit code ongelijk aan 0
- [ ] `add ""` geeft een duidelijke fout en geen traceback
- [ ] na een herstart staan dezelfde taken er nog en is `tasks.json` geldige JSON

## Testaanpak

- Schrijf de tests in `tests/` met pytest
- Draai de CLI als subprocess in een tijdelijke werkmap zodat `tasks.json` per test vers begint
- Spec-first: de tests komen vóór de implementatie en zijn de meetlat voor de agent