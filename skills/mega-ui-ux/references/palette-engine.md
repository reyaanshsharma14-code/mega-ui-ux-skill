# Massive Color Palette Engine Reference
**Author: ScraperDev BD** (https://www.scraperdevbd.fun/)

The Ultra UI/UX Pro Max palette engine (`scripts/palette_engine.py`) programmatically generates thousands of reproducible, WCAG 2.2 AA compliant semantic color tokens.

---

## 1. Features
- **Deterministic Seeds**: Recreate the exact same palette at any time using `--seed <number>`.
- **Theme Modes**: `dark`, `light`, and `amoled` (pure `#000000` pitch black).
- **Color Harmonies**:
  - `analogous`: Subtle, cohesive color transitions (±35° hue shift).
  - `complementary`: High-contrast visual punch (180° opposite).
  - `split-complementary`: Dynamic tension (150° and 210° offsets).
  - `triadic`: Balanced equilateral triangle (120° offsets).
  - `tetradic`: Rich four-color matrix (90° offsets).
  - `monochromatic`: Single-hue variations with lightness/saturation stepping.
- **Mood Modifiers**: `vivid`, `pastel`, `muted`, `earthy`, `futuristic`, `luxury`, `corporate`, `playful`, `cyber`, `minimalist`.
- **WCAG 2.2 AA Contrast Validation**: Real-time luminance formula calculation:
  $$\text{Contrast} = \frac{L_1 + 0.05}{L_2 + 0.05}$$
  Ensures >= 4.5:1 for normal text and >= 3:1 for large text and interactive buttons.
- **Automatic Foreground Optimization**: Detects whether primary buttons require pure white `#ffffff` or dark `#000000` text for maximum contrast.
- **Gradient Recipes**: Pre-computes linear, radial, and ambient mesh gradients.

---

## 2. Generated Design Tokens

Every palette generates a complete token object:
```json
{
  "background": "#090a0f",
  "surface": "#12141c",
  "surface-elevated": "#1a1d28",
  "text-primary": "#f8fafc",
  "text-secondary": "#94a3b8",
  "text-muted": "#64748b",
  "border": "#262a38",
  "border-subtle": "#1c1f2b",
  "primary": "#6366f1",
  "primary-hover": "#4f46e5",
  "primary-active": "#4338ca",
  "primary-foreground": "#ffffff",
  "secondary": "#38bdf8",
  "accent": "#ec4899",
  "success": "#10b981",
  "warning": "#f59e0b",
  "error": "#ef4444",
  "info": "#06b6d4",
  "focus-ring": "#6366f1",
  "gradient-primary": "linear-gradient(135deg, #6366f1 0%, #38bdf8 100%)",
  "gradient-ambient": "radial-gradient(circle at 50% 0%, #6366f122 0%, #090a0f 70%)",
  "gradient-mesh": "linear-gradient(45deg, #6366f133 0%, #ec489933 50%, #38bdf833 100%)"
}
```

---

## 3. CLI Commands

### Generate Dark Mode Palette
```bash
python scripts/palette_engine.py --theme dark --harmony analogous --mood futuristic
```

### Generate Light Mode Palette with Custom Base Color
```bash
python scripts/palette_engine.py --theme light --base "#2563eb" --mood corporate
```

### Export Direct CSS Variables
```bash
python scripts/palette_engine.py --theme amoled --base "#10b981" --css
```

### Generate Synchronized Dark & Light Mode Pair
```bash
python scripts/palette_engine.py --paired --base "#8b5cf6"
```
