# Heuristics and frameworks

Used two ways: as **lenses while designing** (steps 2–5) and as a **checklist while critiquing** (step 8).

## Nielsen's 10 usability heuristics

1. **Visibility of system status:** always show what's happening (loading, saved, sent, step 2 of 4).
2. **Match with the real world:** user language, real-world order, familiar metaphors.
3. **User control and freedom:** clear exits, undo, cancel, back that works.
4. **Consistency and standards:** internal (same thing, same look) and external (platform conventions, Jakob's law).
5. **Error prevention:** constraints, smart defaults, confirmation for destructive actions, inline validation.
6. **Recognition rather than recall:** visible options, recent items, examples.
7. **Flexibility and efficiency:** shortcuts and accelerators for experts that are invisible to novices.
8. **Aesthetic and minimalist design:** every extra element competes with the relevant ones.
9. **Help users recognise, diagnose and recover from errors:** plain words, the cause, the fix; keep the user's input.
10. **Help and documentation:** contextual and searchable, and needed rarely.

## Norman's design principles (The Design of Everyday Things)

- **Affordance:** what an object allows. **Signifier:** what tells you so. Flat design kills signifiers. Tappable things must *look* tappable.
- **Mapping:** controls laid out like their effects (a slider for a range, a toggle for on/off, layout matching the real-world layout).
- **Feedback:** every action gets an immediate, proportionate response.
- **Constraints:** physical, logical and cultural limits that prevent errors (disable impossible options, input masks).
- **Conceptual model:** the user's understanding of how it works. The UI must teach a correct one.
- **Gulfs of execution and evaluation:** "how do I do it?" and "did it work?" Bridge both.
- **Slips vs mistakes:** slips (wrong action, right goal) need prevention and undo; mistakes (wrong goal) need better info.

## Shneiderman's 8 golden rules

Strive for consistency · universal usability (novice to expert) · informative feedback · dialogs that yield closure · prevent errors · easy reversal of actions · keep users in control · reduce short-term memory load.

## Dieter Rams: 10 principles of good design (taste anchor)

Innovative · useful · aesthetic · understandable · unobtrusive · honest · long-lasting · thorough down to the last detail · environmentally friendly · **as little design as possible** ("less, but better").

## Product frameworks

- **Jobs to be done:** people hire a product for progress in a circumstance. Frame every flow as "When ___, I want ___, so I can ___". Design for the job, not the feature.
- **Kano model:** basic (expected; absence enrages), performance (more is better), delighters (unexpected joy). Nail basics before delighters. Today's delighter becomes tomorrow's basic.
- **Double Diamond:** discover → define → develop → deliver. Don't skip "define": it's where the persona and the problem lock in.
- **HEART (Google):** Happiness, Engagement, Adoption, Retention, Task success. Pick the 1–2 signals the design should move.
- **Hierarchy of user needs:** functional → reliable → usable → convenient → pleasurable → meaningful. Never polish a layer whose foundation is broken.
- **Value proposition:** the first screen must answer "what is this, is it for me, what do I do next" within 5 seconds.

## Platform conventions (Jakob's law, made concrete)

- **Apple HIG:** clarity, deference (UI defers to content), depth. 44×44pt targets, SF type and Dynamic Type, tab bar ≤5, large titles, sheets, swipe-back, haptics with meaning, safe areas.
- **Material 3:** 48×48dp targets, dynamic colour roles (primary, secondary, tertiary, surface containers), elevation via tonal surfaces, FAB for the primary action, predictive back, motion that shows spatial relationships.
- **Web:** visible focus states, keyboard navigation, links that look like links, the browser back button works, URL reflects state, no hover-only meaning.

## Accessibility (non-negotiable; ui-ux-pro-max, if installed, checks the detail)

WCAG 2.2 AA: 4.5:1 text contrast (3:1 for large text and UI), targets at least 24px (aim 44/48), never colour alone for meaning, labels on inputs, focus visible and not obscured, reduced-motion support, screen-reader names and roles, no time limits without extension, accessible authentication (no puzzles), dragging has a single-pointer alternative. Inclusive design: **solve for one, extend to many.**
