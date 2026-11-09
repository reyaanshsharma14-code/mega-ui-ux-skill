---
name: mega-ui-ux
description: >-
  Full-spectrum Product Studio, Design Engineering, Founder Council, Growth Psychology, Enterprise Design System, and Browser Verification skill.
  Synthesizes ui-ux-ultra-max + senior-uiux-product-designer + ui-ux-designer (Persona, 11-Mode Reasoning, Interface & Journey Spec, 6-Member Council),
  Impeccable (Persuade/Operate/Read/Experience modes + 21 refinement playbooks), taste-skill 2.5 (business-kind architecture, copy voice & browser gate),
  Unslop (9-pass redline unslopping & story video), Emil Kowalski's Design Engineering (frequency-based animation matrix, springs, gestures, clip-path),
  Growth Design Review (Psych -> B.I.A.S. -> C.L.E.A.R. -> Psychological Triggers causal conversion pipeline),
  B-End Enterprise Design System (0.5px micro-borders, concentric radii, Modal vs Drawer 7 negative criteria, 6 B2B page archetypes),
  Magic UI + HeroUI v3 + MotionSites.ai (shadcn @magicui/*, HeroUI v3 Tailwind v4 + React Aria compound components, 65+ motion hero blueprints),
  Roast Room & Newroaster (12-seat adversarial founder council), Microsoft CUAWright / Webwright (code-as-action Playwright E2E verification & CLI Skill Factory),
  Addy Osmani's 25 Engineering Skills + Andrej Karpathy's 4 Coding Laws, and ultra-frontend/pro-max (260 presets, 320 fonts, Three.js, GSAP, Remotion).
---

# Mega UI/UX

Work like an award-winning design director and design engineer who ships production code. **Core principle: the persona, surface mode, and business kind decide which principles matter, and every visible decision traces back to them.** Generic "AI slop" is what happens when defaults decide.

Resolve `<skill>` as the folder containing this `SKILL.md`. Run Python scripts via `python <skill>/scripts/<name>.py` and Node scripts via `node <skill>/scripts/<folder>/<name>.mjs`. Read reference files **on demand** at the step that names them.

---

## 0. Size the Run & Classify the Surface

### A. Run Path
| Ask | Path |
|---|---|
| New product, site, feature or flow; full redesign; "design/build X" | **Full run**: Phases 1–10, with a checkpoint after Phase 6 |
| "Unslop", clean up, or fix a vibecoded / AI-looking screen | **Unslop 9-Pass Redline**: Write the 5-line Direction (`references/unslop/unslop-guide.md`), audit against `references/unslop/signs.md`, then execute the 9 passes in strict order: `1. Spacing → 2. Color → 3. Icons → 4. Copy → 5. Type → 6. Layout → 7. Details → 8. Visuals → 9. Motion` |
| Targeted refinement verb (`polish`, `bolder`, `quieter`, `distill`, `harden`, `clarify`, `typeset`, `colorize`, `animate`, `delight`, `overdrive`, `adapt`, `optimize`, `onboard`) | Load the matching playbook in `references/impeccable/<verb>.md` + `references/impeccable/craft-floor.md` |
| Critique or UI/animation code review | Phases 1–4 (compact), `references/impeccable/critique.md` + `references/critique.md` + `references/senior-product-designer/skill.md`. Always present concrete code/UI fixes in Emil Kowalski's required `\| Before \| After \| Why \|` markdown table (`references/emil/emil-design-eng.md`) |
| Growth UX, funnel, pricing, or conversion rate audit ("audit conversion", "review checkout/onboarding/pricing") | **Growth Design Causal Pipeline**: Run `[1. Psych Energy] → [2. B.I.A.S. Breakdown] → [3. C.L.E.A.R. Scorecard (25 pts)] → [4. Psychological Triggers] → [5. Prioritized Dev Plan]` (`references/growth-design/growth-design-guide.md`, `psych.md`, `bias.md`, `clear.md`, `psychological-triggers.md`) |
| B2B / Enterprise ("B-end") admin, table, form, drawer, or design system task | **B-End Design System Engine**: Enforce 0.5px hairlines, concentric radii ($R_{\text{outer}} = R_{\text{inner}} + \text{Padding}$), 1 Primary button per zone, 80% light-bg semantic badges, Modal vs Drawer 7 negative criteria, and 6 B2B page templates (`references/b-end-system/b-end-guide.md`, `python <skill>/scripts/audit_b_end_rules.py`) |
| Written Design Spec / Interface & Journey Guide (no code requested) | **Spec Designer Mode**: Derive the Design System Blueprint via `references/spec-designer/reasoning-engine.md` and output the 15-section Interface & Journey Guide (`references/spec-designer/spec-designer-guide.md`) |
| Component library integration (`@magicui/*`, `@heroui/react` v3, motion hero blueprints) | Load `references/component-registries/magic-ui-guide.md`, `heroui-react-guide.md` (Tailwind v4 + compound components, no `HeroUIProvider`), or `references/motionsites/motionsites-guide.md` (65+ motion hero blueprints in `prompts/*.md`) |
| Small scoped fix ("fix this empty state", "make this button feel right") | **Light run**: 2–3 line persona, 1–3 principles, the built fix, one-line rationale |
| Product, pricing, offer, positioning, or feature bet decision ("roast this offer/pricing/funnel", "what would Hormozi/Bezos/Graham say") | **Roast Room 12-Seat Council**: Run 3 adversarial rounds (`Open → Debate Cruxes → Ratify`) with weighted pillar scoring (`references/roast-room/roast-room-guide.md`, `seats.md`, `scoring.md`) and verbatim quote verification (`python <skill>/scripts/roast-room/check_quotes.py <session>`) |
| Add a new expert advisor brain & seat to the council (`/newroaster <name>`) | **Newroaster Pipeline**: Fetch 30–80 public sources, map/reduce 8 brain files with verbatim source IDs, build agent & portrait (`references/roast-room/newroaster-guide.md`, `brain-spec.md`) |
| Automate, E2E-verify, or turn a multi-step web flow into a reusable CLI tool (`/cuawright:run`, `/cuawright:craft`, `webwright`) | **CUAWright / Webwright Code-as-Action Loop**: Enumerate Critical Points in `plan.md`, explore via `aria_snapshot()` at `1280×1800` (never `full_page=True`), execute `final_runs/run_<id>/final_script.py`, and self-verify every CP against saved screenshots + `final_script_log.txt` (`references/cuawright/cuawright-guide.md`, `playwright_patterns.md`, `cli_tool_mode.md`) |
| Recreate a URL or screenshot | `references/url-recreation.md` or `node <skill>/scripts/unslop/snapshot.mjs <url> out.html` — recreate structure/rhythm only, never copy brand assets or text |

### B. Surface Mode (`references/impeccable/impeccable-guide.md`)
Classify the requested surface (not the whole company) before choosing layout or motion:
- **Persuade** (landing pages, pricing, campaigns): earn attention and action; bold POV, real photography or live product views.
- **Operate** (dashboards, apps, tools, admin, settings): scanability, consistency, neutral surfaces, and native expectations outrank expression.
- **Read** (docs, articles, changelogs, guides): structure for comprehension and typographic comfort first.
- **Experience** (portfolios, showcases, interactive 3D): let the artifact lead from viewport 1 while chrome recedes.

### C. Business Kind (`references/taste/taste-skill-guide.md`)
| Brief | Kind | Visual & Effect Rule |
|---|---|---|
| SaaS, AI, dev tool, fintech, studio selling software | `software` | Live HTML UI in an `app-frame`, pulsing diagrams, real tool icons; at most 1 shader/WebGL effect and 1–2 dealt moments |
| Game or game launch | `gaming` | Full-bleed key art or setting photography, bold title treatment |
| Hardware / tech device | `tech` | Product photography or requested 3D render, close-up parts, bench use |
| Physical consumer product (chair, bike, coffee beans) | `product` | Real photography (or stand-in photos of the exact category; 3D render only if asked); product fills its frame; swatch changes photo; **no shader effects or dark tech grounds** |
| Hired expertise (clinic, law firm, agency, trade) | `service` | Photographs of people/work, flat tonal surfaces, clear proof |
| Physical destination (cafe, bakery, hotel, shop, gym) | `place` | 12–20 real photographs, flat tokens, visit/hours/address block on screen 2, **zero shader effects, zero fake dashboards, zero dark neon grounds** |

---

## 1. Ground Yourself
- Inspect `package.json`, framework, existing tokens/components, and language (JS vs TS). **Adapt to the existing stack; never migrate it uninvited.** Default to TypeScript on new projects.
- For a redesign, run or screenshot the current UI first and inventory shipped features (`kept / moved / dropped + reason`).
- If the user is a **non-designer** (`references/persona.md`), use plain words, ask at most 3 questions about their world, and always render screens.

## 2. Persona
Read `references/persona.md`. Fill the persona card (who, job, stakes, fears, context, mental model, language), name **2–3 decision-driving traits**, and define an anti-persona.

## 3. Feel, World & Direction
Read `references/taste-signature.md` and `references/unslop/unslop-guide.md`. Write the 5-line Direction:
1. **Product:** What it does and for whom in one plain sentence.
2. **Character / Feel:** 2–3 concrete words it must feel like (`calm, exact, warm`) + 1 word it must not (`flashy`). **Banned empty words:** *clean, modern, sleek, minimal, premium*.
3. **World:** The physical material or environment the product belongs to (e.g., paper & ink, night-shift instruments, topographic maps). This tints the neutral ramp and sets the accent.
4. **Moments:** 1–2 places where richness concentrates while surrounding chrome stays quiet.
5. **Signature:** 1 small detail only this product would have, used consistently.

> **Anti-Slop Rule:** Treat output from `scripts/search.py --design-system` or `references/aesthetics.md` as raw candidates only. Overrule any category cliché (purple AI gradients, glowing neon borders, glassmorphic blobs on everything).

## 4. Principles (5–8)
Read `references/principle-selector.md` and look up only the chosen laws in `ux-laws.md`, `gestalt-perception.md`, `psychology-persuasion.md`, `heuristics-frameworks.md`. Write each as: `Principle: because <persona trait or moment> → <visible decision>`.

## 5. Flow, Structure & Copy First
Read `references/flows-patterns.md` and `references/taste/copy.md` (`copy-voice.md`, `copy-tells.md`).
- **Write real copy before layout** because headline length dictates type size and composition:
  - H1 names what the product does and for whom in plain words.
  - **Zero exclamation marks (`!`)**, zero greeting headlines (`Welcome back, User! 👋`), zero trailing periods on headlines/labels/buttons, zero hype words (*supercharge, seamless, unlock, revolutionize, game-changing, AI-powered*).
  - Buttons are **verb + object** (`Send ₹48,200`, `Book Langtang trek`, never `Submit` or `Learn more`).
  - Stat deltas always name their comparison (`+12% vs last month`).
  - 60–80 words per screen outside UI mocks; no captions under images (credits go in one footer line).

## 6. Signature Moment
Pick **one** moment where craft concentrates (`references/taste-signature.md`, `references/motion-3d-playbook.md`, `references/taste/moments.md`). Everything around it stays quiet (Von Restorff).

> **Checkpoint (Full runs):** Present Phases 1–6 compactly and ask for confirmation before building screens, unless told to run straight through.

## 7. Tokens & Multi-Platform Compilation
Read `references/mediums.md` and `references/unslop/tokens.md`.
- Build from **one tinted neutral ramp** (graphite, warm, or ink—90% of pixels), **three text roles** (primary, secondary, muted), and **one accent with a job**.
- In **Operate** mode (dashboards/apps), surfaces stay neutral grey/graphite so users can work for hours; richness lives only inside charts and moments.
- Borders are quiet hairlines (`6–10%` opacity of the ramp's text colour). Nested corner radii follow $R_{\text{inner}} = \max(4\text{px}, R_{\text{outer}} - \text{padding})$.
- **Tools:**
  - `python <skill>/scripts/palette_engine.py --theme dark --base "#hex" --css`
  - `python <skill>/scripts/export_tokens.py --base "#hex" --target css|tailwind-v4|shadcn|swiftui|flutter`
  - `python <skill>/scripts/contrast.py "#fg:#bg" ...` (compute every pair; never guess)
  - `python <skill>/scripts/search.py "<query>" --font | --background | --layout | --animation`

## 8. Build with Design Engineering Craft
Read `references/ui-craft.md`, `references/impeccable/craft-floor.md`, and `references/emil/emil-design-eng.md`.
- **Spacing & Layout (`unslop` Pass 1 & 6, `taste-skill` House Rules):**
  - Strict `4px` grid (`4, 8, 12, 16, 20, 24, 32, 48, 64, 96`). Space inside a group < space between groups.
  - Equal left and right content edges. On landing pages, one section per screen (`1` or `2` viewports tall at `1440×900`, no next section heading peeking in).
  - Apps/dashboards use full-viewport app proportions (`240–280px` sidebar + fluid main area), never a narrow centered marketing column.
- **Typography (`unslop` Pass 5):**
  - 1 interface font + at most 1 display or mono partner. Weights `400`, `500`, and `600` max (avoid `700–900` shouty headings and gradient text).
  - Sentence case everywhere (no `UPPERCASE TRACKED` section labels). Never apply negative letter-spacing to small text. Always set `font-variant-numeric: tabular-nums` on numbers, prices, and tables.
- **Icons (`unslop` Pass 3):**
  - Zero emoji as UI icons. One SVG icon set, one size (`16px` or `18px`), one stroke (`1.5px`), taking the secondary/muted text colour in a fixed-width box so labels align in one column.
- **Emil Kowalski's Animation & Interaction Laws (`references/emil/emil-design-eng.md`):**
  1. **Frequency decides animation:** Actions used 100+ times/day (`Cmd+K`, keyboard navigation, tab switching) get **zero animation (`0ms`)**. Occasional overlays (drawers, modals, dropdowns) stay **under `300ms`** (`150–250ms`).
  2. **Custom easing curves:** Built-in CSS easings are too weak, and `ease-in` feels sluggish on entrances. Use strong custom curves:
     - `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)` (entrances/exits)
     - `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)` (on-screen morphs)
     - `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)` (iOS-style sheets/drawers)
  3. **Press feedback:** Every button/pressable gets `:active { transform: scale(0.97) }` (`100–160ms ease-out`).
  4. **Never animate from `scale(0)`:** Start entrances at `scale(0.95); opacity: 0`.
  5. **Origin-aware popovers:** Scale popovers and dropdowns from their trigger (`transform-origin: var(--transform-origin)`), while modals stay centered.
  6. **Tooltips:** Delay the first tooltip (`300ms`), then open adjacent tooltips **instantly (`0ms`)** once one is warm.
  7. **Interruptibility:** Prefer CSS transitions or physics springs (`references/emil/animate.md`, `gestures.md`) over keyframes for state changes so mid-flight interruptions smoothly reverse. Use `clip-path: inset(...)` for lag-free tab highlights and hold-to-delete buttons.
  8. **Only animate `transform` and `opacity`**, never `transition: all`, and always honour `prefers-reduced-motion: reduce`.
- **Forms, Tables, Dashboards & Mobile:** Follow `references/component-systems-and-dataviz.md` and `references/mobile-hig-material.md` (or `references/emil/mobile-native.md`, `animate-expo.md`, `write-swift.md`).

## 9. Verify, Lint, Redline & Run the Review Council
1. **Render, Snapshot & Code-as-Action Verification (`references/modern-web-craft.md`, `references/cuawright/cuawright-guide.md`):**
   - Capture real browser screenshots at `1440px`, `768px`, and `360px/390px`. Never hand over unseen code.
   - For multi-step interactive flows (filters, forms, sorting, modals, checkout), apply the **CUAWright / Webwright Code-as-Action discipline** (`references/cuawright/playwright_patterns.md`, `workflow.md`):
     - Enumerate every verifiable requirement as a **Critical Point (`CP1..CPn`)** in `plan.md`.
     - Drive on-page controls interactively via `get_by_role` / `aria-label` and inspect DOM regions with `locator.aria_snapshot()` rather than relying on brittle deep links.
     - Reopen closed drawers/accordions or capture visible filter chips before marking a state verified; log each step (`step <n> action: ...`) and cite the exact screenshot path for every CP.
2. **Automated Audits & Gates:**
   - HTML/JSX UX & A11y audit: `python <skill>/scripts/audit.py <file>`
   - Exact WCAG 2.2 contrast check: `python <skill>/scripts/contrast.py "#fg:#bg" ...`
   - Copy slop & hype linter: `node <skill>/scripts/taste/copy-lint.mjs <file>`
   - Performance & asset check: `node <skill>/scripts/taste/perf.mjs <file>`
3. **Self-Critique (`references/critique.md`, `references/unslop/signs.md`, `references/impeccable/craft-floor.md`):** Run the swap test, persona test, squint test, remove test, and slop-sign scan.
4. **6-Member Design Council & 12-Seat Strategy Roast (`references/council.md`, `references/roast-room/roast-room-guide.md`):**
   - Run independent passes for Persona Stand-in, Craft Critic, Layout & Accessibility Auditor, States Auditor, Ethics Reviewer, and Brief Keeper. Fix every `FAIL` (up to 3 rounds).
   - Apply **Roast Room adversarial rules** (`references/roast-room/scoring.md`):
     - **Unanimity check:** Treat unanimous Round 1 agreement as a warning; surface the strongest unargued crux and force an explicit rebuttal.
     - **Ruin Cap & One-Way Door Cap:** Any Reviewer flagging catastrophic/ruin risk caps the verdict until mitigated; irreversible one-way UX/product bets require a named cheapest test and kill criteria.
5. **Optional Unslop Story Video (`references/unslop/unslop-guide.md` #story-video):** When the user wants a shareable before-to-after redline video, build `unslop-story/story.html` with `.s1`–`.s4` CSS steps and render with `node <skill>/scripts/unslop/story.mjs`.

## 10. Hand Over
Present the output contract in `SKILL.md` order (`Assumptions · Persona · Feel/World/Direction · Mode & Kind · Principles · Flow · Signature Moment · Tokens · Screens & States · Fixed After Looking · Checks · Council Verdicts · Not Checked`), and use `| Before | After | Why |` tables for any UI review or redline pass.

---

## Reference Map

| Domain | Reference Files |
|---|---|
| **Core Process & Council** | `references/persona.md`, `taste-signature.md`, `principle-selector.md`, `ux-laws.md`, `gestalt-perception.md`, `psychology-persuasion.md`, `heuristics-frameworks.md`, `flows-patterns.md`, `mediums.md`, `ui-craft.md`, `critique.md`, `council.md` |
| **Unslop (Damir Sokolovsky, CC BY 4.0)** | `references/unslop/unslop-guide.md`, `signs.md`, `tokens.md`, `visuals.md`, `effects.md`, `refs.md` · Scripts: `scripts/unslop/snapshot.mjs`, `story.mjs` |
| **Design Engineering & Motion (Emil Kowalski, MIT)** | `references/emil/emil-design-eng.md`, `animate.md`, `animate-expo.md`, `animate-expo-recipes.md`, `animation-performance.md`, `animation-vocabulary.md`, `choreograph.md`, `choreograph-recipes.md`, `find-animation-opportunities.md`, `gestures.md`, `improve-animations.md`, `improve-animations-audit.md`, `remove-animations.md`, `review-animations.md`, `review-animations-standards.md`, `break-ui.md`, `break-ui-catalog.md`, `prototype.md`, `pick-ui-library.md`, `ask-sonner.md`, `mobile-native.md`, `write-swift.md` |
| **Impeccable Modes & 21 Playbooks (Paul Bakaus, Apache 2.0)** | `references/impeccable/impeccable-guide.md`, `craft-floor.md`, `new-work.md`, `mode-persuade.md`, `mode-operate.md`, `mode-read.md`, `shape.md`, `critique.md`, `audit.md`, `polish.md`, `bolder.md`, `quieter.md`, `distill.md`, `harden.md`, `onboard.md`, `animate.md`, `colorize.md`, `typeset.md`, `layout.md`, `delight.md`, `overdrive.md`, `clarify.md`, `adapt.md`, `optimize.md`, `document.md`, `extract.md`, `visualize.md`, `ios.md`, `android.md` |
| **Taste-Skill 2.5 (Leonxlnx, MIT)** | `references/taste/taste-skill-guide.md`, `layout-v4.md`, `sections.md`, `sections-library.md`, `copy.md`, `copy-voice.md`, `copy-tells.md`, `copy-moves.md`, `copy-registers.md`, `cards.md`, `diagrams.md`, `moments.md`, `motion.md`, `photos.md`, `icons.md`, `backgrounds.md`, `effects-usage.md`, `effects-creative.md`, `effects-objects.md`, `scenes.md`, `system.md`, `perf.md`, `gate.md` · Scripts: `scripts/taste/*.mjs` |
| **CUAWright / Webwright (Microsoft Research, MIT)** | `references/cuawright/cuawright-guide.md`, `playwright_patterns.md`, `workflow.md`, `cli_tool_mode.md`, `run.md`, `craft.md`, `browser.md`, `desktop.md` |
| **Roast Room & Newroaster (Nate Herk / AI Automation Society, MIT)** | `references/roast-room/roast-room-guide.md`, `newroaster-guide.md`, `roster.json`, `seats.md`, `round-prompts.md`, `scoring.md`, `report-template.md`, `live-room.md`, `brain-spec.md`, `extract-prompt.md`, `writer-prompt.md`, `agent-template.md`, `agents/council-*.md`, `brains/<12-advisors>/*` · Scripts: `scripts/roast-room/check_quotes.py`, `fetch.mjs`, `check_quotes.mjs`, `add_seat.mjs`, `portrait.mjs`, `build_portraits.py` |
| **Growth Design Review (woakin, MIT)** | `references/growth-design/growth-design-guide.md`, `psych.md`, `bias.md`, `clear.md`, `rules-of-thumb.md`, `psychological-triggers.md` |
| **B-End Enterprise Design System (Ludi-Herry, MIT)** | `references/b-end-system/b-end-guide.md`, `01-design-tokens-and-foundations.md` .. `07-design-system-audit-checklist.md`, `components.manifest.json`, `templates/*.tsx` · Script: `scripts/audit_b_end_rules.py` |
| **Senior Product Designer & Spec Designer (jooo20188-ai & dr-spook, MIT)** | `references/senior-product-designer/skill.md`, `modes.md`, `scoring-rubric.md`, `output-formats.md`, `*-checklist.md`, `prompts/*.md` · `references/spec-designer/spec-designer-guide.md`, `reasoning-engine.md`, `visual-system.md`, `pattern-library.md`, `delivery-and-qa.md` |
| **Magic UI, HeroUI v3 & MotionSites.ai (MIT)** | `references/component-registries/magic-ui-guide.md`, `magic-ui/components.md`, `magic-ui/recipes.md`, `heroui-react-guide.md`, `heroui-native-guide.md`, `heroui-migration-guide.md` · `references/motionsites/motionsites-guide.md`, `prompts/<65-blueprints>.md` · Scripts: `scripts/heroui-react/*.mjs` |
| **Engineering Discipline & Creative Hub (Addy Osmani, Karpathy, Open Agent Hub)** | `references/engineering-discipline/karpathy-guidelines.md`, `addy-frontend-ui-engineering.md`, `addy-*.md` (25 guides) · `references/creative-hub/remotion-best-practices.md`, `algorithmic-art.md`, `canvas-design.md`, `theme-factory.md`, `web-artifacts-builder.md`, `baoyu-*.md` |
| **3D, Scroll Storytelling, Web Craft & Catalogs** | `references/motion-3d-playbook.md`, `modern-web-craft.md`, `aesthetics.md`, `gsap.md`, `components.md`, `component-library.md`, `component-systems-and-dataviz.md`, `mobile-hig-material.md`, `typography-guide.md`, `font-pairing-guide.md`, `layout-patterns-guide.md`, `background-design-guide.md`, `*-catalog.json` · Scripts: `scripts/search.py`, `palette_engine.py`, `export_tokens.py`, `contrast.py`, `audit.py`, `design-system.py`, `url_recreator.py` |
