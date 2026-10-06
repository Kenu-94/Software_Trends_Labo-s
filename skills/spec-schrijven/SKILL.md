# Skill: Specificatie schrijven

name: spec-schrijven
description: Schrijf of verbeter een PRD/spec vóór er code bestaat. Gebruik wanneer een opdracht eerst een specificatie nodig heeft (specs/, docs/PRD.md).

## Wanneer gebruiken

- Een feature of opdracht wordt gevraagd zonder dat er een spec bestaat in `specs/`
- Een bestaande spec moet gereviewd of aangepast worden

## Instructies

1. Lees eerst de opdrachtomschrijving en bestaande specs in `specs/`
2. Schrijf de specificatie naar `specs/specification-<feature>.md` met deze vaste onderdelen:
   - **Doel**: één zin wat het product doet en voor wie
   - **Functionele requirements**: genummerd (FR1, FR2, ...), elk toetsbaar en geformuleerd als "het systeem ..."
   - **Niet-functionele requirements**: genummerd (NFR1, ...), bv. performance, dependencies, codeconventies
   - **Definities van termen**: elke dubbelzinnige term krijgt één betekenis (bv. "geslaagd = score >= 10")
   - **Edge cases**: lijst van randgevallen met verwacht gedrag
   - **Acceptatiecriteria**: genummerd (AC1, AC2, ...), één-op-één testbaar
   - **Randvoorwaarden**: wat mag NIET, welke libraries wel/niet
   - **Definition of Done**: de checklist waarop het product klaar is
3. Vermijd vage woorden ("gebruiksvriendelijk", "snel", "correct") zonder toetsbare betekenis
4. Geef bij elke functionele requirement aan hoe die getest kan worden
5. Maak geen code of tests zolang de spec niet goedgekeurd is

## Constraints

- Schrijf in het Nederlands
- Geen em-dash, geen hoofdletter na een dubbelpunt
- Elke requirement is toetsbaar, anders hoort hij er niet in
- Geen aannames: bij onduidelijkheid stel je verduidelijkende vragen aan de gebruiker
- Houd de spec zo klein mogelijk: exact wat gevraagd is