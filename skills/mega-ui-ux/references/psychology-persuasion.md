# Cognitive psychology, biases, persuasion and ethics

Use these to help people decide well and feel good about it. **Ethics gate:** a technique is allowed only if the user would still be glad of it after finding out how it worked. If not, it's a dark pattern. Don't use it.

## Cognitive principles

| Principle | What it says | Drives |
|---|---|---|
| **Recognition over recall** | Recognising is easier than remembering | Show recent items, suggestions, visible options, examples in empty fields; never make users remember things from a previous screen |
| **Cognitive load** (Sweller) | Intrinsic (the task) + extraneous (the UI) + germane (learning) | Kill extraneous load: decoration, ambiguity, jargon, redundant choices |
| **Progressive disclosure** | Reveal complexity as it's needed | Basics first, "advanced" behind a disclosure; staged forms |
| **Chunking** | Grouped info is easier to process | Sections, card numbers in groups of 4, steps |
| **Information scent** (Pirolli) | People follow cues that predict their goal | Specific link and button labels ("See 12 flats in Indiranagar" not "Learn more") |
| **Satisficing** (Simon) | People pick the first good-enough option | Make the best-for-most option the obvious first one |
| **Mental models** | People predict from experience | Use the vocabulary of the thing being replaced |
| **Locus of control** (Shneiderman) | People want to feel in charge | Undo, cancel, edit, preview; no surprise automation |
| **Flow** (Csikszentmihalyi) | Absorption when challenge matches skill | Remove interruptions mid-task; no modals during flow |
| **Emotional design** (Norman) | Visceral (looks), behavioural (works), reflective (meaning, identity) | Visceral polish for first impression, behavioural reliability, reflective pride (shareable outcomes, identity) |

## Biases (use honestly)

| Bias | Honest use | Dark use (forbidden) |
|---|---|---|
| **Anchoring** | Show the original price beside the real discount; a typical amount as a starting point | Inflated fake "was" prices |
| **Framing** | "98% delivered on time" for reassurance; frame in what the user gains | Misleading percentages |
| **Loss aversion** | "You'll lose your saved cart" only when true; protect progress | Fake "your account will be deleted" threats |
| **Default effect** | Pre-select the option best for most users (and say why) | Pre-ticked add-ons, opt-out marketing |
| **Endowment effect** | Free trial with real value; "your plan" personalisation | Hard-to-cancel trials |
| **IKEA effect** | Let users build or customise something (a profile, a plan); they value it more | Forced effort to raise switching costs |
| **Decoy effect** | A tier structure that clarifies value | Fake tiers designed to trick |
| **Status quo bias** | Keep familiar defaults when changing a design; migrate gently | — |
| **Sunk cost** | Show progress saved so people don't quit near the end | "You've come so far" guilt to block cancellation |
| **Commitment & consistency** | Small first step (save, wishlist) before the big one | Foot-in-the-door to sign up for unwanted subscriptions |
| **Mere exposure** | Consistent brand and patterns build familiarity | — |
| **Social proof** | Real counts, real reviews, "popular in your area" | Fake reviews, invented "23 people viewing" |
| **Scarcity / urgency** | Real stock or time limits, stated plainly | Fake timers, fake low stock |
| **Authority** | Credentials, regulators, certifications, expert endorsements that are real | Fake badges |
| **Reciprocity** | Give value first (a free tool or result) before asking | "Free" that requires card details without saying so |
| **Liking / unity** | Warm human tone, shared identity ("built by and for nurses") | Fake intimacy |
| **Peak-end** | Design the high and the ending | — |
| **Pratfall effect** | Admitting a small flaw raises trust ("We're slower than X but never lose a parcel") | — |
| **Labor illusion** | Show work being done for long operations ("Checking 340 airlines…") | Fake slowdowns |
| **Curiosity gap** | Previews that pull the user forward | Clickbait |

## Persuasion frameworks

- **Cialdini's 7:** reciprocity, commitment/consistency, social proof, authority, liking, scarcity, unity. Pick the 1–2 that match the persona's fear. A low-trust persona → authority + social proof. An aspirational persona → liking + unity.
- **Fogg behaviour model: B = MAP.** Behaviour happens when Motivation, Ability and a Prompt meet. When conversion fails, find which is missing: raise ability (make it simpler) before raising motivation (it's cheaper and more reliable). Prompts must arrive when motivation is high.
- **Hooked (Eyal):** trigger → action → variable reward → investment. Use only for habits the user wants (learning, fitness, savings). Never for compulsion.
- **Friction as a feature:** add deliberate friction before irreversible or risky actions (deleting, sending money, posting publicly): confirmation summaries, typed confirmation, undo windows.

## Dark patterns: never ship

Confirm-shaming, roach motel (easy in, hard out), hidden costs at the last step, sneak into basket, forced continuity, disguised ads, trick questions or double negatives, privacy zuckering, nagging, fake urgency or scarcity, bait and switch, obstruction of cancellation. If the brief asks for one, flag it and offer the honest alternative.
