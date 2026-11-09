# Mega UI/UX Skill (`mega-ui-ux`)

The all-in-one UI/UX design, anti-slop redlining, design engineering, and front-end craft skill for AI coding agents (Antigravity, Claude Code, Cursor, Codex, Windsurf, OpenCode).

It unites **nine open-source design, engineering, strategy & browser-agent skill suites** into one coherent workflow:

1. **Senior Product Design Process & 6-Member Review Council** (*ui-ux-ultra-max* by Rishabh Yadav) — `Persona → Feel → Principles → Flow → Signature Moment → Tokens → Build → Verify`.
2. **Surface Modes & 21 Refinement Playbooks** (*Impeccable* by Paul Bakaus, [impeccable.style](https://impeccable.style)) — scales ambition by mode (`Persuade`, `Operate`, `Read`, `Experience`) with playbooks for `polish`, `bolder`, `quieter`, `distill`, `harden`, `clarify`, `typeset`, `colorize`, `delight`, `overdrive`, `adapt`, `optimize`, and more.
3. **Business-Kind Architecture, Copy Voice & Browser Gate** (*taste-skill 2.5* by Leonxlnx) — tailors layout, photography, UI fragments, diagrams, and shader/WebGL restraint to `software | gaming | tech | product | service | place`, backed by `copy-lint.mjs` and `perf.mjs`.
4. **9-Pass Redline Unslopping & Story Video** (*Unslop* by Damir Sokolovsky, [@heydamir](https://x.com/heydamir)) — fixes vibecoded UI in strict order (`Spacing → Color → Icons → Copy → Type → Layout → Details → Visuals → Motion`) and renders before/after redline morph videos (`story.mjs`).
5. **Design Engineering & Invisible Details** (*emilkowalski/skill* by Emil Kowalski) — frequency-based animation decision framework (`100+/day = 0ms`, `<300ms` UI ceiling), custom cubic-bezier curves, spring physics, gesture momentum, origin-aware popovers, `clip-path` transitions, Sonner toast craft, and `| Before | After | Why |` reviews.
6. **12-Seat Founder & Product Strategy Council** (*Roast Room & Newroaster* by Nate Herk / AI Automation Society) — adversarial 3-round council (`Open → Debate Cruxes → Ratify`) across 12 public-work brains (Bezos, Paul Graham, Alex Hormozi, GaryVee, Dan Martell, Gino Wickman, Warren Buffett, Naval Ravikant, Codie Sanchez, Leila Hormozi, Sara Blakely, Elon Musk) with weighted pillar scoring, Ruin Cap, One-Way Door Cap, and verbatim quote verification (`check_quotes.py`).
7. **Code-as-Action Browser & E2E Verification** (*CUAWright / Webwright* by Microsoft Research) — workspace-as-state Playwright verification (`plan.md` Critical Points `CP1..CPn`, `aria_snapshot()` exploration at `1280×1800`, instrumented `final_runs/run_<id>/final_script.py`, screenshot + action-log self-verification, and `/cuawright:craft` reusable CLI Skill Factory).
8. **Searchable Design Intelligence & Multi-Platform Tokens** (*ultra-ui-ux-pro-max* by ScraperDev BD + *ultra-frontend* by Naman Mehta + original compilers) — 260 design presets, 320 fonts, 200 backgrounds, 120 layouts, 154 animations, exact WCAG 2.2 calculator (`contrast.py`), and multi-platform token compiler (`export_tokens.py` for CSS, Tailwind v4, shadcn/ui, SwiftUI, and Flutter).
9. **3D Web, Scroll Storytelling, Enterprise Components & Mobile HIG/Material 3** — procedural Three.js/R3F terrain & lighting, virtualized tables, 5-second dashboards, form validation timing, iOS HIG / Liquid Glass restraint, and Android Material 3.

---

## Install

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1 -Target all
```

### macOS / Linux
```bash
./install.sh all
```

| Target | Path |
|---|---|
| `antigravity` | `~/.gemini/config/skills/mega-ui-ux` |
| `claude` | `~/.claude/skills/mega-ui-ux` |
| `agents` | `~/.agents/skills/mega-ui-ux` |

---

## Bundled CLI Tools

```bash
# Search 260 presets, 320 fonts, 200 backgrounds, 120 layouts, 154 animations
python skills/mega-ui-ux/scripts/search.py "fintech dashboard" --design-system

# Compute exact WCAG 2.2 AA/AAA contrast ratios
python skills/mega-ui-ux/scripts/contrast.py "#e8e2d2:#0e1512" "#a8340a:#ece6d8"

# Compile synchronized light + dark tokens across 5 platforms
python skills/mega-ui-ux/scripts/export_tokens.py --base "#ff5a1f" --target tailwind-v4

# Audit HTML/JSX for UX, accessibility, and performance anti-patterns
python skills/mega-ui-ux/scripts/audit.py index.html

# Lint copy for AI slop, hype words, and punctuation tells
node skills/mega-ui-ux/scripts/taste/copy-lint.mjs index.html
```

---

## License & Attribution

Licensed under MIT, with bundled third-party references under their respective permissive open-source licenses (MIT, Apache 2.0, and CC BY 4.0). See [`NOTICE.md`](NOTICE.md) and [`licenses/`](licenses/) for full credits and license texts.
