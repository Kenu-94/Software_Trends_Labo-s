# Skill: Mermaid diagram maken

name: mermaid-diagram
description: Maak diagrammen (architectuur, flows, loops) als mermaid code fence, bv. in Marp slides. Gebruik wanneer een concept visueel uitgelegd moet worden.

## Wanneer gebruiken

- Een concept (architectuur, workflow, feedback loop) is lastig uit te leggen met alleen tekst
- Er staat een `[MEDIA]`- of diagram-aanduiding in slides of docs

## Instructies

1. Bepaal eerst het type: `flowchart` (processen), `sequenceDiagram` (interactie), `stateDiagram` (toestanden), `mindmap` (overzicht). Kies het simpelste type dat werkt
2. Houd het diagram beperkt: maximaal 7 knooppunten per diagram, anders splitsen
3. Gebruik korte labels (1 tot 3 woorden), detail hoort op de slide of in de tekst erbij
4. Toon waar relevant de feedback loop met een stippellijn (`-.->`)
5. Plaats diagrammen in een code fence:

   ````
   ```mermaid
   flowchart TD
       G[Goal] --> A[Agent]
       A --> R[Resultaat]
       R -. feedback .-> A
   ```
   ````
6. In Marp: marp rendert fences als `<marp-pre><code class="language-mermaid">` (let op: `<pre>` wordt `<marp-pre>`), en mermaid herkent alleen class `mermaid`. Zet daarom bovenaan het bestand dit conversieblok (vereist `--html` bij het renderen):

   ```html
   <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
   <script>
     window.addEventListener('load', () => {
       document.querySelectorAll('code.language-mermaid').forEach((el) => {
         const div = document.createElement('div');
         div.className = 'mermaid';
         div.textContent = el.textContent;
         (el.closest('pre, marp-pre') || el).replaceWith(div);
       });
       mermaid.run();
     });
   </script>
   ```

   Renderen: `npx @marp-team/marp-cli <bestand>.md --html -o slides.html`
7. Geen emoji in mermaid-nodes: marp vervangt emoji in code fences door een `<img>` (twemoji) wat de conversie stoort
8. Valideer de mermaid syntax (bv. via mermaid.live) voordat je het resultaat als af bent beschouwt

## Constraints

- Geen lange labels of zinnen in knooppunten
- Geen kleuren of styling tenzij gevraagd; houd het leesbaar op een projector
- Elk diagram heeft één boodschap; twee boodschappen = twee diagrammen
