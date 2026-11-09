# Example prompts

The skill sizes the run from the request.

## Full run
- "Design the booking flow for a small-group trekking company. It must not look like a template."
- "Redesign the checkout in this repo. People drop off at payment."
- "Build a landing page with a scroll-driven 3D scene for a mountain guide service."

You get persona, feel, principles, flow and a signature moment, then a checkpoint, then the build, rendered checks and a review council.

## Critique
- "Review this screenshot of our pricing page."
- "Critique the settings screen in `app/settings/`."

## Light run
- "Fix this empty state."
- "Make the primary button on this form clearer."

## Principle questions
- "Is a countdown timer on this offer a dark pattern?"
- "Which UX laws apply to a plan picker for small businesses?"

## Tools
- `python skills/mega-ui-ux/scripts/search.py "fitness app dark" --design-system`
- `python skills/mega-ui-ux/scripts/contrast.py "#e8e2d2:#0e1512" "#a8340a:#ece6d8"`
- `python skills/mega-ui-ux/scripts/audit.py index.html`
- `python skills/mega-ui-ux/scripts/palette_engine.py --theme dark --base "#6366f1" --css`
