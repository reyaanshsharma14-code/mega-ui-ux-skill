# Motion, 3D and scroll storytelling playbook

Motion must explain something (where a thing came from, what changed, what is connected). One hero motion per flow; everything else is quick and quiet. This file is the practical layer on top of `ui-craft.md` §10, `gsap.md` and `animation-standards.md`.

## 1. Picking the signature moment

| Moment | When it fits | Cost |
|---|---|---|
| Scroll-driven 3D camera flight along a route | Travel, maps, real estate, "journey" products | High; needs fallbacks |
| Word-by-word headline entrance | Almost anything editorial | Low |
| Live counter or readout tied to scroll | Data, altitude, price, progress | Low |
| Shared-element / layout morph (Flip, `layoutId`, View Transitions) | App-like flows, galleries, filters | Medium |
| SVG path drawing | Routes, diagrams, logos | Low |
| Cursor-reactive object | Product showcases | Medium; desktop only |
| Command palette, dock magnification | Power-user tools | Medium |

Pick one. If you cannot say which persona emotion it serves, drop it.

## 2. Timing and easing

- 100–200 ms micro feedback; 200–300 ms small transitions; 300–500 ms large; hero entrances up to ~900 ms with a stagger of 60–100 ms per word or item.
- Enter with ease-out, exit with ease-in and faster, move with ease-in-out; springs for touch-driven motion.
- Stagger a **single** thing at a time (staging). Never animate everything on load.
- Animate `transform` and `opacity` only. If you must animate size, use `grid-template-rows` or `clip-path` tricks, not `height`.
- Reduced motion is a first-class design: show the final state, no parallax, no scroll-scrub, no autoplay, no camera drift. Branch in CSS (`@media (prefers-reduced-motion: reduce)`) **and** in JS (`matchMedia`), including WebGL camera and any rAF loops.

## 3. Scroll storytelling pattern

Structure that worked well in practice:

1. A tall container (400–600 vh) holding a `position: sticky; height: 100svh` stage.
2. A single `progress` value (0–1) computed from `-rect.top / (rect.height - innerHeight)`, **smoothed** (`p += (target - p) * (1 - exp(-dt * 5))`) so wheel jitter does not shake the scene.
3. Text stages derived from progress thresholds, announced with `aria-live="polite"`, and also present as real DOM text so the narrative survives without the effect.
4. A visible progress affordance (thin bar or counter) and a "scroll to begin" hint that fades after the first movement.
5. Content before and after the story sits on opaque surfaces so the canvas can **stop rendering** once covered.

## 4. Web 3D (Three.js / React Three Fiber)

Library choice: vanilla Three.js for plain pages, React Three Fiber + Drei in React/Next, GSAP only if you need cross-element timelines.

**Camera**
- Define poses per page zone (hero, overview, follow) and damp the live camera toward the desired pose with `1 - exp(-dt * k)`; frame-rate independent and cinematic.
- For a path flight: position = point behind the walker (arc-length parameterised, `getPointAt`) + lift + lateral offset; look-at = a point ahead. Clamp camera height above terrain/geometry (`max(y, ground(x,z) + clearance)`).
- Hero idle: slow sine drift plus a few units of pointer parallax; disabled under reduced motion.

**Procedural landscapes** (cheaper than shipping models, resolution-independent)
- Height field: domain-warped ridged multifractal noise plus a few Gaussian massifs for composition. Keep the height function in JS so the camera, the route and labels can all sample it.
- Shade in the fragment shader: albedo from altitude and slope (grass → dry grass → rock → snow with noisy snow line), diffuse + hemisphere ambient from a low warm sun, then atmospheric fog that tints toward the sun when looking at it.
- Realism comes from **lighting and atmosphere**, not polygon count: warm key light, cool shadows, aerial perspective, sky gradient with a sun glow, drifting low cloud planes, flat water at a percentile of the height distribution so lakes land in real basins.
- Contour lines can stay as a faint brand/map signature; keep them quiet.

**Performance and resilience**
- Cap `devicePixelRatio` (1.5 is a good default); watch a smoothed frame time and step the ratio down when it exceeds ~26 ms.
- Skip rendering when the canvas is covered or the tab is hidden (`rAF` already pauses hidden tabs; add your own occlusion check).
- Dispose geometries and materials when swapping content.
- Provide a non-blocking fallback if WebGL fails (static image or CSS gradient), and keep all essential content in the DOM.
- Project 3D anchors to DOM labels instead of rendering text in WebGL: crisper, selectable, accessible. Hide labels that are behind the camera.
- Decorative canvas: `aria-hidden="true"`, `pointer-events: none` if it sits over content.

## 5. Page-level motion that earns its keep

- Staggered headline entrance by words (split text, per-word `animation-delay`), then eyebrow, lede, actions, stats. Total under ~1.8 s.
- Scroll reveal with `IntersectionObserver` (one-shot, `threshold ~0.15`), `translateY(28px)` → 0, 0.8 s ease-out. Pre-reveal everything under reduced motion.
- Count-up numbers once, on first visibility, ~1.1 s ease-out cubic; final value in the DOM from the start for no-JS and reduced motion.
- Scroll progress bar via a single `transform: scaleX()` on a fixed element.
- Hover: 150–250 ms, a nudge of 4–6 px or a colour shift; never layout shift.

## 6. Checklist

- [ ] One signature moment, tied to a persona emotion
- [ ] Reduced-motion path covers CSS, JS and WebGL
- [ ] Smoothed scroll progress; narrative text exists in the DOM
- [ ] Canvas stops when covered; pixel ratio capped and adaptive
- [ ] WebGL failure fallback; labels in DOM
- [ ] Verified by screenshots at several scroll positions and three widths
