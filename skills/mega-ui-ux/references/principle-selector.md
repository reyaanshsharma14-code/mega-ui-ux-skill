# Principle selector: which laws for which moment

Pick **5–8 principles** per task: 2–3 from the persona's traits, 2–3 from the screen's moment, 1–2 for craft. Each pick needs a "because" and the decision it drives. If a principle doesn't change a decision, drop it.

## By persona trait (from persona.md)

| Persona trait | Reach for |
|---|---|
| Low trust / high stakes (money, health, legal) | Nielsen #1 (status), friction as a feature, authority + social proof, peak-end, Postel, honesty-as-design (Wise), Tesler |
| First-time / novice | Jakob, progressive disclosure, recognition over recall, Hick, mental model, paradox of the active user, defaults |
| Expert / daily / pro | Flexibility & efficiency (Nielsen #7), density, Pareto, Doherty, keyboard and shortcuts, locus of control |
| Tired / rushed / distracted | Hick, Fitts, cognitive load, goal-gradient, Zeigarnik (resume), satisficing, one task per screen |
| Emotional / aspirational | Aesthetic-usability, peak-end, emotional design (visceral), social proof + liking, photo-first |
| Analytical / comparing | Information scent, chunking, anchoring (honest), decoy clarity, F-pattern, data display rules |
| Low literacy / second language | Recognition over recall, mental model, icons + labels, Miller (chunk numbers), Prägnanz |
| Motor / vision limits, elderly | Fitts, WCAG 2.2, Prägnanz, no time limits, solve for one, extend to many |
| One-handed mobile | Thumb zone, Fitts, bottom sheets, serial position (tab bar ends) |
| Habit product (learning, fitness, saving) | Fogg B=MAP, Hooked (ethical), Zeigarnik, goal-gradient, peak-end, endowment |

## By screen moment

| Moment | Reach for | Key decision |
|---|---|---|
| **First impression / landing** | 5-second value prop, aesthetic-usability, Z-pattern, Von Restorff (one CTA), social proof | Answer "what, for me?, next" above the fold |
| **Onboarding** | Paradox of active user, goal-gradient, Zeigarnik, progressive disclosure, IKEA effect, reciprocity | Value before sign-up; learn by doing; ≤3 steps before first value |
| **Sign-up / login** | Postel, recognition, error prevention, accessible authentication | Passkeys, social login, magic link; show password; no CAPTCHA puzzles |
| **Choosing (plans, products, options)** | Hick, choice overload, decoy (honest), anchoring (honest), default effect, Von Restorff | 3 options, one recommended, with a "why" |
| **Search / browse** | Information scent, recognition, Doherty, F/spotted pattern | Suggestions, recent searches, filters as chips, "no results" recovery |
| **Forms / data entry** | Postel, Miller (chunking), Fitts, Nielsen #5 and #9, Tesler, defaults | Fewer fields, inline validation on blur, right keyboards, autofill |
| **Checkout / payment / send** | Friction as a feature, Nielsen #1, Tesler, loss aversion (honest), trust marks, peak-end | Total up front, summary before commit, button states the outcome |
| **Waiting / processing** | Doherty, response time limits, labor illusion, Zeigarnik | Optimistic UI, skeleton, progress with steps |
| **Success / end** | Peak-end, emotional design (reflective), reciprocity | Specific confirmation, what happens next, a shareable proof |
| **Errors** | Nielsen #9, locus of control, Norman slips/mistakes | Inline, plain, fixable, input preserved, no blame |
| **Empty states** | Zeigarnik, recognition, goal-gradient | Value + one action + example |
| **Dashboard / home** | Pareto, serial position, focal point, data display, layer-cake | One headline answer, then drill-down |
| **Settings** | Progressive disclosure, Jakob, defaults | Grouped, searchable, plain-language toggles that apply instantly |
| **Notifications / re-engagement** | Fogg (prompt at high motivation), Zeigarnik, reciprocity | Specific, timely, valuable; easy to tune; never guilt |
| **Destructive actions** | Friction as a feature, Norman constraints, Shneiderman (reversal) | Undo over confirm when reversible; typed confirm when not |
| **Pricing / upgrade** | Anchoring, decoy, default, social proof, loss aversion (honest), reciprocity | Annual default with a real saving; feature diff in the persona's language |

## Craft picks (always 1–2)

Proximity (structure through space), focal point + Von Restorff (one hero), type-scale hierarchy, colour-with-a-job, motion-as-explanation, the states inventory, microcopy as verb + object.

## Resolving conflicts between principles

- **Persona beats the law.** Laws describe averages; the persona is the specific case. (Experts accept more choice than Hick's law suggests.)
- **Clarity beats delight** in high-stakes moments; **delight beats efficiency** at peak and end moments.
- **Convention (Jakob) beats novelty**, except at the signature moment.
- **Accessibility beats aesthetics**, always.
- **Ethics beats conversion**, always.
