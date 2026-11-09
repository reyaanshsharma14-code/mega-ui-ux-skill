import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
"""
Search & Discovery CLI for Ultra UI/UX Pro Max.
Author: ScraperDev BD (https://www.scraperdevbd.fun/)

Enables targeted querying of:
- 260+ curated, validated design presets (`references/presets-catalog.json`).
- 500+ verified research sources (`references/design-sources.json`).
- 150+ animation recipes (`references/animations-catalog.json`).
- 300+ custom & verified fonts across 40 categories (`references/fonts-catalog.json`).
- 200+ distinct background recipes across 50 categories (`references/backgrounds-catalog.json`).
- Dynamic design system synthesis with color tokens and layout guidance.
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)
REF_DIR = os.path.join(SKILL_ROOT, "references")
if not os.path.exists(REF_DIR):
    # Fallback to local references
    REF_DIR = os.path.join(os.path.dirname(SKILL_ROOT), "references")

def load_presets() -> List[Dict[str, Any]]:
    path = os.path.join(REF_DIR, "presets-catalog.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "presets-catalog.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_sources() -> List[Dict[str, Any]]:
    path = os.path.join(REF_DIR, "design-sources.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "design-sources.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_animations() -> List[Dict[str, Any]]:
    path = os.path.join(REF_DIR, "animations-catalog.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "animations-catalog.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_fonts() -> Dict[str, Any]:
    path = os.path.join(REF_DIR, "fonts-catalog.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "fonts-catalog.json")
    if not os.path.exists(path):
        return {"categories": [], "fonts": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_backgrounds() -> Dict[str, Any]:
    path = os.path.join(REF_DIR, "backgrounds-catalog.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "backgrounds-catalog.json")
    if not os.path.exists(path):
        return {"categories": [], "recipes": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_layouts() -> Dict[str, Any]:
    path = os.path.join(REF_DIR, "layouts-catalog.json")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "references", "layouts-catalog.json")
    if not os.path.exists(path):
        return {"categories": [], "patterns": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def search_layouts(query: str, category: str = None, limit: int = 5) -> List[Dict[str, Any]]:
    catalog = load_layouts()
    patterns = catalog.get("patterns", [])
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for p in patterns:
        score = 0
        if cat_lower and (cat_lower in p.get("category_name", "").lower() or cat_lower == p.get("category_code", "").lower()):
            score += 10
        if query_lower:
            if query_lower in p.get("name", "").lower():
                score += 10
            if query_lower in p.get("category_name", "").lower():
                score += 6
            if query_lower in p.get("css_layout_model", "").lower():
                score += 5
            if query_lower in p.get("description", "").lower():
                score += 4
            for s in p.get("suitable_use_cases", []):
                if query_lower in s.lower():
                    score += 3
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, p))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in results[:limit]]

def search_animations(query: str, category: str = None, limit: int = 5) -> List[Dict[str, Any]]:
    animations = load_animations()
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for a in animations:
        score = 0
        if cat_lower and cat_lower in a["category"].lower():
            score += 10
        if query_lower:
            if query_lower in a["name"].lower():
                score += 8
            if query_lower in a["category"].lower():
                score += 6
            if query_lower in a.get("technology", "").lower():
                score += 5
            if query_lower in a.get("explanation", "").lower():
                score += 4
            for u in a.get("use_cases", []):
                if query_lower in u.lower():
                    score += 3
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, a))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [a for _, a in results[:limit]]

def search_fonts(query: str, category: str = None, limit: int = 5) -> List[Dict[str, Any]]:
    catalog = load_fonts()
    fonts = catalog.get("fonts", [])
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for f in fonts:
        score = 0
        if cat_lower and cat_lower in f.get("category_name", "").lower():
            score += 10
        if query_lower:
            if query_lower in f.get("family", "").lower():
                score += 10
            if query_lower in f.get("category_name", "").lower():
                score += 6
            if query_lower in f.get("role", "").lower():
                score += 5
            if query_lower in f.get("designer_or_foundry", "").lower():
                score += 4
            for s in f.get("suitable_for", []):
                if query_lower in s.lower():
                    score += 3
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, f))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [f for _, f in results[:limit]]

def search_backgrounds(query: str, category: str = None, limit: int = 5) -> List[Dict[str, Any]]:
    catalog = load_backgrounds()
    recipes = catalog.get("recipes", [])
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for r in recipes:
        score = 0
        if cat_lower and cat_lower in r.get("category_name", "").lower():
            score += 10
        if query_lower:
            if query_lower in r.get("name", "").lower():
                score += 8
            if query_lower in r.get("category_name", "").lower():
                score += 6
            if query_lower in r.get("type", "").lower():
                score += 5
            if query_lower in r.get("description", "").lower():
                score += 4
            for t in r.get("supported_tech", []):
                if query_lower in t.lower():
                    score += 3
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, r))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in results[:limit]]

def search_presets(query: str, category: str = None, limit: int = 5) -> List[Dict[str, Any]]:
    presets = load_presets()
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for p in presets:
        score = 0
        if cat_lower and cat_lower in p["category"].lower():
            score += 10
        if query_lower:
            if query_lower in p["name"].lower():
                score += 8
            if query_lower in p["visual_style"].lower():
                score += 6
            if query_lower in p["category"].lower():
                score += 5
            if query_lower in p["layout_pattern"].lower():
                score += 4
            for s in p.get("suitable_projects", []):
                if query_lower in s.lower():
                    score += 3
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, p))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in results[:limit]]

def search_sources(query: str, category: str = None, limit: int = 8) -> List[Dict[str, Any]]:
    sources = load_sources()
    query_lower = query.lower() if query else ""
    cat_lower = category.lower() if category else ""
    
    results = []
    for s in sources:
        score = 0
        if cat_lower and cat_lower in s.get("category", "").lower():
            score += 10
        if query_lower:
            if query_lower in s.get("name", "").lower():
                score += 8
            if query_lower in s.get("category", "").lower():
                score += 6
            if query_lower in s.get("resource_type", "").lower():
                score += 4
        if score > 0 or (not query_lower and not cat_lower):
            results.append((score, s))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in results[:limit]]

def generate_design_system(query: str, project_name: str = "Modern Web Project") -> Dict[str, Any]:
    """Synthesize complete design system specification."""
    matching_presets = search_presets(query, limit=1)
    preset = matching_presets[0] if matching_presets else load_presets()[0]
    
    try:
        from palette_engine import PaletteEngine
    except ImportError:
        import importlib.util
        pal_path = os.path.join(SCRIPT_DIR, "palette_engine.py")
        spec = importlib.util.spec_from_file_location("palette_engine", pal_path)
        pe_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pe_module)
        PaletteEngine = pe_module.PaletteEngine

    theme = "dark"
    if "light" in query.lower() or "white" in query.lower():
        theme = "light"
    elif "amoled" in query.lower() or "oled" in query.lower():
        theme = "amoled"
        
    mood = "futuristic"
    for m in PaletteEngine.MOOD_PARAMS.keys():
        if m in query.lower():
            mood = m
            break

    palette = PaletteEngine.generate(theme_mode=theme, mood=mood)
    sources = search_sources(preset["category"], limit=3)
    matching_fonts = search_fonts(preset["category"], limit=3)
    matching_bg = search_backgrounds(preset["category"], limit=2)

    return {
        "project": project_name,
        "query": query,
        "recommended_preset": {
            "id": preset["id"],
            "name": preset["name"],
            "category": preset["category"],
            "visual_style": preset["visual_style"],
            "layout_pattern": preset["layout_pattern"],
            "typography_direction": preset["typography_direction"],
            "spacing_density": preset["spacing_density"],
            "component_patterns": preset["component_patterns"],
            "animation_strategy": preset["animation_strategy"],
            "accessibility_considerations": preset["accessibility_considerations"]
        },
        "color_tokens": palette["tokens"],
        "contrast_validation": palette["contrast_report"],
        "recommended_typography": [
            {"family": f["family"], "role": f["role"], "source": f["verified_source"], "import": f["css_import"]}
            for f in matching_fonts
        ],
        "recommended_backgrounds": [
            {"name": b["name"], "type": b["type"], "tech": b["supported_tech"]}
            for b in matching_bg
        ],
        "curated_inspiration_sources": sources,
        "implementation_checklist": [
            "Use semantic HTML5 elements (header, nav, main, section, footer, article)",
            "Enforce base 16px body font size with line-height >= 1.5",
            "Maintain WCAG 2.2 AA contrast >= 4.5:1 for normal text and >= 3:1 for controls",
            "Implement visible focus rings (:focus-visible) for keyboard accessibility",
            "Ensure touch targets are at least 44x44px on mobile viewports",
            "Add prefers-reduced-motion media query fallback for all animations",
            "Never use static emojis as interface icons - use SVG icons only"
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="Ultra UI/UX Pro Max Discovery Engine")
    parser.add_argument("query", nargs="?", default="", help="Search query (e.g. 'developer portfolio', 'shuriken', 'mesh gradient')")
    parser.add_argument("--category", "-c", type=str, default=None, help="Filter by category")
    parser.add_argument("--preset", action="store_true", help="Search design presets specifically")
    parser.add_argument("--source", action="store_true", help="Search research source registry specifically")
    parser.add_argument("--animation", "-a", action="store_true", help="Search 150+ animation recipes specifically")
    parser.add_argument("--font", "-f", action="store_true", help="Search 300+ custom & verified fonts")
    parser.add_argument("--background", "-b", action="store_true", help="Search 200+ distinct background recipes")
    parser.add_argument("--layout", "-y", action="store_true", help="Search 120+ distinct layout patterns")
    parser.add_argument("--design-system", "-d", action="store_true", help="Generate complete design system specification")
    parser.add_argument("--project", "-p", type=str, default="Antigravity Project", help="Project name for design system")
    parser.add_argument("--limit", "-l", type=int, default=5, help="Number of results to display")
    parser.add_argument("--list-categories", action="store_true", help="List all 25 preset categories")
    parser.add_argument("--list-animation-categories", action="store_true", help="List all 15 animation categories")
    parser.add_argument("--list-font-categories", action="store_true", help="List all 40 font categories")
    parser.add_argument("--list-background-categories", action="store_true", help="List all 50 background categories")
    parser.add_argument("--list-layout-categories", action="store_true", help="List all 11 layout categories")

    args = parser.parse_args()

    if args.list_categories:
        presets = load_presets()
        categories = sorted(list(set(p["category"] for p in presets)))
        print(f"Total Preset Categories: {len(categories)}")
        for idx, cat in enumerate(categories, 1):
            count = sum(1 for p in presets if p["category"] == cat)
            print(f"{idx:02d}. {cat} ({count} presets)")
        return

    if args.list_animation_categories:
        animations = load_animations()
        categories = sorted(list(set(a["category"] for a in animations)))
        print(f"Total Animation Categories: {len(categories)}")
        for idx, cat in enumerate(categories, 1):
            count = sum(1 for a in animations if a["category"] == cat)
            print(f"{idx:02d}. {cat} ({count} recipes)")
        return

    if args.list_font_categories:
        catalog = load_fonts()
        cats = catalog.get("categories", [])
        print(f"Total Font Categories: {len(cats)}")
        for c in cats:
            count = sum(1 for f in catalog.get("fonts", []) if f["category_id"] == c["id"])
            print(f"{c['id']:02d}. {c['name']} ({count} fonts)")
        return

    if args.list_background_categories:
        catalog = load_backgrounds()
        cats = catalog.get("categories", [])
        print(f"Total Background Categories: {len(cats)}")
        for c in cats:
            count = sum(1 for r in catalog.get("recipes", []) if r["category_id"] == c["id"])
            print(f"{c['id']:02d}. {c['name']} ({count} recipes)")
        return

    if args.list_layout_categories:
        catalog = load_layouts()
        cats = catalog.get("categories", [])
        print(f"Total Layout Categories: {len(cats)}")
        for c in cats:
            count = sum(1 for p in catalog.get("patterns", []) if p.get("category_code") == c.get("code"))
            print(f"{c['code']}. {c['name']} ({count} patterns)")
        return

    if args.design_system:
        ds = generate_design_system(args.query, project_name=args.project)
        print(json.dumps(ds, indent=2))
        return

    if args.layout:
        results = search_layouts(args.query, category=args.category, limit=args.limit)
        print(json.dumps(results, indent=2))
        return

    if args.font:
        results = search_fonts(args.query, category=args.category, limit=args.limit)
        print(json.dumps(results, indent=2))
        return

    if args.background:
        results = search_backgrounds(args.query, category=args.category, limit=args.limit)
        print(json.dumps(results, indent=2))
        return

    if args.animation:
        results = search_animations(args.query, category=args.category, limit=args.limit)
        print(json.dumps(results, indent=2))
        return

    if args.source:
        results = search_sources(args.query, category=args.category, limit=args.limit)
        print(json.dumps(results, indent=2))
        return

    # Default to preset search
    results = search_presets(args.query, category=args.category, limit=args.limit)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
