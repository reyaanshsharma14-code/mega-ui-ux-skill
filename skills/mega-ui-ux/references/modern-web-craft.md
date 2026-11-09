# Modern web craft: CSS, performance, stacks, and seeing your work

## 1. Stack selection

| Project | Motion / UI stack |
|---|---|
| Static HTML | CSS + small vanilla JS; GSAP (jsDelivr) if timelines are needed; Three.js for 3D |
| React / Next.js | `motion` (Framer Motion) + shadcn/ui or the project's kit; GSAP via `@gsap/react` when needed; React Three Fiber for 3D |
| Vue / Nuxt | `@vueuse/motion`, GSAP |
| Svelte / SvelteKit | built-in transitions, GSAP |
| React Native | Reanimated |
| Flutter / SwiftUI | platform animation APIs |

Detect the stack from the repo; do not assume. For a new project with no stated language use TypeScript, with typed props and no unnecessary `any`. Never convert an existing JS project without permission.

GSAP: load bonus plugins from jsDelivr (cdnjs lacks them). All GSAP plugins are free to use. Check licences before shipping any fonts or assets (`asset-licensing-guide.md`).

## 2. Modern CSS worth using

```css
/* Fluid type and spacing */
h1 { font-size: clamp(2.5rem, 7vw, 6rem); text-wrap: balance; }
.section { padding-block: clamp(4rem, 10vw, 9rem); }
.wrap { width: min(1180px, 100% - 3rem); margin-inline: auto; }

/* Scroll-driven reveal with no JS (progressive enhancement) */
@supports (animation-timeline: view()) {
  .reveal { animation: up linear both; animation-timeline: view(); animation-range: entry 0% entry 35%; }
  @keyframes up { from { opacity: 0; transform: translateY(32px); } }
}

/* Container queries for components that live in different widths */
.card-wrap { container-type: inline-size; }
@container (min-width: 420px) { .card { grid-template-columns: 1fr 2fr; } }

/* :has() for state without JS */
.check:has(input:checked) span { text-decoration: line-through; }
form:has(:user-invalid) .submit { opacity: .6; }

/* Logical properties for RTL-safe spacing */
.btn { padding-inline: 1.5rem; margin-inline-start: .75rem; }

/* Dialogs and popovers natively */
/* <button popovertarget="m">Open</button><div id="m" popover>…</div> */

/* View transitions between states */
/* document.startViewTransition(() => render()) */

/* Accessible disclosure without JS: <details><summary> */
```

Prefer `svh/dvh` over `vh` for full-height sections on mobile. Use `aspect-ratio` on all media to prevent layout shift. Use `color-scheme` and tokens for dark mode (not inversion; elevated surfaces get lighter; avoid pure black and pure white text).

## 3. Performance budget

| Do | Never |
|---|---|
| Animate `transform` and `opacity` | Animate `width`, `height`, `top`, `left`, `margin` |
| `{ passive: true }` on scroll/touch listeners | Layout reads/writes interleaved in scroll handlers |
| `loading="lazy"` and explicit dimensions on below-fold images | Missing dimensions (CLS) |
| `font-display: swap`, preconnect to font hosts, subset weights | Loading 6 weights of 3 families |
| `will-change` only on elements that animate right now | `will-change` everywhere |
| WebP/AVIF, responsive `srcset` | Unoptimised hero PNGs |
| Cap WebGL pixel ratio; stop rendering when covered | An always-on full-screen shader under everything |

Targets: LCP < 2.5 s, CLS < 0.1, INP < 200 ms on a mid-range laptop.

## 4. Seeing your work (headless screenshots)

You must look at what you built. On Windows, Edge is almost always present and Chrome often is. For pages with WebGL use software GL flags:

```powershell
$b = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"   # or Chrome
& $b --headless=new --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist `
     --window-size=1440,900 --virtual-time-budget=9000 `
     --screenshot="$env:TEMP\shot.png" http://localhost:5173/
```

Notes learned the hard way:
- Wait for the dev server to be up first (an HTTP 200 check), and give WebGL pages a generous `--virtual-time-budget`.
- Headless will not go below ~500 px wide; to check 360 px, render inside a 360 px-wide container or use device emulation.
- Hash anchors and smooth scroll are **unreliable** in a single-shot screenshot of scroll-driven pages (sticky/fixed layers can appear mid-state). For those, drive the page with a real automation tool (Playwright/Puppeteer: set `scrollTo`, wait a few frames, screenshot) or the browser MCP if available, and say in the hand-over what you could not verify.
- Screenshot at 1440, 768 and 360, and at several scroll positions for scroll-driven pages.

## 5. Encoding and tooling pitfalls

- Reading and rewriting files with Windows PowerShell 5 (`Get-Content -Raw` + `Set-Content`) **corrupts UTF-8** (`·` becomes `Â·`, `—` becomes `â€”`). Use `[IO.File]::ReadAllText` / `WriteAllText` with `UTF8Encoding($false)`, or edit with a proper editor tool. After any scripted text rewrite, grep for `Â|â€` and look at the page.
- Verify that fonts really loaded (network tab or computed style), not just that the CSS link exists.

## 6. Accessibility quick list (details in `heuristics-frameworks.md`)

Contrast 4.5:1 (3:1 for large text and UI), computed with `scripts/contrast.py` · visible focus · keyboard reachable everything · labels for every input, errors tied with `aria-describedby` · target size ≥ 44 px · colour never the only signal · live regions for dynamic stage text · reduced motion · landmarks and one `h1` · skip link · real text for anything a user may need to read, search or translate.
