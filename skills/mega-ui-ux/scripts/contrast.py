#!/usr/bin/env python3
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
"""Compute WCAG 2.2 contrast ratios exactly instead of estimating them.

Usage:
  python contrast.py "#e8e2d2:#0e1512" "#a8340a:#ece6d8"
  python contrast.py --large "#ff5a1f:#0e1512"        # large text / UI thresholds
  python contrast.py --css styles.css                 # check all --on-X / --X pairs found

Each pair is "foreground:background" (hex, 3 or 6 digits, # optional).
Exit code 1 if any pair fails the chosen threshold, so it can gate CI.
"""
import argparse
import re
import sys


def parse_hex(h: str):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"bad colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def channel(c: int) -> float:
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb) -> float:
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    a, b = luminance(parse_hex(fg)), luminance(parse_hex(bg))
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r: float, large: bool) -> str:
    aa = 3.0 if large else 4.5
    aaa = 4.5 if large else 7.0
    if r >= aaa:
        return "AAA"
    if r >= aa:
        return "AA"
    return "FAIL"


def pairs_from_css(path: str):
    text = open(path, encoding="utf-8").read()
    vars_ = dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", text))
    pairs = []
    for name, val in vars_.items():
        m = re.match(r"on-(.+)", name)
        if m and m.group(1) in vars_:
            pairs.append((f"--{name} on --{m.group(1)}", val, vars_[m.group(1)]))
    for fg in ("text", "foreground", "fg", "ink", "cream", "muted", "muted-foreground"):
        for bg in ("bg", "background", "surface", "paper", "card", "ink", "ink-2"):
            if fg in vars_ and bg in vars_ and fg != bg:
                pairs.append((f"--{fg} on --{bg}", vars_[fg], vars_[bg]))
    return pairs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="*", help='"#fg:#bg" pairs')
    ap.add_argument("--large", action="store_true", help="use large-text/UI thresholds (3:1 AA)")
    ap.add_argument("--css", help="scan a CSS file for --on-X/--X and common fg/bg custom-property pairs")
    args = ap.parse_args()

    rows = []
    for p in args.pairs:
        fg, _, bg = p.partition(":")
        if not bg:
            ap.error(f"pair must look like '#fg:#bg', got {p!r}")
        rows.append((p, fg, bg))
    if args.css:
        rows += pairs_from_css(args.css)
    if not rows:
        ap.error("give at least one pair or --css file")

    failed = False
    for label, fg, bg in rows:
        r = ratio(fg, bg)
        v = verdict(r, args.large)
        failed |= v == "FAIL"
        print(f"{r:6.2f}:1  {v:<4}  {label}  ({fg} on {bg})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
