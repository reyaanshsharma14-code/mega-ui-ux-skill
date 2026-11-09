# Producing screens: choosing the medium and building in it

## Choosing the medium

| Situation | Medium |
|---|---|
| Input is code or a built screen inside a repo | **Repo code** (no question) |
| User names a medium | That medium |
| Inside a repo, new design, and Penpot or Figma is also connected | Ask once: "Code in this repo, or a design in Penpot/Figma?" |
| Not in a repo; Penpot or Figma connected | Ask once: "Penpot/Figma, or an HTML mockup?" |
| Nothing connected | **HTML mockup** |

"Connected" means its MCP tools are actually listed in this session (`mcp__penpot__*`, a Figma MCP with write tools). A server that failed to connect doesn't count; mention the failure in one line.

## Tokens first (all mediums)

Before building, write the token set derived from the feel statement: neutral ramp (tinted), one accent plus semantic colours, type scale (ratio and sizes), spacing scale, radii, elevation, motion durations and easing. If the optional ui-ux-pro-max skill is installed, use it for **correctness** inputs (skip this block if it isn't; the WCAG list in `heuristics-frameworks.md` covers the essentials):

```bash
UUPM=$(ls -d ~/.claude/plugins/cache/ui-ux-pro-max-skill/ui-ux-pro-max/*/.claude/skills/ui-ux-pro-max | sort -V | tail -1)
python3 "$UUPM/scripts/search.py" "<one concern, 2-5 words>" --domain ux        # e.g. "form error inline validation"
python3 "$UUPM/scripts/search.py" "<component concern>" --stack <stack>         # e.g. --stack flutter
```

Its pre-delivery checklist is in `$UUPM/references/pro-rules.md` (section "Pre-Delivery Checklist"). For mockups (HTML, Penpot, Figma), apply only its visual items: contrast, target sizes, type sizes, focus and pressed states, safe areas, states. Apply the full list to repo code.

Record the tokens where the medium keeps them (CSS custom properties, the project's theme file, Penpot assets), with a comment linking each group to its feel word.

**Light or dark:** build what the persona's context needs. Night-time use or a media or pro tool means dark first; a project that already supports both needs both; otherwise light only, with dark listed under "Not checked". Don't use its `--design-system` palette or style output as the look. Taste comes from the feel statement. You may use its font-pairing search when the feel needs a pairing. If `$UUPM` is empty, say "ui-ux-pro-max not installed, using built-in checks" and use the WCAG list in heuristics-frameworks.md.

## Repo code

1. Detect the stack (`pubspec.yaml` → Flutter, `package.json` deps → React/Next/Vue/Svelte, `*.xcodeproj` → SwiftUI, etc.).
2. **Reuse the project's design system first**: its theme, tokens and components. Add craft through hierarchy, spacing, copy, states and the signature moment. Only introduce new tokens when the project has none or the user asked for a new look; put them where the project keeps its theme.
3. Edit in the working tree. Never commit or push unless asked.
4. Build every key state (empty, loading, error, success) with realistic sample data.
5. Run it and look at it (the project's run skill or dev server; Claude in Chrome for web; a simulator screenshot for mobile). Fix what you see. Code that wasn't looked at isn't done.

## HTML mockup

- One self-contained file: inline CSS, CSS custom properties for the tokens, Google Fonts if needed, no build step. Mobile personas: render inside a 390×844 frame; web: responsive from 360px.
- Show every key screen of the flow side by side (or as sections), plus the key states for the signature screen.
- Real content and data in the persona's language. Under each screen, a one-line caption giving the screen's job and the principle behind it (this teaches the reader).
- Save to the project's `design/` folder if in a project, otherwise the session scratchpad. Look at it rendered before hand-over: Claude in Chrome, or a headless screenshot you then view:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=<out.png> --window-size=1400,1000 file://<file.html>`
  Fix what you see, then open it for the user (`open <file>`).

## Penpot

1. Call `mcp__penpot__high_level_overview` first and follow it.
2. One board per screen, named `<flow> / <step> / <state>`. Use flex layout. Create colour and typography assets from the tokens before drawing.
3. Export the key board (`mcp__penpot__export_shape`) and look at it before hand-over.

## Figma

Use whatever write-capable Figma tools are connected and follow their instructions. If only read or dev-mode tools are available, read the existing file for critique, and produce new screens as HTML or code instead, saying why.
