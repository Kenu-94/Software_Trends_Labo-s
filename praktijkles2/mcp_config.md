# MCP Configuratie voor Cline in VS Code

Wat is dit bestand? Het legt uit hoe je **off-the-shelf MCP-servers** aan Cline koppelt, en welke servers in deze les toegelaten zijn.

---

## Wat is Cline's MCP config?

Cline leest MCP-server configuratie uit een JSON-bestand.
Per server geef je: het **commando**, de **argumenten**, en eventueel extra opties.

**Lokaal bestand** (per project, deze les):

```
praktijkles2/.vscode/cline_mcp_settings.json
```

**Globaal bestand** (voor alle projecten):

```
~/.vscode-server/data/User/globalStorage/
  saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

---

## Configuratie voor deze les

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"],
      "disabled": false,
      "autoApprove": ["list_directory", "directory_tree", "read_file"]
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "${workspaceFolder}"],
      "disabled": false,
      "autoApprove": ["git_status", "git_diff", "git_log"]
    },
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "${workspaceFolder}/data/grades.db"],
      "disabled": true,
      "autoApprove": ["read_query"]
    }
  }
}
```

| Veld | Uitleg |
|---|---|
| `command` | Het commando om de server te starten (`npx` voor TypeScript-servers, `uvx` voor Python-servers) |
| `args` | Argumenten voor het commando |
| `env` | Omgevingsvariabelen (API-keys etc.; hier niet nodig) |
| `disabled` | Zet op `true` om de server tijdelijk uit te schakelen |
| `autoApprove` | Lijst van tool names die geen bevestiging nodig hebben |

**Op Windows:** zet `npx`-servers om naar `"command": "cmd"` met `"args": ["/c", "npx", ...]`. Laat `uvx`-servers ongewijzigd.

**Vereisten:** `npx` komt met Node.js; `uvx` installeer je met [uv](https://docs.astral.sh/uv/).

---

## De drie servers in deze les

| Server | Waarvoor | Kritisch? |
|---|---|---|
| **filesystem** | CSV-bestanden zoeken, tests analyseren, extra testdata genereren | Begrensd tot `${workspaceFolder}` |
| **git** | Status, diff, log en commits via gestructureerde tools | Alleen-lezen tools zijn veilig; `git_commit` review je vóór je goedkeurt |
| **sqlite** | `data/grades.db` bevragen (en aanmaken) | Alleen-lezen query's via `read_query` |

### Waarom deze servers, en welke zijn toegelaten?

**Toegelaten in deze les** (kern): filesystem, git, sqlite.
**Ook veilig om toe te voegen:** servers die alleen-lezen zijn of geen credentials nodig hebben, bv. memory, of een openbare zoekserver.
**Niet aanbevolen voor deze les:**

- servers die extern schrijven (mail, chat, social media)
- servers die API-keys of persoonlijke tokens nodig hebben
- servers uit onbekende bronnen die niet in de [MCP Registry](https://github.com/modelcontextprotocol/servers) staan

Regel: **een tool die je agent kan gebruiken, is een tool die jij moet kunnen reviewen.** Laat `autoApprove` daarom leeg of beperkt tot alleen-lezen tools.

---

## Transport-types

Lokale servers gebruiken **STDIO**: Cline start het proces en praat via stdin/stdout met JSON-RPC 2.0.

```
┌────────┐  stdin/stdout  ┌──────────────┐
│  Cline │◄─────────────►│ MCP Server   │
│  (host)│  JSON-RPC 2.0  │ (proces)     │
└────────┘                └──────────────┘
```

Remote servers gebruiken **Streamable HTTP**. Voor deze les is dat niet nodig.

---

## Foutzoeken

| Probleem | Oplossing |
|---|---|
| Server start niet | Controleer of `command` en `args` kloppen en of Node.js (`npx`) of uv (`uvx`) geïnstalleerd is |
| Status "Disconnected" | Herstart VS Code of herlaad het venster |
| Tool niet zichtbaar | Klik op het MCP-knopje in Cline en check of de server enabled is |
| SQLite-server faalt | `data/grades.db` moet bestaan; maak hem eerst aan, zet dan `"disabled": false` |
| Timeout | Voeg alleen-lezen tools toe aan `autoApprove` |
| Geen tool-suggestie | Vermeld de server expliciet in je prompt ("gebruik de filesystem MCP-server") |
| `npx` vraagt om installatie-bevestiging | Voeg `-y` toe aan de args (staat in de config hierboven) |

Meer servers: zoek in de [MCP Servers Registry](https://github.com/modelcontextprotocol/servers).
