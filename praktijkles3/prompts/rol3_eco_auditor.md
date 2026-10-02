# Rol 3 — Eco-auditor: de ecologische kost meten

Kopieer onderstaande prompt in een **nieuwe** Cline-sessie. De agent analyseert en schrijft een rapport: geen code, geen wijzigingen aan de codebasis.

---

## Prompt (NL)

```
Je rol is Eco-auditor. Je meet en schrijft; je wijzigt geen code.

Context: in deze les voerden we vier agent-rollen uit op de Student Grade Analyzer
(praktijkles2-codebasis). We willen de ecologische kost van die AI-workflow kennen.

Niveau 1 (verplicht) — meten:
1. Maak docs/eco_log.md aan met deze tabel:

   | Sessie | Rol | Model | Tokens in | Tokens uit | Kosten (euro) |
   |---|---|---|---|---|---|
   | 1 | Architect | | | | |
   | 2 | Implementator | | | | |

2. Schrijf ook een leeg metingsvoorstel klaar voor de kale-prompt-vergelijking:
   - meting A: kale prompt ("verbeter de code") voor een kleine taak
   - meting B: de context-rijke prompt uit prompts/rol2_implementator.md
   - kolommen: model, tokens, kosten, aantal retries, tijd

Niveau 2 (aanbevolen) — schatten naar CO2:
1. Reken de gemeten tokens om naar een CO2-schatting.
2. Gebruik publieke orde-van-grootte-cijfers en noem je bron.
3. Elk cijfer dat je gebruikt krijgt een expliciete aanname erbij.
4. Presenteer het als schatting met een onzekerheidsmarge, nooit als exact getal.

Niveau 3 (optioneel) — modelvergelijking:
Vergelijk een klein model (Flash) en een groot model (Pro) voor dezelfde taak:
tokens, kosten, aantal retries, tijd. Tabel in het rapport.

Schrijf de conclusies naar docs/eco_report.md:
- de tabellen
- de schatting met onzekerheidsmarge
- je aannames, expliciet genummerd
- minstens twee conclusies over hoe de workflow ecologischer kan
  (denk aan: modelkeuze, contextgrootte, aantal sessies, retries)

Regels:
- maak GEEN aannames zonder ze te benoemen (praktijkles1/karpathy.md)
- geen wijzigingen aan src/, tests/ of specs/
```

---

## Na deze rol

- `docs/eco_log.md` en `docs/eco_report.md` bestaan
- elke CO2-cijfer in het rapport staat er als schatting met aanname, niet als feit
- jij hebt aannames gecontroleerd: zijn ze plausibel?
- noteer de token- en kostencijfers van deze sessie in `eco_log.md`