# Cross-Platform Mobile Craft: Apple HIG & Android Material 3

Synthesizes core platform rules from Apple's Human Interface Guidelines (`apple-design`) and Google's Material Design 3 so mobile and desktop apps (SwiftUI, UIKit, AppKit, Flutter, React Native, Tauri, Electron) feel native without looking generic.

---

## 1. Platform Geometry & Ergonomics

| Metric | iOS / iPadOS (HIG) | Android (Material 3) | Web / Desktop |
|---|---|---|---|
| **Minimum tap target** | `44 × 44 pt` | `48 × 48 dp` | `44 × 44 px` (touch), `32 × 32 px` (pointer-only dense UI) |
| **Default body size** | `17 pt` (SF Pro, Dynamic Type `body`) | `16 sp` (Roboto / system) | `16 px` (`1rem`) minimum |
| **Screen edge margins** | `16 pt` (compact), `20 pt` (large phones / iPad) | `16 dp` (compact), `24 dp` (medium/expanded) | `clamp(1rem, 4vw, 3rem)` |
| **Base spacing grid** | `4 pt` / `8 pt` | `4 dp` / `8 dp` | `4 px` / `8 px` |
| **Primary navigation** | Bottom Tab Bar (3–5 items max) or Sidebar on iPad | Bottom Navigation Bar (3–5 items) or Navigation Rail on tablet | Top header or left sidebar |

---

## 2. Navigation & Hierarchy Rules

1. **Tab bars belong only on top-level destinations.** When pushing a detail screen, checkout, media player, or creation flow, hide the bottom tab bar or cover it with a sheet so the user has one clear way back.
2. **Never nest horizontal scroll inside horizontal scroll** of the same direction, or put swipe-to-delete inside a swipeable pager without clear gesture disambiguation.
3. **Sheets & Detents:** Prefer bottom sheets with medium/large detents and a visible grabber (`36 × 5 pt`) for secondary tasks on mobile rather than full-screen modals.
4. **Thumb Zone:** Primary actions on mobile belong in the bottom third of the screen (above the home indicator safe area: `env(safe-area-inset-bottom)`), while navigation back and secondary actions sit at the top.

---

## 3. Surface, Depth & Liquid Glass / Material Tonal Elevation

### Apple HIG & Liquid Glass Restraint
- **Material is for chrome, not content.** Translucent blur / Liquid Glass belongs on floating navigation bars, tab bars, toolbars, and transient overlays that float *over* scrolling content so the user senses depth.
- **Never stack glass on glass** (e.g., a blurred card inside a blurred sheet over a blurred background). Content cards sit on solid or subtly tinted opaque surfaces.
- **Concentric corner radii:** When a rounded button or card sits inside a rounded container with padding $p$, its inner radius should be $\max(0, R_{\text{outer}} - p)$ so the curves stay concentric.

### Material 3 Tonal Elevation
- In dark and light themes alike, distinguish surface hierarchy through **tonal surface steps** (`surface-dim`, `surface`, `surface-container-low`, `surface-container`, `surface-container-high`, `surface-container-highest`) rather than heavy drop shadows or harsh 1px borders everywhere.

---

## 4. Typography & Dynamic Scaling

- **Support Dynamic Type / Font Scaling:** Layouts must survive text scaled up to `200%` without clipping or overlapping. Switch horizontal rows (`icon + label + value + button`) to stacked vertical layouts when accessibility font sizes are active.
- **Optical Sizing & Weight:** Use tight tracking (`-0.02em`) on display sizes (`> 32pt/px`), neutral tracking (`0`) on body copy, and slightly loose tracking (`+0.04em` to `+0.08em`) on small uppercase captions.
- **Never go below `11 pt` / `12 sp` / `12 px`** for any legible text, including badge counts and legal footnotes.

---

## 5. Dark Mode Craft (Both Platforms)

1. **Dark mode is not colour inversion.** A surface that is white with a drop shadow in light mode becomes a *lighter* elevated grey (`#16181D` -> `#1E2128`) in dark mode, because elevation moves closer to the virtual light source.
2. **Desaturate accents by 10–20% in dark mode** so saturated colours don't vibrate against dark surfaces and so dark text on accent buttons stays readable.
3. **Never use pure `#000000` for elevated cards** (save true black for OLED backgrounds only when intentional, and use `#0E1116`–`#181C24` for surfaces so depth cues still work).
4. **Preserve semantic meaning across modes:** `primary`, `on-primary`, `surface`, `on-surface`, `outline`, `error`, `warning`, `success`.
