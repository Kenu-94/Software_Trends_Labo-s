# Skill: Off-the-shelf MCP-server koppelen aan Cline

name: mcp-koppelen
description: Koppel een kant-en-klare MCP-server (filesystem, git, sqlite, ...) aan Cline in VS Code. Gebruik wanneer de agent tools van externe systemen nodig heeft.

## Wanneer gebruiken

- De agent heeft tools nodig die Cline niet ingebouwd heeft (database, git, begrensd bestandssysteem)
- Er moet een server geconfigureerd worden in `.vscode/cline_mcp_settings.json`

## Instructies

1. Zoek eerst of er een off-the-shelf server bestaat in de [MCP Servers Registry](https://github.com/modelcontextprotocol/servers); bouw nooit zelf wat er al bestaat
2. Bepaal het transport: lokale TypeScript-server via `npx`, lokale Python-server via `uvx`, of remote via HTTP
3. Voeg de server toe aan `.vscode/cline_mcp_settings.json`:

   ```json
   {
     "mcpServers": {
       "<naam>": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-<naam>", "<pad-argument>"],
         "disabled": false,
         "autoApprove": []
       }
     }
   }
   ```

4. Voor Python-servers gebruik je `"command": "uvx"` met de package-naam als eerste arg
5. Zet `autoApprove` alleen voor expliciet genoemde, alleen-lezen tools; alles andere bevestigt de gebruiker handmatig
6. Laat de gebruiker herstarten (Developer: Reload Window) en check in het MCP-paneel of de server **Connected** is
7. Test met een expliciete prompt ("gebruik de <naam> MCP-server om ...")
8. Documenteer eventuele vereisten (Node.js voor npx, uv voor uvx, database-bestand moet bestaan)

## Constraints

- Begrens filesystem-servers tot de werkmap; geef nooit het hele bestandssysteem bloot
- Koppel geen servers die credentials nodig hebben zonder expliciete toestemming
- Externe schrijfacties (mail, chat, publicatie) zijn niet toegelaten zonder goedkeuring
- Een server die niet in de registry of een betrouwbare bron staat, koppel je niet
