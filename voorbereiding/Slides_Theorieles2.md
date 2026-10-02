---
marp: true
theme: ap-theme
paginate: true
---

<!-- _class: title-slide -->

# Theorieles 2 — Risico's, controle en toekomst
## Software Trends — Agentic Coding

---

## Leerdoelen

- Risico's herkennen
- AI-output kritisch beoordelen
- Milieuimpact begrijpen
- Economische impact begrijpen
- Relevante developer skills identificeren

---

## 1. Waar gaat agentic coding fout?

### Gekende problemen — overzicht

| Probleem | Symptoom |
|---|---|
| Hallucinaties | APIs, bibliotheken bestaan niet |
| Schijnbaar correct | Code compileert, voldoet niet |
| Context drift | Agent vergeet oorspronkelijk doel |
| Dependency chaos | Onnodige libraries toegevoegd |
| Infinite loops | Blijft zelfde fout oplossen |

---

### Hallucinaties

- **Oorzaak:** LLM "vult in" op basis van patronen
- **Gevolg:** Verzonnen functies, endpoints, packages
- **Oplossing:** Altijd valideren tegen echte documentatie

---

### Schijnbaar correcte code

- Code draait zonder fouten
- Voldoet **niet** aan requirements
- Mist edge cases, beveiliging, error handling

**Oorzaak:** Gebrek aan domeinkennis bij LLM

---

### Context drift

- Start: duidelijk doel
- Na 5-10 iteraties: zijpad ingeslagen
- Oorzaak: agent verlaten van oorspronkelijke instructie

**Oplossing:** Heldere DoD + human review gates + beperking aantal pogingen

---

### Dependency chaos

Agent voegt toe zonder overleg:

```
npm install express  (al aanwezig)
npm install lodash   (onnodig)
npm install axios    (fetch is ingebouwd)
```

**Oplossing**: installs expliciet beheren met package manager en valideren

---

### Infinite loops

```
Fix bug
  → test fails
  → fix anders
  → test fails
  → fix anders...
```

**Oplossing:** max retries, timeout, human escalation

---

## 2. Kosten van agentic coding
### Tokenverbruik — onderschat probleem

```
Prompt
  → Antwoord
  → Tool call
  → Analyse
  → Edit
  → Test
  → Retry
```

💰 **1 simpele bugfix kan duizenden tokens kosten**

---

### Aanbieders vergeleken

| Model | Kostprijs | Snelheid | Kwaliteit |
|---|---|---|---|
| OpenRouter (diverse) | Variabel | afhankelijk | wisselend |
| Claude (Anthropic) | $$$ | traag | hoog |
| Gemini (Google) | $$ | snel | goed |
| DeepSeek | $ | snel | goed |
| Lokaal (LLaMA, Qwen) | €€€ (hardware) | variabel | matig |

**[MEDIA] Voeg kostengrafiek per taak toe** — bv. cost per feature, per bugfix


---


### Kostenverschil tussen modellen

| Model | SWE-bench Verified | Input/output per 1M | Gemengde prijs |
|---|---|---|---|
| Claude Opus 5 | 96,0% | $5 / $25 | $10,00 |
| Gemini 3.1 Pro | 80,6% | $2 / $12 | $4,50 |
| DeepSeek V4 Flash 0731 | 79,0% | $0,04 / $0,64 | $0,19 |

> Zelfde taak, 25x prijsverschil, 17% kwaliteitsverschil

---

### Wat is SWE-bench Verified?

- Benchmark: echte GitHub-issues oplossen
- ~500 handmatig geverifieerde taken
- Score = % correct opgeloste issues
- **Deeltaken:** begrijpen, code aanpassen, tests laten slagen

**Let op:** benchmarkscore ≠ jouw project. Domein en codebase verschillen.

---

### Bespaartips

- Gebruik goedkope modellen voor eenvoudige taken
- Duur model alleen voor complexe redeneringen
- Beperk context window (minder tokens)
- Caching van veelgebruikte context

---

### Caching: hoe werkt dat?

- Providers cachen **identieke prompt-prefixes**
- Cache hit: goedkoper (bv. ~10% van inputprijs) én sneller
- Werkt als het begin van je prompt **stabiel** blijft
- Verandert één teken vooraan → hele cache weg

> Dit is (onder meer) waarom we werken met een vaste `.clinerules` file!

---

### Caching in Cline

| Maatregel | Effect |
|---|---|
| **Stabiele system prompt** | blijft gecachet tussen calls |
| **Geen wijzigingen bovenin context** | prefix blijft gelijk |
| **Checkpoints / samenvattingen** | voorkomt opnieuw sturen van volledige context |

**Cline zelf cachet niet, maar stuurt context zo in dat provider-caching kan meewerken.**

---

## 3. Milieukost van agentic coding

### Vier bronnen van impact

| Niveau | Bron | Impact |
|---|---|---|
| **1. AI-calls** | Energie per token × CO₂-intensiteit elektriciteit | meest zichtbaar |
| **2. Rekentijd tools** | tests, builds, containers, zoekacties | soms groter dan LLM |
| **3. Training + infra** | modeltraining, datacenters bouwen en koelen | groot, gedeeld door alle gebruikers |
| **4. Vermeden werk** | minder mensuren, rebuilds, meetings | vaak positief |

---

### Training en infrastructuur

| Post | Cijfer (studie) |
|---|---|
| Training GPT-3 | ~1.300 MWh, ~500 ton CO₂ (Patterson e.a., 2021) |
| Training GPT-4 | geschat ~50 GWh (publicatiecijfers, onbevestigd) |
| Datacenter-overhead | cooling, stroomverlies: 1,2-1,5x boven GPU-verbruik |
| Hardware | GPU-productie en e-waste tellen vaak niet mee |

> Training kost veel, maar wordt over **miljoenen queries** afgeschreven. Inference domineert dagelijkse kosten.

---

### Waarom agents meer verbruiken

Eén feature = tientallen tot honderden modelinteracties:

```
plannen → tool-calls → refactorings
→ testanalyses → foutoplossingen → iteraties
```

| Activiteit | Milieu-impact |
|---|---|
| Enkele code-completion | laag |
| Volledige codebase-analyse | middel |
| Agent die 50 testen uitvoert | hoger |
| Agentische bugfix, meerdere iteraties | hoog |

---

### Vermeden menselijke activiteit

Agent kan vervangen: developerwerk, rebuilds, verspilde cloudresources

→ **"CO₂ per prompt" is daarom een slechte KPI**

Beter: **CO₂ per afgewerkte feature**

---

### CO₂ per feature (cijfers op basis van studies)

**Bronnen:** Epoch AI (0,3 Wh per LLM-query), Patterson e.a. (2021), grid ≈ 400 g CO₂/kWh

| Werkwijze | Energie per feature | CO₂ |
|---|---|---|
| Developer zonder AI | 6 uur laptop + builds ≈ 0,5 kWh | ~0,2 kg |
| Agent, goedkoop model | ~500 calls + tests ≈ 0,5 kWh | ~0,2 kg |
| Agent, frontier model | ~2.000 calls, lange outputs ≈ 1,5 kWh | ~0,6 kg |

> Dezelfde grootte-orde. Besparen op tokens helpt, maar de KPI blijft **CO₂ per afgewerkte feature**

**Ter context:** typische LLM-query ≈ 0,3 Wh, vergelijkbaar met een Google-zoekopdracht; oudere schattingen (3 Wh) waren 10x te hoog.

---

### Jevons-effect

> Efficiëntere AI → goedkoper per taak → **veel meer taken** → totaalverbruik stijgt

- Elke besparing verlaagt de drempel om agents in te zetten
- Netto impact: meer output, niet minder verbruik
- Efficiëntie ≠ duurzaamheid

---

### Duurzaam modelkiezen

- Lokale modellen: minder datacenterimpact, meer lokale energie, soms meer iteraties
- Frontier-modellen: omgekeerd profiel
- **Duurzaamste = laagste CO₂ per geslaagde taak**, niet het kleinste model

---

## 4. Human in the Loop

### Nieuwe rol van de developer

| Minder | Meer |
|---|---|
| Code typist | **Architect** |
| — | **Reviewer** |
| — | **Validator** |
| — | **Product thinker** |

---

### Belangrijkste gewoonte

> 🚫 **Nooit blind accepteren**

Elke agent-output = **voorstel**, geen eindproduct

---

### Review Checklist

| Check | Vraag |
|---|---|
| ✅ Requirement | Klopt het met de vraag? |
| ✅ Design | Past het in de architectuur? |
| ✅ Security | Geven we geen toegang prijs? |
| ✅ Testing | Zijn edge cases gedekt? |
| ✅ Architectuur | Houdt het systeem gezond? |

---

### Approval Gates

```
Agent voorstel
  → Developer review
  → Goedkeuring? 
    → Ja: agent implementeert
    → Nee: feedback, agent past aan
```

**[DEMO] Laat approval gate zien in Cline/CodeGate — accepteren/aanpassen**

---

## 5. Welke skills verliezen waarde?

### Dalende waarde

- Boilerplate schrijven
- CRUD schermen bouwen
- Eenvoudige API wrappers
- Syntax memoriseren

**Agentic coding automatiseert** deze taken

---

### Blijvende waarde — skills stijgen

| Skill | Waarom belangrijk |
|---|---|
| **Requirements engineering** | Probleem kunnen uitleggen |
| **Architectuur** | Grenzen definiëren, patronen kiezen |
| **Testen** | Kwaliteit meten en waarborgen |
| **Systems thinking** | Grote systemen begrijpen |
| **AI orchestration** | Meerdere agents aansturen |

---

### Skills — vooruitblik

```
2020: "Hoe schrijf ik deze functie?"
2025: "Hoe ontwerp ik deze feature?"
2030: "Hoe orchestreer ik 10 agents?"
```
---

### Conclusie

> **Developer 2026 = Architect + Reviewer + Orchestrator**

- Laat agent het typewerk doen
- Jij bewaakt de **kwaliteit, context en visie**

---

## Samenvatting Les 2

- **Risico's:** hallucinaties, drift, loops, kosten
- **Kosten:** tokens tellen, modelkeuze, caching
- **Impact op milieu:** energieverbruik, rekentijd van tools, vermeden CO₂-kost, Jevons-effect
- **Human in the loop:** altijd reviewen
- **Toekomst:** architect, orchestration, domeinkennis

---

## Vragen