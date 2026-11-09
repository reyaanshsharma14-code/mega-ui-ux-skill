# Ultra UI/UX Pro Max — Quick Reference & Core Rules
**Author: ScraperDev BD** (https://www.scraperdevbd.fun/)

This document defines the core UX, design quality, and engineering standards enforced by the **Ultra UI/UX Pro Max** skill.

---

## 1. Golden Rules of High-Impact UI Design

### Avoid AI Cliches and Slop
- **NEVER** use the generic purple-blue diagonal gradient across every card and hero without explicit brand rationale.
- **NEVER** scatter random floating decorative 3D shapes or emojis as substitute iconography. Use curated SVG icons (Lucide, Heroicons, Phosphor, Feather).
- **NEVER** build fake testimonials, dummy client rosters, or non-functional placeholder buttons. Every interactive element must have a defined hover, active, and focus state.
- **NEVER** ship gray-on-gray low-contrast text. Maintain WCAG 2.2 AA standards (minimum 4.5:1 contrast for normal text, 3:1 for large text and interactive components).

### Modern Visual Excellence
1. **Typography Hierarchy**: Base font size minimum 16px for body text, line-height 1.5 to 1.6, heading line-height 1.15 to 1.25. Always set letter-spacing tight on headings (`-0.02em` to `-0.03em`) and normal or slightly open on small captions.
2. **Intentional Spacing & Rhythm**: Use a consistent 4px/8px modular spacing scale (`0.25rem`, `0.5rem`, `1rem`, `1.5rem`, `2rem`, `3rem`, `4rem`, `6rem`).
3. **Contrast & Color Depth**: Pair dark surfaces with fine hairline borders (`border: 1px solid rgba(255, 255, 255, 0.08)` or subtle tokens) to establish elevation without muddy drop shadows.
4. **Touch & Ergonomics**: Minimum tap target size of 44×44px on mobile viewports. Place primary actions in the lower 40% thumb zone on mobile layouts.
5. **Reduced Motion**: Always respect user motion preferences:
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## 2. Priority Rule Categories

| Priority | Category | Key Checks | Anti-Patterns to Avoid |
|---|---|---|---|
| **P1** | **Accessibility (A11y)** | 4.5:1 contrast, visible `:focus-visible` rings, semantic landmarks, ARIA labels | Removing focus outlines, low-contrast text |
| **P2** | **Touch & Interaction** | Min 44×44px target, tactile hover states, spring physics | Hover-only triggers on mobile, 0ms laggy states |
| **P3** | **Responsive Layout** | Mobile-first breakpoints, zero horizontal overflow, fluid `clamp()` type | Fixed px container widths, horizontal scroll |
| **P4** | **Typography & Hierarchy** | Base 16px body, curated pairings, optical tracking | Font soup (>3 fonts), tiny &lt;13px body text |
| **P5** | **Color & Design Tokens** | Semantic variables (`--color-background`, `--color-primary`), light/dark sync | Raw hex codes hardcoded inside components |
| **P6** | **Motion & Delight** | Smooth spring transitions (200-300ms), purposeful scroll reveals | Over-animated jank, animating height/width |
| **P7** | **Forms & Inputs** | Explicit `<label>`, inline error messages, clear active borders | Placeholder-only inputs, hidden error states |
| **P8** | **Data & Dashboards** | Scannable metrics, sparklines, filterable tables, legible chart colors | Unreadable charts, cluttered unsegmented layouts |

---

## 3. Stack Detection & Preservation

Before creating or editing frontend code:
1. Inspect project root (`package.json`, `index.html`, etc.).
2. Adapt to the project's existing framework:
   - **Vanilla HTML/CSS/JS**: Use CSS custom properties and semantic HTML5.
   - **React / Next.js**: Use modular components, Tailwind CSS (if installed) or CSS Modules.
   - **Vue / Svelte**: Follow idiomatic component scoped styling.
3. Do not arbitrarily install or inject new CSS frameworks if the repository already has an established styling convention.
