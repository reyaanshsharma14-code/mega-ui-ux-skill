#!/usr/bin/env python3
"""Multi-Platform Design Token Exporter for Mega UI/UX.

Generates WCAG-checked semantic design tokens from a base accent colour and outputs
ready-to-paste code for:
  - css          (Standard CSS custom properties with light + dark themes)
  - tailwind-v4  (Tailwind CSS v4 @theme block)
  - shadcn       (shadcn/ui CSS variables)
  - swiftui      (SwiftUI Theme.swift semantic Color & spacing tokens)
  - flutter      (Flutter Material 3 ThemeData in Dart)

Usage:
  python export_tokens.py --base "#ff5a1f" --target css
  python export_tokens.py --base "#ff5a1f" --target tailwind-v4
  python export_tokens.py --base "#ff5a1f" --target shadcn
  python export_tokens.py --base "#ff5a1f" --target swiftui
  python export_tokens.py --base "#ff5a1f" --target flutter
"""
import argparse
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_palette(base: str, mode: str) -> dict:
    cmd = [sys.executable, os.path.join(SCRIPT_DIR, "palette_engine.py"), "--theme", mode, "--base", base]
    out = subprocess.check_output(cmd, text=True, encoding="utf-8")
    return json.loads(out)["tokens"]


def emit_css(light: dict, dark: dict) -> str:
    lines = [':root, [data-theme="light"] {']
    for k, v in light.items():
        lines.append(f"  --{k}: {v};")
    lines.append("  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem;")
    lines.append("  --space-6: 1.5rem; --space-8: 2rem; --space-12: 3rem; --space-16: 4rem;")
    lines.append("  --radius-sm: 6px; --radius-md: 10px; --radius-lg: 16px;")
    lines.append('}\n\n[data-theme="dark"] {')
    for k, v in dark.items():
        lines.append(f"  --{k}: {v};")
    lines.append("}")
    return "\n".join(lines)


def emit_tailwind_v4(light: dict, dark: dict) -> str:
    return f"""@import "tailwindcss";

@theme {{
  --color-background: {dark['background']};
  --color-surface: {dark['surface']};
  --color-surface-elevated: {dark['surface-elevated']};
  --color-text-primary: {dark['text-primary']};
  --color-text-secondary: {dark['text-secondary']};
  --color-text-muted: {dark['text-muted']};
  --color-primary: {dark['primary']};
  --color-primary-foreground: {dark['primary-foreground']};
  --color-secondary: {dark['secondary']};
  --color-accent: {dark['accent']};
  --color-border: {dark['border']};
  --color-success: {dark['success']};
  --color-warning: {dark['warning']};
  --color-error: {dark['error']};
  --radius-sm: 0.375rem;
  --radius-md: 0.625rem;
  --radius-lg: 1rem;
}}
"""


def emit_shadcn(light: dict, dark: dict) -> str:
    return f""":root {{
  --background: {light['background']};
  --foreground: {light['text-primary']};
  --card: {light['surface']};
  --card-foreground: {light['text-primary']};
  --popover: {light['surface-elevated']};
  --popover-foreground: {light['text-primary']};
  --primary: {light['primary']};
  --primary-foreground: {light['primary-foreground']};
  --secondary: {light['secondary']};
  --secondary-foreground: {light['text-primary']};
  --muted: {light['surface']};
  --muted-foreground: {light['text-muted']};
  --accent: {light['accent']};
  --accent-foreground: {light['text-primary']};
  --destructive: {light['error']};
  --border: {light['border']};
  --input: {light['border']};
  --ring: {light['focus-ring']};
  --radius: 0.625rem;
}}

.dark {{
  --background: {dark['background']};
  --foreground: {dark['text-primary']};
  --card: {dark['surface']};
  --card-foreground: {dark['text-primary']};
  --popover: {dark['surface-elevated']};
  --popover-foreground: {dark['text-primary']};
  --primary: {dark['primary']};
  --primary-foreground: {dark['primary-foreground']};
  --secondary: {dark['secondary']};
  --secondary-foreground: {dark['text-primary']};
  --muted: {dark['surface']};
  --muted-foreground: {dark['text-muted']};
  --accent: {dark['accent']};
  --accent-foreground: {dark['text-primary']};
  --destructive: {dark['error']};
  --border: {dark['border']};
  --input: {dark['border']};
  --ring: {dark['focus-ring']};
}}
"""


def emit_swiftui(dark: dict) -> str:
    return f"""import SwiftUI

enum AppTheme {{
    static let background = Color(hex: "{dark['background']}")
    static let surface = Color(hex: "{dark['surface']}")
    static let surfaceElevated = Color(hex: "{dark['surface-elevated']}")
    static let textPrimary = Color(hex: "{dark['text-primary']}")
    static let textSecondary = Color(hex: "{dark['text-secondary']}")
    static let primary = Color(hex: "{dark['primary']}")
    static let secondary = Color(hex: "{dark['secondary']}")
    static let accent = Color(hex: "{dark['accent']}")
    static let border = Color(hex: "{dark['border']}")
    static let success = Color(hex: "{dark['success']}")
    static let warning = Color(hex: "{dark['warning']}")
    static let error = Color(hex: "{dark['error']}")
}}

extension Color {{
    init(hex: String) {{
        let cleaned = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: cleaned).scanHexInt64(&int)
        let r = Double((int >> 16) & 0xFF) / 255.0
        let g = Double((int >> 8) & 0xFF) / 255.0
        let b = Double(int & 0xFF) / 255.0
        self.init(.sRGB, red: r, green: g, blue: b, opacity: 1)
    }}
}}
"""


def emit_flutter(dark: dict) -> str:
    def c(h: str) -> str:
        return "0xFF" + h.lstrip("#").upper()

    return f"""import 'package:flutter/material.dart';

class AppTheme {{
  static ThemeData dark() {{
    const scheme = ColorScheme.dark(
      surface: Color({c(dark['surface'])}),
      onSurface: Color({c(dark['text-primary'])}),
      primary: Color({c(dark['primary'])}),
      onPrimary: Color({c(dark['primary-foreground'])}),
      secondary: Color({c(dark['secondary'])}),
      error: Color({c(dark['error'])}),
      outline: Color({c(dark['border'])}),
    );
    return ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: const Color({c(dark['background'])}),
      colorScheme: scheme,
    );
  }}
}}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="#ff5a1f", help="Base accent hex colour (e.g. #ff5a1f)")
    ap.add_argument("--target", choices=["css", "tailwind-v4", "shadcn", "swiftui", "flutter"], default="css")
    args = ap.parse_args()

    light = run_palette(args.base, "light")
    dark = run_palette(args.base, "dark")

    if args.target == "css":
        print(emit_css(light, dark))
    elif args.target == "tailwind-v4":
        print(emit_tailwind_v4(light, dark))
    elif args.target == "shadcn":
        print(emit_shadcn(light, dark))
    elif args.target == "swiftui":
        print(emit_swiftui(dark))
    elif args.target == "flutter":
        print(emit_flutter(dark))


if __name__ == "__main__":
    main()
