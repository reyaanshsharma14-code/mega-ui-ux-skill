# Critique: reviewing an existing design and checking your own

Use this file in two places: **reviewing an existing screen** (when the input is a screenshot, Figma or Penpot frame, code, or a description) and the **self-critique** before every hand-over. Work top-down: don't polish pixels on a screen solving the wrong problem.

For a critique, have open `principle-selector.md` (the row for this screen's moment), `taste-signature.md` (generic tells and tests) and `psychology-persuasion.md` (the dark-pattern list). Look up other laws as you cite them.

## Order of review (go through every layer; problems in earlier layers rank higher)

1. **Job and persona:** does this screen serve the persona's job at this moment? Is anything here for the business rather than the user, and is it honest?
2. **Flow:** is this the right step? Could it be skipped, merged or deferred? Are the unhappy paths handled?
3. **Hierarchy:** one focal point? A clear reading order? Squint test passes?
4. **Principles:** check each selected principle is visibly applied (e.g. Fitts: is the primary action in the thumb zone and ≥48dp?).
5. **Heuristics:** quick pass through Nielsen's 10.
6. **Craft:** type scale, spacing scale, alignment axes, colour roles, states, microcopy, motion (ui-craft.md, sections 1–12).
7. **Taste:** generic-design tells and the five generic tests (taste-signature.md). Does the product have a signature moment? If not, name the moment that should become one.
8. **Accessibility and correctness:** run the ui-ux-pro-max pre-delivery checks (contrast, targets, focus, labels, reduced motion), or the WCAG list in heuristics-frameworks.md if it's unavailable.
9. **Ethics:** dark-pattern scan (psychology-persuasion.md).

## Critique output format (for reviewing someone else's design)

```
Verdict: <one sentence: what works, the biggest problem>
Persona assumed: <one line>

Fix first (changes outcomes):
1. <problem> → <fix>. Why: <principle> because <persona trait>.
2. ...

Then (craft and finesse):
- <problem> → <fix> (<principle>)

Keep (working well): <1–3 items, so they aren't lost in a redesign>
```

Persona here is compact: one line plus the 2–3 decision-driving traits. Rank by impact on the persona's job, not by how easy the fix is. When space is short, keep every "Fix first" item and cut "Then" items from the bottom. Every point names a principle and a fix. "Feels cluttered" alone is not a critique; "Two competing focal points (price and promo banner) → demote the banner to an inline line under the price (Von Restorff, focal point)" is.

## Self-critique gate (before hand-over)

Hand over only when all are true:
- [ ] Three or more visible decisions trace back to named persona traits.
- [ ] Each selected principle is visibly applied, not just listed.
- [ ] Swap test fails: this would look wrong with a competitor's logo.
- [ ] One focal point per screen; one primary action per screen.
- [ ] The signature moment exists and is custom.
- [ ] Key states designed: empty, loading, error, success (at minimum for the key screen).
- [ ] Copy is verb + object, in the persona's words; realistic data, not placeholders.
- [ ] Accessibility checks pass.
- [ ] No dark patterns.

If any box fails, fix it and re-check. Don't hand over with a known failure unless you name it.
