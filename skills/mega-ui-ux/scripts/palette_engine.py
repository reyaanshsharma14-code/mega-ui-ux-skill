import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
"""
Massive Color Palette Engine for Ultra UI/UX Pro Max.
Author: ScraperDev BD (https://www.scraperdevbd.fun/)

Features:
- Deterministic, reproducible generation via integer seeds or string keys.
- Supports light, dark, and AMOLED black theme modes.
- Color harmonies: monochromatic, analogous, complementary, split-complementary, triadic, tetradic.
- Mood tuners: pastel, vivid, muted, earthy, futuristic, luxury, corporate, playful, cyber, minimalist.
- Complete semantic design tokens:
    background, surface, surface-elevated, text-primary, text-secondary,
    text-muted, border, border-subtle, primary, primary-hover, primary-active,
    secondary, accent, success, warning, error, focus-ring.
- WCAG 2.2 AA contrast calculation and validation.
- Linear, radial, and mesh gradient recipe generation.
- Paired light/dark theme synchronization.
- CLI interface and programmatic Python module.
"""

import sys
import os
import json
import math
import random
import argparse
from typing import Dict, Any, Tuple, Optional, List

# --- COLOR MATH & CONVERSIONS ---

def hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join([c * 2 for c in h])
    if len(h) != 6:
        raise ValueError(f"Invalid hex string: {hex_str}")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def rgb_to_hex(r: int, g: int, b: int) -> str:
    r = max(0, min(255, int(round(r))))
    g = max(0, min(255, int(round(g))))
    b = max(0, min(255, int(round(b))))
    return f"#{r:02x}{g:02x}{b:02x}"

def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r_norm, g_norm, b_norm)
    cmin = min(r_norm, g_norm, b_norm)
    delta = cmax - cmin

    # Lightness
    l = (cmax + cmin) / 2.0

    # Saturation
    if delta == 0:
        s = 0.0
        h = 0.0
    else:
        s = delta / (1.0 - abs(2.0 * l - 1.0))
        # Hue
        if cmax == r_norm:
            h = 60.0 * (((g_norm - b_norm) / delta) % 6)
        elif cmax == g_norm:
            h = 60.0 * (((b_norm - r_norm) / delta) + 2)
        else:
            h = 60.0 * (((r_norm - g_norm) / delta) + 4)
            
    if h < 0:
        h += 360.0
        
    return h, s, l

def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    h = h % 360.0
    c = (1.0 - abs(2.0 * l - 1.0)) * s
    x = c * (1.0 - abs((h / 60.0) % 2 - 1.0))
    m = l - c / 2.0

    if 0 <= h < 60:
        r_p, g_p, b_p = c, x, 0.0
    elif 60 <= h < 120:
        r_p, g_p, b_p = x, c, 0.0
    elif 120 <= h < 180:
        r_p, g_p, b_p = 0.0, c, x
    elif 180 <= h < 240:
        r_p, g_p, b_p = 0.0, x, c
    elif 240 <= h < 300:
        r_p, g_p, b_p = x, 0.0, c
    else:
        r_p, g_p, b_p = c, 0.0, x

    r = (r_p + m) * 255.0
    g = (g_p + m) * 255.0
    b = (b_p + m) * 255.0
    return int(round(r)), int(round(g)), int(round(b))

def hsl_to_hex(h: float, s: float, l: float) -> str:
    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)

# --- WCAG 2.2 RELATIVE LUMINANCE & CONTRAST ---

def get_relative_luminance(hex_str: str) -> float:
    r, g, b = hex_to_rgb(hex_str)
    
    def channel_luminance(c_val: int) -> float:
        c_norm = c_val / 255.0
        if c_norm <= 0.04045:
            return c_norm / 12.92
        else:
            return math.pow((c_norm + 0.055) / 1.055, 2.4)
            
    r_lum = channel_luminance(r)
    g_lum = channel_luminance(g)
    b_lum = channel_luminance(b)
    
    return 0.2126 * r_lum + 0.7152 * g_lum + 0.0722 * b_lum

def get_contrast_ratio(hex_a: str, hex_b: str) -> float:
    lum1 = get_relative_luminance(hex_a)
    lum2 = get_relative_luminance(hex_b)
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    return (lighter + 0.05) / (darker + 0.05)

# --- PALETTE ENGINE CLASS ---

class PaletteEngine:
    """Ultra UI/UX Pro Max Palette Generation Engine."""
    
    MOOD_PARAMS = {
        "vivid": {"s_range": (0.75, 0.95), "l_primary": 0.52},
        "pastel": {"s_range": (0.35, 0.60), "l_primary": 0.70},
        "muted": {"s_range": (0.25, 0.45), "l_primary": 0.48},
        "earthy": {"s_range": (0.30, 0.55), "l_primary": 0.42},
        "futuristic": {"s_range": (0.80, 1.00), "l_primary": 0.55},
        "luxury": {"s_range": (0.40, 0.65), "l_primary": 0.45},
        "corporate": {"s_range": (0.60, 0.80), "l_primary": 0.46},
        "playful": {"s_range": (0.70, 0.90), "l_primary": 0.54},
        "cyber": {"s_range": (0.85, 1.00), "l_primary": 0.50},
        "minimalist": {"s_range": (0.10, 0.35), "l_primary": 0.40}
    }
    
    @staticmethod
    def generate(
        seed: Optional[int] = None,
        theme_mode: str = "dark",  # 'dark', 'light', 'amoled'
        harmony: str = "analogous", # 'monochromatic', 'analogous', 'complementary', 'split-complementary', 'triadic', 'tetradic'
        mood: str = "futuristic",
        base_color: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate a complete reproducible semantic palette."""
        if seed is None:
            seed = random.randint(100000, 999999)
            
        rng = random.Random(seed)
        
        # Determine Base Hue and Saturation
        if base_color:
            try:
                base_r, base_g, base_b = hex_to_rgb(base_color)
                base_h, base_s, base_l = rgb_to_hsl(base_r, base_g, base_b)
            except Exception:
                base_h = rng.uniform(0, 360)
                base_s = 0.75
                base_l = 0.50
        else:
            base_h = rng.uniform(0, 360)
            mood_setting = PaletteEngine.MOOD_PARAMS.get(mood, PaletteEngine.MOOD_PARAMS["corporate"])
            base_s = rng.uniform(*mood_setting["s_range"])
            base_l = mood_setting["l_primary"]

        # Calculate Harmonies
        if harmony == "monochromatic":
            sec_h = base_h
            acc_h = base_h
        elif harmony == "complementary":
            sec_h = (base_h + 180) % 360
            acc_h = (base_h + 30) % 360
        elif harmony == "split-complementary":
            sec_h = (base_h + 150) % 360
            acc_h = (base_h + 210) % 360
        elif harmony == "triadic":
            sec_h = (base_h + 120) % 360
            acc_h = (base_h + 240) % 360
        elif harmony == "tetradic":
            sec_h = (base_h + 90) % 360
            acc_h = (base_h + 180) % 360
        else:  # analogous
            sec_h = (base_h + 35) % 360
            acc_h = (base_h - 35) % 360
            
        # Theme Mode Adaptations
        if theme_mode == "amoled":
            bg_hex = "#000000"
            surface_hex = hsl_to_hex(base_h, 0.08, 0.06)
            surface_elevated_hex = hsl_to_hex(base_h, 0.10, 0.11)
            text_primary_hex = "#ffffff"
            text_secondary_hex = "#a1a1aa"
            text_muted_hex = "#71717a"
            border_hex = hsl_to_hex(base_h, 0.06, 0.18)
            border_subtle_hex = hsl_to_hex(base_h, 0.05, 0.12)
            primary_hex = hsl_to_hex(base_h, min(base_s + 0.1, 1.0), 0.55)
            primary_hover_hex = hsl_to_hex(base_h, min(base_s + 0.1, 1.0), 0.62)
            primary_active_hex = hsl_to_hex(base_h, min(base_s + 0.1, 1.0), 0.48)
            secondary_hex = hsl_to_hex(sec_h, 0.70, 0.52)
            accent_hex = hsl_to_hex(acc_h, 0.85, 0.58)
            focus_ring_hex = primary_hex
        elif theme_mode == "light":
            bg_hex = hsl_to_hex(base_h, 0.08, 0.98)
            surface_hex = "#ffffff"
            surface_elevated_hex = hsl_to_hex(base_h, 0.06, 0.95)
            text_primary_hex = hsl_to_hex(base_h, 0.15, 0.10)
            text_secondary_hex = hsl_to_hex(base_h, 0.08, 0.35)
            text_muted_hex = hsl_to_hex(base_h, 0.05, 0.55)
            border_hex = hsl_to_hex(base_h, 0.10, 0.88)
            border_subtle_hex = hsl_to_hex(base_h, 0.08, 0.93)
            primary_hex = hsl_to_hex(base_h, min(base_s, 0.85), 0.45)
            primary_hover_hex = hsl_to_hex(base_h, min(base_s, 0.85), 0.38)
            primary_active_hex = hsl_to_hex(base_h, min(base_s, 0.85), 0.32)
            secondary_hex = hsl_to_hex(sec_h, 0.65, 0.42)
            accent_hex = hsl_to_hex(acc_h, 0.75, 0.46)
            focus_ring_hex = hsl_to_hex(base_h, 0.80, 0.45)
        else:  # dark mode default
            bg_hex = hsl_to_hex(base_h, 0.12, 0.06)
            surface_hex = hsl_to_hex(base_h, 0.10, 0.10)
            surface_elevated_hex = hsl_to_hex(base_h, 0.09, 0.15)
            text_primary_hex = "#f8fafc"
            text_secondary_hex = "#94a3b8"
            text_muted_hex = "#64748b"
            border_hex = hsl_to_hex(base_h, 0.08, 0.22)
            border_subtle_hex = hsl_to_hex(base_h, 0.06, 0.15)
            primary_hex = hsl_to_hex(base_h, min(base_s, 0.90), 0.58)
            primary_hover_hex = hsl_to_hex(base_h, min(base_s, 0.90), 0.65)
            primary_active_hex = hsl_to_hex(base_h, min(base_s, 0.90), 0.50)
            secondary_hex = hsl_to_hex(sec_h, 0.70, 0.54)
            accent_hex = hsl_to_hex(acc_h, 0.80, 0.60)
            focus_ring_hex = primary_hex

        # Semantic System States (Success, Warning, Error, Info)
        success_hex = "#10b981" if theme_mode != "light" else "#059669"
        warning_hex = "#f59e0b" if theme_mode != "light" else "#d97706"
        error_hex = "#ef4444" if theme_mode != "light" else "#dc2626"
        info_hex = "#06b6d4" if theme_mode != "light" else "#0284c7"

        # Gradient Recipes
        linear_gradient = f"linear-gradient(135deg, {primary_hex} 0%, {secondary_hex} 100%)"
        radial_gradient = f"radial-gradient(circle at 50% 0%, {primary_hex}22 0%, {bg_hex} 70%)"
        accent_mesh = f"linear-gradient(45deg, {primary_hex}33 0%, {accent_hex}33 50%, {secondary_hex}33 100%)"

        # Contrast calculations
        c_text_bg = get_contrast_ratio(text_primary_hex, bg_hex)
        c_text_surface = get_contrast_ratio(text_primary_hex, surface_hex)
        c_text_sec_bg = get_contrast_ratio(text_secondary_hex, bg_hex)
        
        # Primary button text color (choose white or dark for best contrast)
        c_btn_white = get_contrast_ratio("#ffffff", primary_hex)
        c_btn_black = get_contrast_ratio("#000000", primary_hex)
        btn_text_hex = "#ffffff" if c_btn_white >= c_btn_black else "#000000"
        c_btn_contrast = max(c_btn_white, c_btn_black)

        wcag_aa_compliant = (c_text_bg >= 4.5) and (c_text_surface >= 4.5) and (c_btn_contrast >= 3.0)

        tokens = {
            "background": bg_hex,
            "surface": surface_hex,
            "surface-elevated": surface_elevated_hex,
            "text-primary": text_primary_hex,
            "text-secondary": text_secondary_hex,
            "text-muted": text_muted_hex,
            "border": border_hex,
            "border-subtle": border_subtle_hex,
            "primary": primary_hex,
            "primary-hover": primary_hover_hex,
            "primary-active": primary_active_hex,
            "primary-foreground": btn_text_hex,
            "secondary": secondary_hex,
            "accent": accent_hex,
            "success": success_hex,
            "warning": warning_hex,
            "error": error_hex,
            "info": info_hex,
            "focus-ring": focus_ring_hex,
            "gradient-primary": linear_gradient,
            "gradient-ambient": radial_gradient,
            "gradient-mesh": accent_mesh
        }

        contrast_report = {
            "text_primary_on_background": round(c_text_bg, 2),
            "text_primary_on_surface": round(c_text_surface, 2),
            "text_secondary_on_background": round(c_text_sec_bg, 2),
            "button_text_on_primary": round(c_btn_contrast, 2),
            "wcag_22_aa_pass": wcag_aa_compliant
        }

        palette_id = f"pal-{theme_mode}-{harmony[:3]}-{mood[:3]}-{seed}"

        return {
            "palette_id": palette_id,
            "seed": seed,
            "theme_mode": theme_mode,
            "harmony": harmony,
            "mood": mood,
            "base_color": base_color or primary_hex,
            "tokens": tokens,
            "contrast_report": contrast_report
        }

    @staticmethod
    def generate_paired(
        seed: Optional[int] = None,
        harmony: str = "analogous",
        mood: str = "futuristic",
        base_color: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate synchronized light and dark palette pairs."""
        if seed is None:
            seed = random.randint(100000, 999999)
        dark_p = PaletteEngine.generate(seed=seed, theme_mode="dark", harmony=harmony, mood=mood, base_color=base_color)
        light_p = PaletteEngine.generate(seed=seed, theme_mode="light", harmony=harmony, mood=mood, base_color=base_color)
        return {
            "seed": seed,
            "dark": dark_p,
            "light": light_p
        }

    @staticmethod
    def to_css(tokens: Dict[str, str], selector: str = ":root") -> str:
        """Export tokens as CSS custom properties."""
        lines = [f"{selector} {{"]
        for key, val in tokens.items():
            lines.append(f"  --color-{key}: {val};")
        lines.append("}")
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Ultra UI/UX Pro Max Color Palette Engine")
    parser.add_argument("--seed", type=int, default=None, help="Reproducible integer seed")
    parser.add_argument("--theme", choices=["dark", "light", "amoled"], default="dark", help="Theme mode")
    parser.add_argument("--harmony", choices=["monochromatic", "analogous", "complementary", "split-complementary", "triadic", "tetradic"], default="analogous")
    parser.add_argument("--mood", choices=list(PaletteEngine.MOOD_PARAMS.keys()), default="futuristic")
    parser.add_argument("--base", type=str, default=None, help="Base hex color (e.g. '#6366f1')")
    parser.add_argument("--css", action="store_true", help="Output CSS variables instead of JSON")
    parser.add_argument("--paired", action="store_true", help="Generate synchronized dark & light pair")

    args = parser.parse_args()

    if args.paired:
        result = PaletteEngine.generate_paired(seed=args.seed, harmony=args.harmony, mood=args.mood, base_color=args.base)
        print(json.dumps(result, indent=2))
    else:
        palette = PaletteEngine.generate(seed=args.seed, theme_mode=args.theme, harmony=args.harmony, mood=args.mood, base_color=args.base)
        if args.css:
            print(PaletteEngine.to_css(palette["tokens"]))
        else:
            print(json.dumps(palette, indent=2))

if __name__ == "__main__":
    main()
