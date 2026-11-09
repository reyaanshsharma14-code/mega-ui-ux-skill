# Google Stitch MCP Integration & Fallback Reference
**Author: ScraperDev BD** (https://www.scraperdevbd.fun/)

Ultra UI/UX Pro Max seamlessly bridges Antigravity's **Google Stitch MCP** service when available, and provides full autonomous operation when Stitch MCP is disconnected.

---

## 1. Connection Detection

The skill inspects local Antigravity MCP tooling at:
`~/.gemini/antigravity-ide/mcp/StitchMCP/`

Run the detector:
```bash
python scripts/stitch_connector.py
```

### Connected State
When connected, the following 15 tools are available:
- `create_project`: Initialize a new Stitch design project.
- `get_project`: Retrieve project details and metadata.
- `list_projects`: List all available Stitch projects.
- `generate_screen_from_text`: Generate high-fidelity screen designs from natural language descriptions.
- `generate_variants`: Explore alternate layout arrangements and color variations.
- `create_design_system`: Synthesize tokenized design systems.
- `apply_design_system`: Apply design tokens across screens.
- `edit_screens`, `list_screens`, `get_screen`, `upload_design_md`, `update_design_system`, etc.

### Calling Stitch MCP from Antigravity
```json
{
  "ServerName": "StitchMCP",
  "ToolName": "generate_screen_from_text",
  "Arguments": {
    "prompt": "Modern high-density fintech dashboard with candlestick charts and dark theme"
  }
}
```

---

## 2. Graceful Fallback Strategy (When Stitch is Not Connected)

If Stitch MCP is not configured or offline:
1. **Never Block Execution**: The agent informs the user that Stitch MCP is optional and proceeds immediately.
2. **Preset Library Fallback**: Automatically searches the built-in **260+ design presets** (`references/presets-catalog.json`) for the matching category and layout.
3. **Programmatic Palette**: Uses `scripts/palette_engine.py` to synthesize WCAG 2.2 AA compliant tokens.
4. **Direct Frontend Generation**: Employs semantic HTML5, modern CSS custom properties, and responsive design systems directly in the codebase.
