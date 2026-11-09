# Design Presets System Reference (260 Curated Presets)
**Author: ScraperDev BD** (https://www.scraperdevbd.fun/)

The Ultra UI/UX Pro Max skill provides **260 distinct, validated design presets** across 25 industry categories plus flagship cross-domain hybrids.

All presets are stored in structured JSON at:
`references/presets-catalog.json`

---

## Preset Categories & Distribution

1. **Modern developer portfolios** (11 presets) — Terminal cyber-minimalism, Bento dossiers, sumi ink tech.
2. **Minimal editorial portfolios** (10 presets) — Swiss typographic serenity, Japanese craft, gallery monographs.
3. **Creative agency websites** (10 presets) — Maximalist motion canvas, brutalist studio vanguard, 3D spatial web.
4. **SaaS landing pages** (10 presets) — Enterprise B2B precision, developer-first dark mode, high-converting linear layouts.
5. **AI product websites** (11 presets) — Neural glow luminescence, cognitive workspaces, agentic workflows.
6. **Startup homepages** (10 presets) — Venture-backed clarity, bold challenger energy, humanist tech.
7. **Product launch pages** (11 presets) — Apple-grade keynote elegance, midnight teasers, hardware monoliths.
8. **E-commerce storefronts** (10 presets) — Modern boutique curated, luxury high-fashion minimal, streetwear drops.
9. **Product detail pages (PDP)** (11 presets) — Luxury editorial PDPs, tech spec dense, interactive 3D customizers.
10. **Admin dashboards** (10 presets) — Modern B2B clean white, dark command slate, high-density operations.
11. **Analytics dashboards** (10 presets) — Data observatory dark, real-time telemetry, funnel conversion radar.
12. **Finance dashboards** (11 presets) — Wall Street high-frequency, modern fintech consumer, crypto wealth monoliths.
13. **Authentication and login pages** (10 presets) — Minimalist centered cards, split-screen brand stories, passkey biometric.
14. **Signup and onboarding flows** (10 presets) — Multi-step progress journeys, interactive persona selectors, workspace wizards.
15. **Social networking interfaces** (10 presets) — Modern algorithmic feeds, micro-community hubs, visual creator grids.
16. **Community platforms** (10 presets) — Modern discussion forums, developer Q&A, Discord-style channel hubs.
17. **Documentation websites** (11 presets) — Stripe-grade API clarity, Vercel/Next.js docs, interactive code playgrounds.
18. **Developer tool websites** (10 presets) — Terminal cyber engines, cloud infrastructure monoliths, CLI simulators.
19. **Educational platforms** (10 presets) — Interactive academies, gamified learning quests, coding bootcamp simulators.
20. **Gaming and Minecraft websites** (11 presets) — Voxel blockcraft modern, esports arena, SMP server citadels.
21. **Mobile-first web applications** (11 presets) — iOS fluid spring touch, Material 3 dynamic, thumb-zone ergonomic layouts.
22. **Glassmorphism interfaces** (11 presets) — Frosted aurora glass, dark cosmic translucence, floating glass docks.
23. **Neo-brutalist interfaces** (11 presets) — Stark cyber brutalism, playful gumdrop brutalism, punk zine collages.
24. **Editorial and typography-led websites** (10 presets) — High-fashion magazine spreads, literary journal serenity.
25. **Experimental, futuristic, and immersive websites** (10 presets) — Three.js WebGL canvas, CRT simulations, spatial interfaces.
26. **Flagship Cross-Domain Hybrids** (10 presets) — Master implementations combining editorial typography, bento grids, and glass pills.

---

## Preset Schema Contract

Every preset follows this validated data contract:
```json
{
  "id": "port-dev-001",
  "name": "Terminal Cyber-Minimalism — Modern Developer Portfolio",
  "category": "Modern developer portfolios",
  "visual_style": "Terminal Cyber-Minimalism",
  "layout_pattern": "Split-view interactive terminal with right-hand live project canvas",
  "color_strategy": "Onyx (#0b0c10) base, slate (#1f2833) cards, electric cyan (#66fcf1) highlights",
  "typography_direction": "JetBrains Mono + Inter",
  "spacing_density": "compact",
  "component_patterns": [
    "Curated modern developer portfolios hero section",
    "Responsive accessible primary navigation bar with focus indicators",
    "Interactive project dossier cards",
    "Work experience timeline with verification links"
  ],
  "responsive_behavior": "Desktop: Multi-column expanded grid; Mobile: Single-column vertical stream, 44px tap targets.",
  "animation_strategy": "Refined cubic-bezier transitions (300ms ease), scroll-triggered stagger reveals.",
  "accessibility_considerations": "Target WCAG 2.2 AA compliance: minimum 4.5:1 text contrast ratio, visible :focus-visible rings.",
  "suitable_projects": ["Developer portfolios", "Engineering dossiers"],
  "reference_sources": ["https://dribbble.com/search/port", "https://www.scraperdevbd.fun/"],
  "implementation_notes": "Utilizes CSS Grid with tokenized CSS custom properties."
}
```

## How to Query Presets

Use the search utility:
```bash
python scripts/search.py "<keywords>" --category "<category>" --limit 3
```
