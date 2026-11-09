# Taste: escaping the generic

Generic design comes from **defaults**: the kit's components, the category's colours, the template's layout. Taste is choosing on purpose, from the persona outward.

## The feel statement

Before any visuals, write 2–3 words for how the product should feel to this persona, plus one word it must **not** feel like.
- Wise: *honest, exact, calm*. Not: *flashy*.
- Airbnb: *warm, human, inviting*. Not: *corporate*.
- Apple: *confident, effortless, precise*. Not: *busy*.
- Google: *helpful, fast, clear*. Not: *ornamental*.

Every visual choice (type, colour, radius, motion, density, imagery, copy) must be defensible against these words. Example: "calm" → generous space, low saturation, slow ease-out, no exclamation marks.

## Transferable lessons from the bar-setters (principles, not imitation)

| Company | Signature habit | Principle to transfer |
|---|---|---|
| **Wise** | Fee and rate shown up front, arrival time, transparent breakdown | **Honesty as the design.** Put the thing competitors hide at the centre of the screen |
| **Wise** | Bold, flat, bright accent; big friendly numbers | One confident accent; the number is the hero |
| **Airbnb** | Photo-first listings; the host as a person; reviews woven in | **Let content be the interface.** Imagery and people carry trust and emotion |
| **Airbnb** | Category icons and the "flexible" search | Lower the cost of starting when the user doesn't know exactly what they want |
| **Apple** | One bold idea per screen; giant type; white space; product as hero | **Restraint.** Remove until one idea remains. Deference: UI steps back for content |
| **Apple** | Motion with physics; haptics that confirm | Feedback felt, not just seen |
| **Google** | Search box as the whole product; Material motion explains space | **Speed and clarity** beat ornament; motion as explanation |
| **Stripe** | Docs and dashboards that respect expert users; exquisite detail | **Craft in the unglamorous parts** (errors, tables, empty states) |
| **Linear** | Keyboard-first, opinionated, fast, dark-capable, dense yet calm | Opinionated defaults for power personas; speed is a feature |
| **Duolingo** | Peak-end celebration, character, streaks | **Emotion at the peak**, with personality in voice and motion |
| **Monzo / Revolut** | Real-time notifications; spending made visible | Instant feedback builds trust in money products |
| **Headspace / Calm** | Pace, colour and illustration that slow you down | The UI's tempo can match the desired emotional state |

## The signature moment

Each flow gets **one** moment where the craft effort concentrates: the thing a user would screenshot or describe to a friend. Pick it from the persona's peak emotion or biggest fear:
- Fear of hidden cost → a fee breakdown so clear it *becomes* the brand (Wise).
- Anticipation → an immersive preview (Airbnb listing photos).
- Achievement → a celebration at the end (Duolingo lesson complete).
- Anxiety about status → a live tracking timeline (delivery, transfer).

Rules: one per flow. Custom-designed (not a kit component). Supports the job; never delays it. Everything around it stays quiet so it stands out (Von Restorff).

## Generic-design tells (find and replace)

| Tell | Replace with |
|---|---|
| Everything in cards, card-in-card | Space, alignment, tonal surfaces, list rows |
| Default kit blue / category-cliché colour | A hue chosen from the feel statement; neutrals tinted toward it |
| Equal visual weight everywhere | One focal point; de-emphasised labels |
| Centred everything | Strong left alignment; centre only short, symmetric content |
| "Submit", "Learn more", "Get started" | Verb + object in the persona's words |
| Stock illustration or people photos | Real product, real content, purposeful brand illustration, or none |
| Hero + 3 feature icons + testimonial carousel | A structure derived from the persona's questions in order |
| Gradient blobs, glassmorphism or neon for no reason | A material that matches the feel statement |
| Emoji as icons | One consistent icon set |
| Lorem ipsum, John Doe, round numbers | Realistic, persona-specific data (₹48,200, Sunita Devi) |
| Same radius, shadow and spacing as every Tailwind or shadcn demo | A deliberate token set derived from the feel |
| Motion everywhere or nowhere | One meaningful hero motion; quick, quiet feedback elsewhere |
| Generic empty states ("No data") | Value + one action, in voice |

## The generic test (must pass)

1. **Swap test:** put a competitor's logo on it. Does it still fit? If yes, it isn't designed yet.
2. **Persona test:** point to three elements that exist *because of this persona*. If you can't, go back to the persona.
3. **Squint test:** blur it. Is there one obvious focal point and a reading order?
4. **Remove test:** remove one element at a time. If nothing is lost, keep it removed.
5. **Screenshot test:** is there a moment someone would screenshot? That's the signature moment.
