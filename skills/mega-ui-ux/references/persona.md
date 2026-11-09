# Persona: building one that changes decisions

A persona is a **decision tool**, not a profile. If removing a trait wouldn't change any screen, the trait is noise. Every persona is a hypothesis: label it as such and invite correction.

## The persona card (fill every field)

| Field | Question it answers | Example (booking a child's doctor visit) |
|---|---|---|
| **Who, specifically** | One person, with a name, role and one-line situation | Meera, 36, school teacher in Pune, books for her 6-year-old |
| **Job to be done** | "When ___, I want to ___, so I can ___" | When my son has a fever at night, I want the earliest slot with his own paediatrician, so I don't miss a school day |
| **Stakes** | What does failure cost them? | A sick child waiting; a lost workday; guilt |
| **Fears and trust level** | What would make them abandon? | Slot vanishing at payment, an unknown doctor, hidden consultation fees |
| **Context of use** | Device, place, time, attention, connectivity | Phone in one hand, child on her lap, 11 pm, anxious |
| **Literacy and language** | Reading level, digital fluency, language | Fluent English and Marathi, comfortable with apps |
| **Acts for whom** | Themselves only, or also on behalf of others (family, friends, clients), and out of curiosity about others? | Books for her son; also checks her mother's appointments |
| **Frequency** | First-time, occasional, daily, power user | A few times a year, always under stress |
| **Mental model** | What do they compare this to? | Calling the clinic receptionist who knows her son |
| **Success feels like** | The emotion at the end | Relief: "it's sorted, I can sleep" |
| **Decision-driving traits** | The 2–3 traits that most change design | Anxious + one-handed + wants *their* doctor |

## How to infer from thin input

1. Product and problem statement → who has this problem most acutely? Design for the **most constrained realistic user**. Accessibility and clarity gains carry up to everyone else (curb-cut effect).
2. Find the **stakes** first: money, health, time, identity, social standing. High stakes → trust and clarity beat delight.
3. Find the **context**: one-handed? noisy? rushing? first-time? These map directly to laws (Fitts, Hick, cognitive load).
4. Find the **mental model**: what physical or familiar thing are they replacing? Mirror its vocabulary (Jakob's law, conceptual model).
5. If two personas pull in opposite directions, name a **primary** persona and a **secondary** one. Design for the primary; don't break the secondary.

Ask the user only if a missing answer would flip a major decision (e.g. "Is this for first-time investors or traders?"). Otherwise state assumptions in one line each.

## Trait → decision map (examples)

| Trait signal | Decisions it drives |
|---|---|
| Low trust / high stakes | Show fees and totals up front, a confirmation summary, recognisable trust marks, a status timeline, no surprises, a human-sounding tone |
| Acts for others, or curious about others | Saved people as one-tap chips ("who is this for?" first), the subject's name visible on every result with a switch, privacy stated where their data appears, results easy to share with that person |
| Tired, distracted, rushing | One task per screen, big targets, smart defaults, resumable progress, no required reading |
| First-time | Progressive disclosure, an example or preview of the result, an undo/escape, plain words, no jargon |
| Power user / daily | Density, shortcuts, remembered choices, batch actions, skip the onboarding |
| Low literacy / second language | Icons with labels, numbers and visuals over text, short sentences, a familiar script, voice option |
| Emotional / aspirational purchase | Imagery first, social proof, story, space to dream, a light commitment first (save, wishlist) |
| Professional / analytical | Comparison tables, exact numbers, filters, export, information scent |
| Elderly / low vision / motor limits | 18px+ body, 48px targets, high contrast, no time limits, no gestures-only |
| One-handed mobile | Primary actions in the thumb zone (bottom third), bottom sheets, no top-corner critical actions |
| Poor connectivity | Optimistic UI, offline states, small payloads, retries, saved drafts |

## Stub persona red flags (rewrite if any are true)

- Demographics only (age, city, hobby) and no stakes, fears or context.
- "Users" or "people" plural instead of one person.
- Could describe the user of any app in the category.
- No trait is cited later in a design decision.
- Every trait is positive. Real people have constraints.

## Anti-persona

Name who you are **not** designing for when it prevents a bad trade. Example: "Not clinic admins. They'd want a dense calendar grid that would overwhelm Meera at 11 pm." This guards against feature creep.

The examples in these references illustrate a method. Build each new persona from the brief in front of you; don't reuse the example's names or details.
