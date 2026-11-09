# Flows, information architecture and patterns

## Designing a flow

1. **Start from the job and the end state.** What is true for the persona when it's done? Work backwards.
2. **List the minimum steps.** For each step ask: can the system do it (Tesler)? Can it be deferred until after first value? Can it merge with another step?
3. **Mark the decision points** (Hick), **trust moments** (where fear peaks), **effort spikes** (typing, uploading, waiting), the **peak** and the **end**.
4. **Map each step to one screen with one primary action.** Name the action as verb + object.
5. **Design the unhappy paths:** back, cancel, error, timeout, offline, interrupted (and resumed), permission denied, edit after commit.
6. **Plan returning use:** what does the second visit skip? (Remember choices, repeat last, shortcuts.)

Write the flow as: `Step → screen goal → primary action → principle(s) → what can go wrong`.

## Information architecture

- **Card-sort thinking:** group by the persona's mental model, not the org chart or the database.
- **Navigation depth vs breadth:** broad and shallow beats deep, up to around 5–7 top-level items. Mobile tab bar ≤5 (Apple HIG and Material).
- **Labels:** the persona's nouns; specific over clever ("Transfers", not "Flow").
- **Wayfinding:** the user always knows where they are (title, selected tab), where they can go, and how to get back.
- **Object-oriented UX:** identify the core objects (Transfer, Recipient, Account), their attributes and actions; screens are views of objects.

## Pattern playbook

**Onboarding:** value first, then account. Ask only what personalises the next screen. Show progress. Let the user skip and do later. First win under 60 seconds.

**Forms:** one column; labels above fields; group related fields; mark optional fields (not required ones) when most are required; the right input types and keyboards; autofill and autocomplete attributes; inline validation after blur, not while typing; the error under its field; keep values on error; a primary button that says the outcome; avoid splitting names or phones into many fields unless that's convention.

**Checkout / payment:** guest option; total, fees and delivery cost visible early; address autocomplete; saved methods; a review summary before the commit; the button names the amount; a confirmation with what happens next plus a receipt.

**Search:** visible search field (not just an icon) when search is primary; suggestions and recent searches; typo tolerance (Postel); results show why they matched; filters as chips with counts; zero results suggest alternatives.

**Lists and feeds:** consistent row anatomy (leading visual, title, meta, trailing action); swipe actions duplicated in a menu; pull to refresh where expected; infinite scroll for browsing, pagination for finding.

**Detail pages:** hero content first (the photo, the number, the name), the primary action sticky in reach, details progressively disclosed, related next steps.

**Dashboards:** one headline metric and its change; 3–5 supporting cards at most; everything clickable to the underlying list; empty and first-day states designed.

**Notifications:** permission asked in context after value is shown (not at launch); each notification specific and actionable; a preference centre.

**Trust patterns:** regulator and licence line, security cues at the moment of fear (not as a banner), real reviews, a human support route, transparent status timelines, a reversible-first design.

**Mobile specifics:** thumb-zone primary actions, bottom sheets over modals, safe areas, swipe-back, haptics on confirm, large titles, offline handling.

**Web specifics:** responsive from 360px, keyboard and focus, real links (middle-click works), hover never required, URL state for shareable views.
