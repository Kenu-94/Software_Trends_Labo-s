# Business requirements: open vragen en suggesties

Vragen die je moet stellen (en beantwoorden) vóór je de spec schrijft. De antwoorden hieronder zijn **suggesties op basis van de case en de data**. Behandel ze als aannames die je bevestigt met de stakeholder vóór je ze vastlegt in `specs/specification.md`.

## 1. Scorevalidatie

| Vraag | Suggestie |
|---|---|
| Is een score verplicht? | Nee. Data bevat lege scores en `absent`, dus niet-deelname moet kunnen. |
| Betekent leeg hetzelfde als afwezig? Of is leeg onbekend? | In deze data zijn leeg, `absent` en `n/a` vermoedelijk synoniemen: niet deelgenomen. Of `leeg` iets anders betekent dan `absent` (onbekend vs geweigerd) is voor de berekeningen niet relevant, zolang alle drie buiten de statistieken vallen. |
| Wat is `absent` en `n/a`? | Allebei niet-deelname. Normaliseer naar één interne waarde, bv. `None`, en sluit uit van gemiddelde en slaagpercentage. |
| Wat is een geldige score? | Een geheel getal van 0 tot en met 20. Alles wat daarbuiten of niet parseerbaar is, is ongeldig. |
| Zijn negatieve scores geldig? | Nee. De data bevat `-2` als valstrik: behandelen als ongeldige score, niet als 0. |
| Zijn scores boven 20 geldig? | Nee. De data bevat `21` en `27`: ongeldig. |
| Wat met waarden zoals `14/20` of `50%`? | Niet parseerbaar als geheel getal: ongeldig. (Data bevat beide vormen.) Beslis: negeren, of optioneel omzetten (bv. `50%` = 10/20) als de stakeholder dat wil. |

**Beslispunt:** wat doe je met een ongeldige score? Opties: (a) rij negeren, (b) foutmelding en stoppen, (c) rapporteren en doorgaan. Suggestie: (c), want stil negeren verbergt datakwaliteitsproblemen.

## 2. Pogingen en resits

| Vraag | Suggestie |
|---|---|
| Welke poging telt? Laatste of beste? | De laatste poging telt. Data bevat studenten met `midterm` + `resit` zonder `final`. |
| Mag een resit een hoger of lager resultaat vervangen? | Ja, de laatste score vervangt de vorige, ongeacht of die hoger of lager is. De regel "resit enkel indien gebuisd" komt in deze case niet voor, maar bevestig dit. |
| Wat als de resit voor de final plaatsvond? | Volgens datum kan een resit chronologisch vóór een final liggen (of de final ontbreekt). Suggestie: rangschik per examenonderdeel op datum; de laatste poging van het laatste onderdeel telt. Blijf dit onduidelijk vinden, markeer het dan als datafout. |
| Wat met twee verschillende finals? | Twee `final`-records voor dezelfde student is een datafout. Suggestie: neem de poging met de meest recente datum en rapporteer het conflict. |

## 3. Slagen

| Vraag | Suggestie |
|---|---|
| Wanneer ben je geslaagd? | Geslaagd = score >= 10, zoals vermeld in de opdracht. Vraag wel: telt alleen de final, of de combinatie midterm/final? Suggestie: de score van de (laatste) tussentijdse beoordeling die telt als eindresultaat, dus wat er na punt 2 overblijft per student. |

## 4. Identificatie

| Vraag | Suggestie |
|---|---|
| Worden studenten geïdentificeerd via id of via naam? | Via `student_id`. Namen zijn niet stabiel: `student_info.csv` bevat `Oscar Peeters` en `Oscar P.` met hetzelfde id en e-mailadres. |
| Wat met dubbele records? | Dedupliceer op `student_id`. Bij conflicterende naam of klas wint de meest recente rij, of rapporteer het conflict. |

## 5. Statistieken

| Vraag | Suggestie |
|---|---|
| Wat wordt bedoeld met gemiddelde score? | Verduidelijk: gemiddelde per student, per examenonderdeel, of over alle studenten? Suggestie: gemiddelde van de eindresultaten (één score per student). |
| Bepaal het slaagpercentage van klas B: tellen studenten die niet meedoen mee? | Suggestie: niet-deelnemers (afwezig of ongeldige score) tellen mee in de noemer als niet-geslaagd, want het slaagpercentage van de klas moet de volledige groep weerspiegelen. Alternatief: alleen studenten met een geldige score tellen. Bevestig met de stakeholder; dit verandert het resultaat aanzienlijk. |

## 6. Datakwaliteit: datums

| Vraag | Suggestie |
|---|---|
| Wat met een ongeldige datum? | Datum niet parseerbaar (bv. `2026-13-45`): rij behandelen als datafout, rapporteren en niet meenemen in de rangschikking van pogingen. |
| Wat met een toekomstige datum? | Toekomstig ten opzichte van wat? Suggestie: definieer in de spec een referentiedatum. Datums na de referentiedatum markeer je als verdacht en rapporteer je, zonder ze stil te negeren. |

## Checklist voor de spec

- [ ] Alle vragen hierboven hebben een bevestigd antwoord (niet enkel een aanname)
- [ ] Regels voor ongeldige data staan expliciet in de spec (wat negeren, wat rapporteren)
- [ ] Elke regel is toetsbaar als test: zie `tests/` (spec first, daarna implementatie)
