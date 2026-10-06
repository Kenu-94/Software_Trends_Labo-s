# PRD: Taakbeheer-CLI

## Doel

Een eenvoudige CLI-applicatie om taken bij te houden: toevoegen, bekijken en afvinken.
Dit project is de oefening in specification-driven development: eerst context en spec, dan tests, dan pas implementatie door een AI-agent.

## Functionele vereisten

Elke vereiste is toetsbaar via een test.

- [ ] `add "<beschrijving>"` voegt een nieuwe taak toe
  - toetsbaar: `list` toont de beschrijving en `tasks.json` bevat de taak
- [ ] `list` toont alle taken met id en status
  - toetsbaar: de output bevat elke toegevoegde beschrijving
- [ ] `done <id>` markeert een taak als klaar
  - toetsbaar: na `done 1` toont `list` de status als klaar
- [ ] `done` met een onbekend id geeft een duidelijke fout en een exit code ongelijk aan 0
  - toetsbaar: de output bevat een foutmelding en geen traceback
- [ ] een lege beschrijving wordt afgevangen
  - toetsbaar: geen traceback en geen indexfout
- [ ] taken blijven bewaard na een herstart van de applicatie
  - toetsbaar: een nieuwe aanroep toont dezelfde taken
- [ ] de data staat in `tasks.json` in de huidige werkmap
  - toetsbaar: het bestand bestaat en bevat geldige JSON

## Niet-functionele vereisten

- [ ] Python 3.12+ en alleen de standaardbibliotheek, geen externe packages
- [ ] veilige invoer, geen tracebacks bij onverwachte invoer
- [ ] leesbare output zonder ruis voor de gebruiker

## Definities en concepten

- Taak: een opdracht om later af te handelen
- id: een oplopend geheel getal dat start bij 1 en uniek blijft in het bestand
- status: `open` of `klaar`, in het datamodel `done: true` of `done: false`

## Randvoorwaarden

- De commando's heten `add`, `list` en `done` (Engels) zodat ze niet botsen met bestaande tools
- Geen externe libraries en geen netwerktoegang
- Het dataformaat blijft JSON zodat de gebruiker het bestand kan bekijken

## Definition of Done

- [ ] Alle functionele vereisten hierboven zijn getest en slagen
- [ ] De implementatie volgt `context/coding-standards.md`
- [ ] De agent blijft binnen het afgesproken budget
- [ ] Een menselijke reviewer keurt de code en de tests goed
- [ ] De code voldoet aan `specs/spec-task-manager.md`