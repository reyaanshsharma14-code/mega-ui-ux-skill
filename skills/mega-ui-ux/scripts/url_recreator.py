import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
"""
Reference-Driven Website Recreation Engine for Ultra UI/UX Pro Max.
Author: ScraperDev BD (https://www.scraperdevbd.fun/)

Analyzes accessible public URLs or supplied HTML documents, extracts information
architecture, typography, color cues, navigation structures, and component trees,
and generates an implementation-ready design blueprint and scaffolding.
"""

import sys
import os
import re
import json
import urllib.request
import urllib.error
from html.parser import HTMLParser
from typing import Dict, Any, List, Optional

class DOMAnalyzer(HTMLParser):
    """Fast, zero-dependency HTML DOM and Design Token extractor."""
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.headings: List[Dict[str, str]] = []
        self.current_heading_tag = None
        self.current_heading_text = []
        self.nav_links: List[Dict[str, str]] = []
        self.buttons: List[str] = []
        self.current_button_text = []
        self.in_button = False
        self.images: List[Dict[str, str]] = []
        self.meta_tags: Dict[str, str] = {}
        self.font_links: List[str] = []
        self.inline_styles: List[str] = []
        self.section_tags: List[str] = []
        self.forms_count = 0
        self.classes: set = set()
        self.color_matches: set = set()

    def handle_starttag(self, tag: str, attrs: List[tuple]):
        attrs_dict = dict(attrs)
        
        # Track classes
        if "class" in attrs_dict:
            for cls in attrs_dict["class"].split():
                self.classes.add(cls)

        # Track inline styles and color cues
        if "style" in attrs_dict:
            style_val = attrs_dict["style"]
            self.inline_styles.append(style_val)
            # Find hex colors in styles
            hexes = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}\b", style_val)
            for h in hexes:
                self.color_matches.add(h.lower())

        if tag == "title":
            self.in_title = True
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.current_heading_tag = tag
            self.current_heading_text = []
        elif tag == "button":
            self.in_button = True
            self.current_button_text = []
        elif tag == "a" and "href" in attrs_dict:
            href = attrs_dict.get("href", "")
            if href and not href.startswith("javascript:"):
                # We will collect anchor text in handle_data if inside a nav
                self.nav_links.append({"href": href, "text": attrs_dict.get("title", "")})
        elif tag == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt", "")
            })
        elif tag == "meta":
            name = attrs_dict.get("name") or attrs_dict.get("property")
            content = attrs_dict.get("content")
            if name and content:
                self.meta_tags[name] = content
        elif tag == "link":
            rel = attrs_dict.get("rel", "")
            href = attrs_dict.get("href", "")
            if "stylesheet" in rel and ("font" in href or "google" in href or "type" in href):
                self.font_links.append(href)
        elif tag in ["section", "header", "nav", "main", "footer", "article", "aside"]:
            self.section_tags.append(tag)
        elif tag == "form":
            self.forms_count += 1

    def handle_endtag(self, tag: str):
        if tag == "title":
            self.in_title = False
        elif tag == self.current_heading_tag:
            text = "".join(self.current_heading_text).strip()
            if text:
                self.headings.append({"tag": self.current_heading_tag, "text": text})
            self.current_heading_tag = None
            self.current_heading_text = []
        elif tag == "button":
            text = "".join(self.current_button_text).strip()
            if text:
                self.buttons.append(text)
            self.in_button = False
            self.current_button_text = []

    def handle_data(self, data: str):
        if self.in_title:
            self.title += data.strip()
        elif self.current_heading_tag:
            self.current_heading_text.append(data)
        elif self.in_button:
            self.current_button_text.append(data)


def analyze_url(url: str, timeout: int = 10) -> Dict[str, Any]:
    """Fetch and analyze an accessible public URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 UltraUIUXProMax/1.0"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            html_content = response.read().decode("utf-8", errors="ignore")
            status_code = response.status
            final_url = response.geturl()
    except urllib.error.HTTPError as e:
        return {
            "success": False,
            "error_type": "HTTPError",
            "status_code": e.code,
            "message": f"HTTP Error {e.code}: {e.reason}",
            "fallback_instructions": (
                f"The target URL returned status {e.code}. To recreate this website:\n"
                "1. Provide a screenshot of the page using the Antigravity image context.\n"
                "2. Or supply saved HTML/CSS files directly in the workspace.\n"
                "3. Alternatively, specify the website's key brand colors, layout style, and required sections for an original recreation."
            )
        }
    except Exception as e:
        return {
            "success": False,
            "error_type": "ConnectionError",
            "message": str(e),
            "fallback_instructions": (
                "Unable to connect to the target URL directly (firewall, offline, or bot blocking).\n"
                "Fallback to screenshot-based or requirement-based recreation workflow."
            )
        }

    return analyze_html_content(html_content, source_url=final_url)


def analyze_html_content(html: str, source_url: str = "custom_document") -> Dict[str, Any]:
    """Parse HTML and extract architectural blueprint."""
    parser = DOMAnalyzer()
    parser.feed(html)
    
    # Infer fonts
    detected_fonts = []
    for link in parser.font_links:
        if "family=" in link:
            match = re.search(r"family=([^&:]+)", link)
            if match:
                detected_fonts.append(match.group(1).replace("+", " "))
    
    # Categorize sections
    sections_detected = list(set(parser.section_tags))
    
    # Structure synthesis
    blueprint = {
        "success": True,
        "source": source_url,
        "title": parser.title,
        "description": parser.meta_tags.get("description", ""),
        "og_title": parser.meta_tags.get("og:title", ""),
        "og_image": parser.meta_tags.get("og:image", ""),
        "detected_fonts": detected_fonts,
        "headings_hierarchy": parser.headings[:15],
        "key_buttons": parser.buttons[:10],
        "image_count": len(parser.images),
        "form_count": parser.forms_count,
        "detected_sections": sections_detected,
        "extracted_color_cues": list(parser.color_matches)[:10],
        "scaffolding_recommendations": {
            "layout_strategy": "Header -> Hero with H1 & CTA -> Bento Feature Grid -> Proof/Stats -> Footer",
            "typography_direction": detected_fonts[0] + " + Inter" if detected_fonts else "Plus Jakarta Sans + Inter",
            "form_complexity": "High" if parser.forms_count > 1 else ("Standard" if parser.forms_count == 1 else "None"),
            "target_viewport": "Mobile (<768px), Tablet (768-1024px), Desktop (>1024px)"
        }
    }
    return blueprint


def generate_scaffold_html(blueprint: Dict[str, Any]) -> str:
    """Generate a clean, accessible, modern HTML scaffold from the analyzed blueprint."""
    title = blueprint.get("title", "Recreated Web Interface")
    headings = blueprint.get("headings_hierarchy", [])
    h1_text = next((h["text"] for h in headings if h["tag"] == "h1"), title)
    
    buttons = blueprint.get("key_buttons", ["Get Started", "Learn More"])
    primary_cta = buttons[0] if buttons else "Get Started"
    secondary_cta = buttons[1] if len(buttons) > 1 else "Explore Features"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Ultra UI/UX Recreated</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --color-background: #090a0f;
      --color-surface: #12141c;
      --color-surface-elevated: #1a1d28;
      --color-text-primary: #f8fafc;
      --color-text-secondary: #94a3b8;
      --color-border: #262a38;
      --color-primary: #6366f1;
      --color-primary-hover: #4f46e5;
      --color-accent: #38bdf8;
      --font-display: 'Plus Jakarta Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
      --radius-sm: 6px;
      --radius-md: 12px;
      --radius-lg: 20px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background-color: var(--color-background);
      color: var(--color-text-primary);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.25rem 2rem;
      border-bottom: 1px solid var(--color-border);
      position: sticky;
      top: 0;
      background: rgba(9, 10, 15, 0.85);
      backdrop-filter: blur(12px);
      z-index: 50;
    }}
    .logo {{
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 1.25rem;
      letter-spacing: -0.02em;
      color: var(--color-text-primary);
    }}
    nav ul {{
      display: flex;
      gap: 1.5rem;
      list-style: none;
    }}
    nav a {{
      color: var(--color-text-secondary);
      text-decoration: none;
      font-size: 0.9375rem;
      font-weight: 500;
      transition: color 0.2s ease;
    }}
    nav a:hover, nav a:focus-visible {{
      color: var(--color-text-primary);
      outline: 2px solid var(--color-primary);
      outline-offset: 4px;
    }}
    .hero {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 6rem 2rem 4rem;
      text-align: center;
    }}
    .hero h1 {{
      font-family: var(--font-display);
      font-size: clamp(2.5rem, 5vw, 4.25rem);
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 1.5rem;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      color: var(--color-text-secondary);
      font-size: 1.25rem;
      max-width: 640px;
      margin: 0 auto 2.5rem;
    }}
    .cta-group {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .btn {{
      padding: 0.875rem 1.75rem;
      border-radius: var(--radius-md);
      font-weight: 600;
      font-size: 0.9375rem;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      transition: all 0.2s ease;
    }}
    .btn-primary {{
      background-color: var(--color-primary);
      color: #ffffff;
      border: 1px solid transparent;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
    }}
    .btn-primary:hover {{
      background-color: var(--color-primary-hover);
      transform: translateY(-1px);
    }}
    .btn-secondary {{
      background-color: var(--color-surface);
      color: var(--color-text-primary);
      border: 1px solid var(--color-border);
    }}
    .btn-secondary:hover {{
      background-color: var(--color-surface-elevated);
      border-color: #3b4255;
    }}
    .features {{
      max-width: 1200px;
      margin: 4rem auto;
      padding: 0 2rem;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.5rem;
    }}
    .card {{
      background-color: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 2rem;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .card:hover {{
      transform: translateY(-3px);
      border-color: var(--color-primary);
    }}
    .card h3 {{
      font-family: var(--font-display);
      font-size: 1.25rem;
      margin-bottom: 0.75rem;
    }}
    .card p {{
      color: var(--color-text-secondary);
      font-size: 0.9375rem;
    }}
    footer {{
      border-top: 1px solid var(--color-border);
      padding: 3rem 2rem;
      text-align: center;
      color: var(--color-text-secondary);
      font-size: 0.875rem;
      margin-top: 6rem;
    }}
    @media (max-width: 768px) {{
      header {{ padding: 1rem; }}
      nav {{ display: none; }}
      .hero {{ padding: 4rem 1rem 2rem; }}
      .features {{ padding: 0 1rem; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="logo">ScraperDev Studio</div>
    <nav aria-label="Main Navigation">
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#specs">Specifications</a></li>
        <li><a href="#docs">Documentation</a></li>
      </ul>
    </nav>
    <a href="#action" class="btn btn-primary" style="padding: 0.625rem 1.25rem;">{primary_cta}</a>
  </header>

  <main>
    <section class="hero">
      <h1>{h1_text}</h1>
      <p>Precision-engineered web interface recreated with modern responsive architecture, accessible semantic tokens, and fluid typography.</p>
      <div class="cta-group">
        <a href="#get-started" class="btn btn-primary">{primary_cta}</a>
        <a href="#learn-more" class="btn btn-secondary">{secondary_cta}</a>
      </div>
    </section>

    <section class="features" id="features">
      <div class="card">
        <h3>Architecture & Hierarchy</h3>
        <p>Engineered with semantic HTML5 landmarks, clear typography hierarchy, and robust layout responsiveness across all screen dimensions.</p>
      </div>
      <div class="card">
        <h3>Design System Tokens</h3>
        <p>WCAG 2.2 AA verified contrast ratios with flexible CSS custom properties, seamless dark mode support, and interactive focus indicators.</p>
      </div>
      <div class="card">
        <h3>Performance & Tactility</h3>
        <p>Optimized for zero Cumulative Layout Shift (CLS), lightweight typography loading, and tactile micro-interaction states.</p>
      </div>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 ScraperDev BD. Recreated using Ultra UI/UX Pro Max. All rights reserved.</p>
  </footer>
</body>
</html>
"""
    return html


def main():
    if len(sys.argv) < 2:
        print("Usage: python url_recreator.py <URL_OR_HTML_FILE> [--scaffold] [--output <FILE>]")
        sys.exit(1)

    target = sys.argv[1]
    do_scaffold = "--scaffold" in sys.argv
    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    if os.path.exists(target):
        with open(target, "r", encoding="utf-8") as f:
            content = f.read()
        result = analyze_html_content(content, source_url=target)
    elif target.startswith("http://") or target.startswith("https://"):
        result = analyze_url(target)
    else:
        print(f"Error: Target '{target}' is neither an accessible URL nor a valid file path.")
        sys.exit(1)

    if not result.get("success", False):
        print(json.dumps(result, indent=2))
        sys.exit(1)

    if do_scaffold:
        scaffold = generate_scaffold_html(result)
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(scaffold)
            print(f"Scaffold HTML written to {output_path}")
        else:
            print(scaffold)
    else:
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"Blueprint written to {output_path}")
        else:
            print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
