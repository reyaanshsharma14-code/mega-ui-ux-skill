# Ultra UI/UX Pro Max — Animation Library (150+ Distinct Recipes)
**Author: ScraperDev BD** ([scraperdevbd.fun](https://www.scraperdevbd.fun/))

This reference documents the **154 distinct animation recipes** built into **Ultra UI/UX Pro Max**.

The catalog is stored in structured, searchable JSON at:
`references/animations-catalog.json`

---

## Animation Inventory by Category

| Category | Count | Code Prefix | Key Effects |
|---|---|---|---|
| **A — Entrance Animations** | 12 | `anim-ent` | Fade in, Fade from top/bottom/left/right, Scale up/down, Zoom fade, Blur to focus, Flip in, 3D rotate, Clip-path reveal |
| **B — Exit Animations** | 8 | `anim-ext` | Fade out, Slide out up/down/left/right, Scale down, Blur fade, 3D flip exit |
| **C — Hover Animations** | 12 | `anim-hov` | Color transition, Card lift, Image scale, Zoom within clipped container, Underline reveal, Border reveal, Gradient shift, Glow, Shadow elevation, Perspective tilt, Magnetic attraction, Overlay reveal |
| **D — Button & Control Animations** | 12 | `anim-btn` | Button press feedback, Ripple, Sliding background, Gradient movement, Icon slide, Arrow movement, Loading spinner, Success checkmark, Toggle switch, Checkbox drawing, Radio pop, Focus ring |
| **E — Text & Typography Animations** | 12 | `anim-txt` | Typewriter, Character-by-character reveal, Word-by-word reveal, Line-by-line reveal, Text slide, Blur reveal, Gradient text, Highlight sweep, Animated underline, Counter, Rotating phrases, Scramble text |
| **F — Scroll-Triggered Animations** | 12 | `anim-scrl` | Reveal on scroll, Staggered cards, Parallax, Sticky section, Horizontal scroll, Scroll progress bar, Scrubbed text, Image mask, Pinning sequence, Scroll scale, Ambient opacity, SVG drawing |
| **G — Navigation & Page Transitions** | 10 | `anim-nav` | Mobile drawer, Dropdown reveal, Mega-menu, Active nav indicator, Sliding tab indicator, Crossfade, Slide page, Shared-element, Modal entry/exit, Full-screen menu |
| **H — Card & Component Animations** | 10 | `anim-cmp` | 3D card tilt, Card flip, Expandable card, Accordion open/close, Image to details, Staggered grid, Horizontal carousel, Spotlight hover, Border tracing, Layered depth |
| **I — Background & Ambient Animations** | 10 | `anim-bg` | Floating shapes, Animated gradient, Mesh gradient, Ambient glow, Particle field, Starfield, Tech grid, Noise texture, Spotlight following pointer, Aurora background |
| **J — Loading & Skeleton Animations** | 8 | `anim-load` | Spinning circle, Pulsing beacon, Bouncing dots, Sliding loading bar, Indeterminate bar, Shimmer skeleton, Content crossfade, Image blur-up |
| **K — Form & Validation Animations** | 8 | `anim-frm` | Focus expansion, Floating label, Underline reveal, Success checkmark, Error shake, Error message reveal, Submit progress fill, Multi-step slide |
| **L — SVG & Icon Animations** | 8 | `anim-svg` | Path drawing, Line reveal, Circular progress ring, Stroke color transition, Icon rotation, Menu to close morph, Shape morph, Logo reveal |
| **M — 3D & Spatial Animations** | 10 | `anim-3d` | Floating 3D object, Turntable rotation, Scroll 3D rotation, Camera push-in, Camera orbit, Exploded product view, 3D card depth, Particle field, 3D model inspection, 3D scene transition |
| **N — Data, Charts & Dashboard Animations** | 8 | `anim-dsh` | Animated counter, Bar chart grow, Line chart draw, Donut arc, Progress ring, Metric value crossfade, Status ping indicator, Expandable table row |
| **O — Advanced & Experimental Effects** | 14 | `anim-adv` | Magnetic button, Spotlight hover, Custom cursor, Image displacement, Liquid transition, Glitch text, Chromatic aberration, Portal reveal, Slat mask, Elastic drag, Spring physics, Timeline wire, Drag and drop feedback, Before/after reveal |
| **Total** | **154** | | **154 Distinct Recipes** |

---

## How to Query Animations from CLI

Use the updated `scripts/search.py` CLI:

```bash
# Search animations by keyword
python scripts/search.py "card lift" --animation

# Search animations by category
python scripts/search.py --animation --category "Category F — Scroll-Triggered Animations"

# List all 15 animation categories with counts
python scripts/search.py --list-animation-categories
```

---

## Strict Animation Rules
1. **Never use static emojis as icons**: Every animated control, toggle, or status indicator must use an SVG element.
2. **Always include `@media (prefers-reduced-motion: reduce)`**: Ensure all movement can be suppressed or simplified.
3. **Prefer `transform` and `opacity`**: Avoid animating `width`, `height`, `margin`, or `left`/`top` to prevent layout thrashing and preserve 60fps responsiveness.
