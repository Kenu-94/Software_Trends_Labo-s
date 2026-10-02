# Fase 4 — MCP inzetten

Prompts om de off-the-shelf MCP-servers te gebruiken. Zie `mcp_config.md` voor de configuratie.

---

## 4.1 — Filesystem MCP

```text
Gebruik de filesystem MCP-server.

Zoek alle CSV-bestanden in dit project.
Analyseer welke van die bestanden gebruikt worden in de tests.
Geef per bestand aan of het gebruikt wordt en waar.
```

en daarna:

```text
Gebruik de filesystem MCP-server om extra testdata te genereren:
maak data/testdata_edge_cases.csv met edge cases uit specs/specification.md
(lege waarden, score 0, score 100, ongeldige rijen).
```

---

## 4.2 — Git MCP

```text
Gebruik de git MCP-server.
Toon welke bestanden gewijzigd zijn sinds de laatste commit
en maak daarna een commit met een betekenisvolle boodschap.
```

---

## 4.3 — SQLite MCP

Voer deze stappen in volgorde uit:

**Stap 1 — database aanmaken (mag met Python of via de SQLite MCP-server):**

```text
Maak data/grades.db aan met een tabel grades (name TEXT, score INTEGER).
Vul de tabel met de rijen uit data/results.csv.
```

Zet daarna de sqlite-server op `"disabled": false` in `.vscode/cline_mcp_settings.json` en herstart VS Code.

**Stap 2 — lezen via MCP:**

```text
Gebruik de SQLite MCP-server om data/grades.db te bevragen.

Breid grade_analyzer.py uit: de resultaten komen niet langer
uit de CSV maar uit data/grades.db.

Gebruik de MCP-server om te checken welke tabellen bestaan
en om deze query uit te voeren:

SELECT * FROM grades WHERE score >= 10;

Pas specs/specification.md en de tests aan en implementeer de wijziging.
Bestaande functionaliteit (CSV-modus) blijft werken.
```

---

## Inzichten na dit onderdeel

- model ≠ tool: een LLM is geen filesystem/git/database, MCP geeft hem die mogelijkheden
- MCP = extra mogelijkheden voor de agent, zichtbaar en reviewbaar
- dezelfde agent kan tools uit meerdere servers combineren