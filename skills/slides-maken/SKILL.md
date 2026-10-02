# Skill: Slides maken op basis van cursustekst

name: slides-maken
description: Maak of pas Marp-slides aan op basis van een cursustekst. Gebruik wanneer theorielesmateriaal omgezet wordt naar een presentatie.

## Wanneer gebruiken

- Een cursustekst (bv. in `course-text/`) moet worden omgezet naar of aangepast in Marp-slides

## Instructies

1. Lees eerst de volledige cursustekst en de bestaande slides; identificeer de verschillen
2. Volg het bestaande Marp-formaat: frontmatter met `theme: ap-theme`, `paginate: true`, titelslide met `_class: title-slide`
3. Houd per slide beperkte inhoud: maximaal 6 rijen in een tabel of 6 bullets; te lange tabellen splitsen over meerdere slides
4. Houd de structuur van de cursustekst aan: zelfde volgorde, zelfde nummering en tijdsduur per onderdeel
5. Vermeld demo's en interactieve elementen expliciet met `[DEMO]` of `[LIVE DEMO]`
6. Sluit af met een samenvatting en een "Vragen?"-slide
7. Illustreer concepten met mermaid-diagrammen via de skill `mermaid-diagram`
8. Slides zijn een steiger voor de docent, geen script: korte zinnen, geen alinea's

## Constraints

- Schrijf in het Nederlands
- Geen em-dash, geen hoofdletter na een dubbelpunt
- Voeg geen inhoud toe die niet in de cursustekst staat tenzij de docent het gevraagd heeft
- Overschrijf bestaande slides alleen waar de cursustekst daar aanleiding toe geeft
- Bij twijfel over schaarste van inhoud: vraag de docent in plaats van slides vol te proppen
