# Agentic Coding — Cursustekst

Software Trends — 10 uur: 2 theorielessen + 3 praktijklessen.

**Rode draad:** *Van developer die code schrijft → naar developer die agents stuurt, valideert en bewaakt.*

Doelgroep: developers die al kunnen programmeren maar weinig ervaring hebben met agentic coding.

---

## 1. Van LLM naar Agentic Coding (Theorieles Week 1)

### 1.1 Waarom is dit relevant?

Evolutie van AI-ondersteuning:

| Tijdperk | Mens | AI |
|---|---|---|
| Vroeger | schrijft alles | geen |
| Autocomplete / Copilot | schrijft meeste | suggereert lijnen |
| AI pair programmer | schrijft veel | bouwt mee aan features |
| Agentic | stuurt werk | voert werk uit |

Zelfde opdracht, steeds grotere scope:

- "Write function" → autocomplete
- "Build feature" → pair programmer
- "Add authentication" → agentic
- "Create entire MVP" → agentic

### 1.2 Wat is een LLM?

Kernconcepten:

| Concept | Uitleg |
|---|---|
| Taalmodel | getraind op enorme tekstcorpus (internet, boeken, code), leert statistische taalpatronen |
| Token predictie | voorspelt het volgende token op basis van alle voorgaande context; autoregressief |
| Context window | aantal tokens dat het model in één keer kan verwerken; oudere informatie wordt "vergeten" bij overschrijding (4K tot 200K tokens) |
| Embeddings | tekst als dense vector (512-4096 dimensies); gelijkaardige betekenis ligt dicht bij elkaar; basis voor semantisch zoeken en RAG |
| Reasoning modellen | chain-of-thought: extra tokens om stap-voor-stap te "denken" (o1, DeepSeek-R1) |

Samenhang: embeddings bepalen *hoe* een model tekst begrijpt, het context window bepaalt *hoeveel* het kan verwerken, token predictie is *het mechanisme* waarmee het genereert.

Waarom relevant voor agents:

| Concept | Impact op agent |
|---|---|
| Context window | bepaalt hoeveel code/instructies de agent in één keer aankan; te klein → hij "vergeet" instructies |
| Embeddings | bepalen semantische gelijkheid van codefragmenten; cruciaal voor retrieval |
| Tokenisatie | code en niet-westerse talen kosten meer tokens → impact op kosten en context budget |
| Hallucinaties | agent verzint APIs, bestanden, functienamen — altijd verifiëren |
| Prompt kwaliteit | hoe preciezer en gestructureerder, hoe beter het resultaat |
| Reasoning | bepaalt of een agent complexe problemen kan oplossen |

Experimenteer zelf:

- [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app) — zie hoe dezelfde prompt per model anders getokenized wordt
- [bbycroft.net/llm](https://bbycroft.net/llm) — 3D-visualisatie van een LLM in actie
- [projector.tensorflow.org](https://projector.tensorflow.org) — embeddings visueel verkennen
- [openrouter.ai/playground](https://openrouter.ai/playground) — zelfde prompt, meerdere modellen naast elkaar
- [lmarena.ai](https://lmarena.ai) — blind A/B-testen van modellen

Demo: geef hetzelfde probleem aan GPT-4o, Claude, Gemma, DeepSeek en gratis modellen. Bespreek snelheid, correctheid, hallucinaties en kosten.

### 1.3 Wat is een agent?

> **Agent = LLM + Tools + Geheugen + Doelen**

Een agent kan:

- bestanden lezen en aanpassen
- de terminal gebruiken
- tests uitvoeren
- git commands uitvoeren
- de browser gebruiken

```
        🎯 Goal
          |
        Agent
          |
   +------+------+------+
   |      |      |      |
  LLM   Files Terminal Tests
         Git   Browser
```

### 1.4 Wat is agentic coding?

Workflow:

```
Goal → Plan → Implement → Run tests → Fix → Retest → Done
```

Kernconcepten:

| Concept | Betekenis |
|---|---|
| Plan-Act-Observe | agent maakt plan, voert uit, evalueert het resultaat |
| Agent loops | herhalen tot doel bereikt of max iteraties |
| Tool calling | LLM kiest en roept zelf tools aan |
| Autonomous execution | uitvoeren zonder menselijke tussenkomst |
| Human approval gates | checkpoints waar de developer moet goedkeuren |

### 1.5 Denken in agents

Mindset shift:

| Vroeger | Nu |
|---|---|
| "Hoe implementeer ik dit?" | "Hoe **omschrijf** ik dit probleem?" |
| | "Hoe **verifieer** ik de oplossing?" |
| | "Hoe kan een agent dit uitvoeren?" |

Framework voor elke opdracht:

| Laag | Vraag |
|---|---|
| Taken | wat moet er gebeuren? |
| Constraints | wat mag niet? |
| Definition of done | wanneer is het klaar? |
| Validatie | hoe weten we dat het werkt? |

**Samenvatting:** LLM = token predictor met context. Agent = LLM + tools + doelen. Workflow = plan → act → observe → loop. De developer wordt taakomschrijver en validator.

---

## 2. Praktijk Week 1 — Eerste Agent Pipeline

**Doel:** zelf een volledige agent workflow opzetten met VS Code, Cline en OpenRouter.

### Deel 1: Setup (30 min)

Installeer VS Code, Cline en maak een OpenRouter account of een Google AI Studio account (deze laatste heeft 1 jaar gratis tokens, en kan je ook gebruiken in het Software Project). Kies modellen (DeepSeek, Qwen, Gemini Flash) en vergelijk prijs en kwaliteit.

**Cline aansluiten in VS Code (stappenplan):**

1. Open VS Code → Extensions (`Ctrl+Shift+X`) → zoek "Cline" → Install.
2. Klik op het Cline-icoon in de activiteitenbalk (links).
3. Kies API provider (**OpenRouter** of **Google AI Studio**) → plak je API key.
4. Kies een model (bv. DeepSeek of Gemini Flash om goedkoop te starten).
5. Auto-approve: laat alles uit op approval gates; later per tool toestaan.
6. Open je projectfolder via File → Open Folder en start een taak. Cline vraagt per actie goedkeuring.

**Folderstructuur voor deze les:**

```
task-manager/
├── src/
│   ├── main.py
│   └── task_manager.py     # logica
├── tests/
│   └── test_task_manager.py
├── harness/
│   └── run_tests.sh        # de feedback loop
└── .clinerules             # komt later; hier nog optioneel
```

### Deel 2: Eerste pipeline (30 min)

Project: Task Manager CLI. Prompt:

```
Build a task manager CLI.
Requirements:
- create task
- list tasks
- mark task done
Use Python. Write tests.
```

### Deel 3: Harness engineering (45 min)

Kernidee: **de agent werkt beter met feedback**. Maak `harness/run_tests.sh`: één commando dat linting, type check en tests draait (exit code 0 = alles ok).

De agent doorloopt zelf de loop: code → tests → fix → tests.

### Deel 4: Reflectie (15 min)

Wat deed de agent goed? Wat fout? Welke prompts werkten wel en niet?

---

## 3. TDD, MCP en de agent loop (Praktijk week 2)

nog toe te voegen

---

## 4. Risico's, controle en toekomst (Theorieles 2, Week 3)

### 4.1 Waar gaat agentic coding fout?

| Probleem | Symptoom |
|---|---|
| Hallucinaties | APIs en bibliotheken bestaan niet |
| Schijnbaar correcte code | code compileert, voldoet niet aan requirements |
| Context drift | agent vergeet het oorspronkelijke doel |
| Dependency chaos | onnodige libraries toegevoegd |
| Infinite loops | agent blijft dezelfde fout proberen oplossen |

- **Hallucinaties**: het LLM "vult in" op basis van patronen. Oplossing: altijd valideren tegen echte documentatie.
- **Schijnbaar correcte code**: draait zonder fouten, maar mist edge cases, beveiliging en error handling. Oorzaak: gebrek aan domeinkennis.
- **Context drift**: na 5-10 iteraties een zijpad ingeslagen. Oplossing: heldere DoD en human review gates.
- **Dependency chaos**: agent installeert wat al aanwezig is of wat de standaardlib al kan. Oplossing: constraints in de agent rules.
- **Infinite loops**: fix → test fail → andere fix → test fail → ... Oplossing: max retries (bv. 3), timeout, human escalation.

**Latent reasoning zonder reasoning trail.** Nieuwere modellen (bv. Google's Astra-generatie, en latent-reasoning architecturen zoals Meta's Coconut-lijn) redeneren **in de latent space**: het denkwerk gebeurt in interne vectorruimte, zonder stap-voor-stap als tokens uitgeschreven te worden. Bij klassieke reasoning modellen (o1, DeepSeek-R1) kun je de chain-of-thought lezen en harnessen: de trail verifiëren, foute assumities spotten, sturen via feedback. Bij latent reasoning is die trail er niet:

- je kunt het redeneerproces **niet inspecteren of corrigeren** tussen prompt en antwoord
- fouten blijven verborgen tot aan de output
- validatie moet volledig **extern**: via tests, review gates en de harness

Vuistregel: hoe minder het model zichtbaar redeneert, hoe sterker de objectieve meetlat eromheen moet zijn.

### 4.2 Kosten van agentic coding

Tokenverbruik wordt onderschat: één simpele bugfix kan duizenden tokens kosten.

```
Prompt → antwoord → tool call → analyse → edit → test → retry
```

Modelvergelijking:

| Model | Kostprijs | Snelheid | Kwaliteit | Geschikte use-case |
|---|---|---|---|---|
| Claude (Anthropic) | $$$ | traag | hoog | complexe redenering, architectuur, review |
| Gemini (Google) | $$ | snel | goed | dagelijkse features |
| DeepSeek / Qwen | $ | snel | goed | boilerplate, simpele fixes, bulkwerk |
| OpenRouter (diverse) | variabel | afhankelijk van model | wisselend | experimenteren, modelkeuze per taak |
| Lokaal (LLaMA, Qwen) | hardwarekost | variabel | matig | gevoelige code, geen data-exposure gewenst |

Beheersingstechnieken (dieper behandeld in hoofdstuk 5):

- **modelkeuze per taak**: goedkoop model voor eenvoudig werk, sterk model alleen voor complexe redenering
- **context compression**: samenvatten, prunen, refereren i.p.v. volledige bestanden meegeven (§5.8)
- **checkpointing**: nieuwe sessie per feature → fris context window (§5.8)
- **caching** van veelgebruikte context (`.clinerules`, projectbrief)
- **spec-first en harness**: een agent die het in één keer juist doet, is de goedkoopste agent

Vuistregel: kosten beheersen = context beheersen.

### 4.3 Human in the loop

De developer doet minder code-typing en meer:

**architect | reviewer | validator | product thinker**

Belangrijkste gewoonte: **nooit blind accepteren**. Elke agent-output is een voorstel, geen eindproduct.

Review checklist:

| Check | Vraag |
|---|---|
| Requirement | klopt het met de vraag? |
| Design | past het in de architectuur? |
| Security | geven we geen toegang prijs? |
| Testing | zijn edge cases gedekt? |
| Architectuur | houdt het systeem gezond? |

Approval gate: agent stelt voor → developer reviewt → goedkeuring? dan implementeert de agent; anders feedback en de agent past aan.

### 4.4 Welke skills veranderen van waarde?

Dalende waarde: boilerplate schrijven, CRUD-schermen bouwen, eenvoudige API wrappers, syntax memoriseren.

Stijgende waarde:

| Skill | Waarom |
|---|---|
| Requirements engineering | het probleem kunnen uitleggen |
| Architectuur | grenzen definiëren, patronen kiezen |
| Testen | kwaliteit meten en waarborgen |
| Systems thinking | grote systemen begrijpen |
| AI orchestration | meerdere agents aansturen |

```
2020: "Hoe schrijf ik deze functie?"
2025: "Hoe ontwerp ik deze feature?"
2030: "Hoe orchestreer ik 10 agents?"
```

**Developer 2026 = Architect + Reviewer + Orchestrator.** De agent doet het typewerk; jij bewaakt kwaliteit, context en visie.

---

## 5. Context Engineering (kernhoofdstuk)

Meeste opleidingen focussen te veel op tooling en te weinig op context engineering.
Kernprincipe: **Specification Driven Development + Harnessing**. De agent krijgt eerst een helder doel (spec) én een meetlat (harness), daarna pas mag hij implementeren.

### 5.1 Projectstructuur

```
project/
├── .clinerules              # agent-aanwijzingen (verplicht)
├── docs/
│   ├── PRD.md
│   ├── ADR/                 # Architecture Decision Records
│   └── WORKFLOW.md          # multi-agent workflow (optioneel)
├── specs/                   # specificaties per feature
├── harness/
│   └── run_tests.sh         # 1 commando draait alles
├── src/
├── tests/
└── prompts/                 # herbruikbare prompts en templates
```

Deze structuur geeft de agent vaste houvast: hij weet waar specs staan, waar tests horen en hoe hij feedback krijgt.

### 5.2 .clinerules — permanente context

Het belangrijkste bestand in je project: Cline leest het automatisch bij elke taak. Zonder `.clinerules` begint de agent elke sessie op nul.

Verplichte onderdelen:

```markdown
# Agent Rules — projectnaam

## Taal & conventies
- Python 3.12+, type hints verplicht, docstrings Google-style, tests pytest

## Werkwijze
- Lees eerst de relevante spec uit specs/ voor je implementeert
- Lees docs/ADR/ voor architectuurbeslissingen
- Schrijf tests vóór implementatie (spec first)
- Na elke wijziging: voer harness/run_tests.sh uit
- Bij failing tests: los op, herhaal tot alles groen is
- Voeg geen onnodige dependencies toe
- Overschrijf nooit bestaande code zonder overleg

## Constraints
- Max 3 retries per failing test, daarna escaleren naar developer
- Geen wijzigingen aan .clinerules zonder goedkeuring
- Alle code moet door de harness (tests + lint + type check)

## Definition of Done
- Alle tests slagen; harness geeft exit code 0
- Type checker geeft geen fouten
- Geen ongebruikte imports of variabelen
- Code voldoet aan de specs
```

### 5.3 PRD voor agents

Een agent-PRD moet **expliciet en toetsbaar** zijn, anders dan een humane PRD die vaag mag zijn ("gebruiksvriendelijk").

Template: doel, functionele vereisten (elk met "hoe testen we dit?"), niet-functionele vereisten, definities van termen (voorkomt misinterpretatie), expliciete randvoorwaarden (wat mag NIET, welke libraries wel/niet), en een definition of done.

### 5.4 ADR — Architecture Decision Records

Elke ADR is één bestand in `docs/ADR/` en documenteert **waarom** een beslissing is genomen: status, context, beslissing, pro/contra-argumenten, gevolgen en alternatieven. Maak er één bij elke beslissing over framework- of librarykeuze, opslag, API-design, projectstructuur of deployment.

Waarom: agents kiezen anders willekeurige patronen, en bij refactors vind je de redenen terug.

### 5.5 Specification Driven Development

Volgorde is heilig: **spec → tests → code**. De agent mag niet beginnen implementeren voor spec en tests klaar zijn; je dwingt dit af via `.clinerules`.

```
Stap 1: spec           specs/spec-feature.md   (wat moet het doen?)
Stap 2: tests          tests/test_feature.py   (hoe meten we dat?)
Stap 3: implementatie  src/feature.py          (agent doet dit)
```

### 5.6 Harness engineering

De harness is de geautomatiseerde feedback loop die de agent zelf kan draaien:

```bash
#!/bin/bash
set -e
ruff check src/ tests/        # linting
mypy src/ tests/              # type checking
pytest tests/ -v --tb=short   # unit tests
echo "✓ Harness geslaagd!"
```

Met harness: agent schrijft code → draait harness → ziet foutmelding in eigen context → fixt → herhaalt tot groen.
Zonder harness: agent zegt "klaar" → developer draait tests → 10 fouten → developer debugt zelf → context verloren.

### 5.7 De eerste prompt

Slecht: "Build the URL shortener."

Goed:

```
Lees eerst:
1. specs/spec-url-shortener.md
2. docs/ADR/001-use-python.md
3. .clinerules

Implementeer de URL Shortener API volgens de spec.
Volg spec first: specs → tests → code.
Gebruik harness/run_tests.sh voor validatie.
```

### 5.8 Context compression

Het context window is beperkt en duur. Technieken:

| Techniek | Wat | Besparing |
|---|---|---|
| Summarization | vat lange bestanden samen in 1-2 paragrafen | 50-80% |
| Pruning | verwijder geslaagde tests uit context | 20-40% |
| ADR als referentie | verwijs in plaats van volledige architectuur mee te geven | 60-90% |
| Spec-first | agent heeft alleen de spec nodig, niet de volledige codebase | 70-90% |
| Checkpointing | nieuwe Cline-sessie per feature | 100% per sessie |

Nieuwe sessie = fris context window. `.clinerules` blijft altijd beschikbaar als brug.

**Concreet in Cline:**

| Techniek | Hoe in Cline |
|---|---|
| Auto-compact | wanneer het context window vol raakt, vat Cline de conversatie automatisch samen; activeer dit in de settings |
| `/newtask` | start een nieuwe taak met een gegenereerde samenvatting van het huidige werk; oude details vallen weg |
| `/smol` | condenseert de huidige context ter plekke, zonder de sessie af te breken |
| Checkpoints | snapshots van je workspace per stap; terug naar een eerder punt i.p.v. context vergroten met correcties |
| Memory Bank | markdown-bestanden in `memory-bank/` (projectbrief, activeContext, progress, ...); de agent leest ze aan het begin van elke taak |

Praktische combinatie: lang werk → "update memory bank" → `/newtask` → verder met fris window. `.clinerules` (regels, verandert zelden) en memory bank (projectkennis, verandert per sessie) vullen elkaar.

### 5.9 Multi-agent workflows

Start met 1 agent. Schakel naar multi-agent pas bij context-limieten: grote codebases (split per domein), full-stack features (frontend + backend apart), complexe refactors (split per module).

Patroon 1 — sequential handoff, elke sessie met fris context window:

1. Sessie 1 (architect): PRD, spec en ADR's schrijven
2. Sessie 2 (implementator): implementeren volgens spec, met harness
3. Sessie 3 (tester): integratietests schrijven en uitvoeren

De documentatie uit sessie 1 is de brug tussen de sessies.

Patroon 2 — specialist agents via rollen in de prompt (architect, implementator, tester, reviewer), met een handoff protocol in `docs/WORKFLOW.md`.

---

## 6. Praktijk 3 — Project Structuur, governance en kosten

**Doel:** een professionele workflow opzetten.

### Deel 1: Goede project setup (30 min)

Bouw de projectstructuur uit hoofdstuk 5.1 en leg uit waarom elk onderdeel er is.

### Deel 2: Context engineering (30 min)

Sterk onderbelicht onderwerp. Schrijf, vóór de agent iets krijgt:

- een PRD
- een architecture.md (of ADR's)
- coding standards
- AI-rules (.clinerules)

Pas daarna krijgt de agent de opdracht. Vergelijk de kwaliteit tegen Praktijk 1.

### Deel 3: Kosten beheersen (30 min)

Meet prompts, tokens en kosten. Vergelijk Claude, Gemini Flash, Qwen en DeepSeek en bespreek per model de geschikte use-cases.

### Deel 4: Eindopdracht (30 min)

De agent bouwt een mini-app (bv. Expense Tracker). Voorwaarden:

- tests verplicht
- architecture.md verplicht
- coding standards verplicht
- budget < €0,50
- menselijke review verplicht

---

## 7. Samenvatting — Principes en gouden regels

### Kernprincipes

- **Spec first, code later**: agent implementeert pas als spec en tests klaar zijn
- **Feedback loop eerst**: zonder harness (meetlat) is agent-output ongeloofwaardig
- **Context is kostbaar**: minder en betere context = betere output en lagere kosten
- **Permanente context in bestanden**: `.clinerules`, specs en ADR's overleven elke sessie; conversatie niet
- **Nooit blind accepteren**: elke agent-output is een voorstel
- **Developer = architect + reviewer + orchestrator**: de agent doet het typewerk, jij bewaakt kwaliteit, context en visie
- **Model volgt taak**: goedkoop model voor eenvoudig werk, sterk model voor complexe redenering
- **Hoe minder zichtbaar redeneren, hoe sterker de harness**: bij latent reasoning is externe validatie de enige verificatie

### De 7 gouden regels

| # | Regel | Waarom |
|---|---|---|
| 1 | Start met `.clinerules` | permanente context voor elke sessie |
| 2 | Spec first, altijd | de agent weet exact wat te doen |
| 3 | Bouw de harness eerst | feedback loop = kwaliteit |
| 4 | ADR bij elke architectuurbeslissing | voorkomt willekeur en contextverlies |
| 5 | Compresseer context | bespaart tokens, verbetert focus |
| 6 | Review elke output | agent stelt voor, jij beslist |
| 7 | Nieuwe sessie per feature | fris context window, lagere kosten |

Tooling-installatie is 10% van het werk; de rest is **hoe je denkt, specificeert en valideert**.
