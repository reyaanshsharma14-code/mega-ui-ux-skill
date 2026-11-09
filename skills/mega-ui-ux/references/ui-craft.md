# UI craft: the rules behind finesse

Finesse is a hundred small decisions made on purpose. Work through these in this order: each layer depends on the one before it.

## 1. Hierarchy (decide before styling)

1. Write the screen's **reading order**: what the user must see 1st, 2nd and 3rd, and the one action.
2. Assign one **focal element**. Everything else is quieter.
3. Create emphasis with the **cheapest tool first**: position → size → weight → colour → container. A card or border is the last resort, not the first.
4. **De-emphasise to emphasise:** make secondary text lighter or smaller instead of making primary text louder.
5. Labels are secondary to values. "₹48,200" is big; "Family receives" is small and muted. Often the label can go entirely when the value explains itself.
6. One primary button per view. Secondary = outline or tonal; tertiary = text. Destructive = tertiary styling plus red text, confirmed.

## 2. Typography

- **Scale:** use a modular ratio. 1.2 (minor third) for dense apps, 1.25 (major third) for general UI, 1.333+ for editorial or marketing. Example at 16 base, ×1.25: 12.8 / 16 / 20 / 25 / 31 / 39 / 49.
- **Limit:** 1–2 families. Prefer one family with 3 weights (400/500/600 or 400/600/700). Use more sizes with fewer weights rather than the reverse.
- **Body:** 16px minimum on mobile and web (17pt iOS default). Line length 45–75 characters. Line height 1.4–1.6 for body, 1.1–1.25 for headings (larger type needs tighter leading).
- **Tracking:** tighten large headings (−1% to −2%); loosen small all-caps labels (+4% to +8%). Never track lowercase body text.
- **Numbers:** tabular figures for tables, prices and timers; proportional figures in prose. Align decimals.
- **Hierarchy through type alone:** a screen should read correctly in pure black and white with no boxes.
- **Hanging punctuation, real quotes (“ ”), en dashes for ranges (9–5), non-breaking spaces between a value and its unit (₹ 500, 10 km).**
- **Script support:** pick families that cover the persona's languages (Noto for Indic scripts, plus a native-feeling pairing). Indic and Arabic scripts need more line height.

## 3. Space and layout

- **Spacing scale on a 4/8 base:** 4, 8, 12, 16, 24, 32, 48, 64, 96. Never arbitrary values.
- **Proximity rule:** spacing inside a group < spacing between groups. A label sits closer to its field than to the field above.
- **Start with too much white space, then remove.** Crowding reads cheap; space reads confident.
- **Grid:** 4 columns on mobile (16–24 margins), 8 on tablet, 12 on desktop. Content max width around 1200px; text columns around 680px.
- **Alignment:** few, strong alignment axes. Everything on a shared left edge beats centring. Centre only short, symmetric content (confirmations, empty states).
- **Optical alignment over mathematical:** nudge icons in circular buttons, play triangles, and text next to icons. Round shapes overshoot the baseline a little.
- **Density by persona:** consumer and first-time = spacious; pro and daily = compact. One density per product.
- **Responsive:** design the smallest screen first; at larger sizes add columns, don't stretch.
- **Fluid rows:** in a row of text plus a button, the text column takes `flex:1; min-width:0` and wraps; the button keeps its size and drops to its own line when space runs out. Keep at least 12px between any button and its container edge, including inside centred overlays and lock cards.

## 4. Colour

- **Neutrals do most of the work** (around 90% of pixels). Build a 9–11 step neutral ramp, tinted slightly toward the brand hue (warm or cool) instead of pure grey.
- **One accent with a job.** The accent marks the primary action and the focal point. If it's everywhere, it means nothing. The 60-30-10 split is a starting heuristic, not a law.
- **Semantic roles:** primary, surface and surface-variant, on-surface, outline, success, warning, error, info. Tokens, never raw hex in components.
- **Meaning, not decoration:** colour signals state (selected, error, live, new). Pair it with shape, text or an icon for colour-blind users.
- **Choose the hue from the persona and brand feel, not the category cliché.** The cliché is the hue most of the category's best-known apps share (finance and health: blue or green; food: red or orange; AI: purple gradients). If you know or can look up the top competitors, check their primary colours. Ask what feeling *this* persona needs (calm? confident? warm?) and what distinguishes the brand from rivals.
- **Contrast:** 4.5:1 for text, 3:1 for UI and large text. Use APCA thinking for thin weights. Grey text on a coloured background: use a tint of the background hue, not grey.
- **Dark mode:** not inverted. Elevated surfaces get lighter; desaturate accents; avoid pure black (#0B0B0F–#121212) and pure white text (around 90% white).
- **Gradients and shadows:** subtle, a single light source, layered shadows (tight and dark plus wide and soft) instead of one blurry shadow.

## 5. Depth and surfaces

- Elevation should mean something: the active layer, overlays, draggable items.
- Prefer **tonal separation** (a slightly different surface) or **space** over borders. Use borders at low contrast (around 8–12% opacity) when necessary.
- **No card-in-card.** If you're nesting containers, remove one and use space or a divider.
- Corner radii: one family (e.g. 8/12/20), with nested radius = outer radius − padding.

## 6. Iconography and imagery

- One icon set, one stroke weight, one optical size. Icons always have labels unless universally known (search, close, back).
- Icons sized to match the cap height of the text beside them; optically centred.
- Imagery: real photography or purposeful illustration that belongs to the brand. Stock "people pointing at laptops" kills taste. Photo-first for emotional products (travel, food, homes).
- Every image has a defined aspect ratio, a placeholder (blur hash or a dominant colour), and alt text.

## 7. Components with restraint

- Before using a component, ask: **is there a simpler primitive?** A list row beats a card; text beats a chip; inline beats a modal.
- The tab bar appears only on top-level tab destinations. Any screen pushed from a tab (detail, tool, player, game, result) hides it and shows back or close instead (Apple HIG, Material). Immersive flows such as a quiz match or a video player hide it too.
- Modals only for interrupts that need a decision. Use sheets on mobile. Don't put a modal on top of a modal.
- Toasts for low-stakes confirmation with undo. Inline messages for errors.
- Tabs for peer views; segmented controls for filters of one view; a stepper only for a truly linear process.
- **Customise the 3–5 components that carry the signature moment**; keep the rest standard and quiet.

## 8. States (designed, not forgotten)

Each important screen has: **ideal · empty (first use, no results, cleared) · loading (skeleton matching the layout) · partial · error (inline, recoverable, input kept) · success · offline · permission denied · long content and edge data (long names, 0, 1, 10k items, RTL).** An empty state is an onboarding opportunity: explain the value plus one action. Empty, offline and error screens never waste the space: show what is saved on the device, a small illustration or motion, something to pass the time, and say what is safe ("your streak is kept").

## 9. Microcopy and voice

- Buttons are **verb + object**: "Send ₹48,200", not "Submit" or "OK".
- Write the way the persona speaks; use their nouns. Sentence case. Cut every word that doesn't help.
- Errors: what happened + why + how to fix, without blame. "That IFSC doesn't match a branch. Check the last 6 characters." Not "Invalid input".
- Empty states: value plus action. Confirmations: say exactly what will happen ("Ravi will get it by 6 pm").
- Voice stays constant; tone flexes with the moment (playful on success, calm on errors, serious on money).

## 10. Motion

- Motion must explain something: where a thing came from or went, what changed, what's connected (spatial continuity, Material motion).
- **Durations:** 100–200ms for micro feedback, 200–300ms for small transitions, 300–500ms for large or full-screen ones. Exits are faster than entrances.
- **Easing:** ease-out (decelerate) for entering, ease-in for exiting, standard ease-in-out for moving; springs for touch-driven motion.
- Animate transform and opacity only. Respect `prefers-reduced-motion`.
- One "hero" motion per flow at most (the peak moment). Everything else is quick and quiet.
- Disney principles in UI: anticipation (press states), follow-through (overshoot on sheets), staging (one thing moves at a time), slow in and out.

## 11. Data display

- Lead with the answer (one big number plus its meaning), then the detail.
- Right-align numbers; use tabular figures; use units and relative context ("↑ 12% vs last month").
- Charts: the simplest type that answers the question; direct labels instead of legends; muted context, one highlighted series. (For full chart rules, use the dataviz skill if present.)

## 12. Language, localisation and RTL

- Design with the persona's real language, not English placeholders. German and Malayalam can run 30–40% longer than English; let buttons and labels grow instead of truncating.
- RTL (Arabic, Urdu, Hebrew): mirror the layout, navigation, back arrows and progress direction. Don't mirror media controls, numbers, clocks or brand logos. Use logical CSS properties (`margin-inline-start`) or the platform's directionality.
- Format dates, numbers and currency per locale (₹1,00,000 in India; 1.000,00 € in Germany). Never build strings by concatenation; whole sentences go to translation.
- Let the user choose the language in its own script ("മലയാളം", not "Malayalam"); don't infer it only from the region.
- Icons and colours carry cultural meaning (red = luck in China, danger elsewhere). Check them for the persona's culture.

## 13. The last 10% (polish pass)

Pixel-snapped hairlines · consistent radii · icon and text baseline alignment · press, hover, focus and disabled states on every interactive element · haptics on meaningful confirmations (mobile) · no widows in headings (`text-wrap: balance`) · truncation with tooltips · skeletons that match the final layout · real-feeling sample data (not "Lorem ipsum" or "John Doe") · favicon, app icon and splash consistent · safe areas respected.
