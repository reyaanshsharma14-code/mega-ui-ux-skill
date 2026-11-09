# UX laws (Laws of UX canon + classic HCI)

Format: **Law**: what it says. **Apply when**: persona or context signal. **Drives**: the concrete decision. **Misuse**: how it goes wrong.

## Decision and choice

| Law | What it says | Apply when | Drives | Misuse |
|---|---|---|---|---|
| **Hick's law** | Decision time grows with the number and complexity of choices | Choosing under time pressure, first-time users, tired users | Fewer options per step, a recommended default, grouping, progressive disclosure | Hiding options experts need; splitting one decision into many screens |
| **Choice overload** | Too many options lowers satisfaction and conversion | Plans, products, settings | 3 tiers with one highlighted; filters before a list; curation | Removing real choice to push one option |
| **Miller's law** | Working memory holds about 7±2 chunks (more like 4 in practice) | Codes, numbers, multi-step forms | Chunk numbers (4521 8890), keep the info visible rather than remembered, group into ≤5 | Using "7 items max" as a hard menu rule. Miller is about memory, not lists people can see |
| **Tesler's law** (conservation of complexity) | Every system has complexity that can't be removed, only moved | Anything with real complexity (taxes, FX, insurance) | Move complexity from the user to the system: auto-detect, defaults, inference | Oversimplifying so the user is surprised later |
| **Occam's razor** | Prefer the simplest solution that works | Any screen with competing elements | Remove elements until something breaks | Removing signifiers or info people need |
| **Pareto principle** | 80% of use comes from 20% of features | Prioritising features and navigation | Promote the top 20%, tuck the rest away | Ignoring the long tail that matters to key users |
| **Parkinson's law** | A task expands to fill the time available | Forms, checkout | Autofill, saved details, a single-tap repeat | Fake countdowns |

## Motor and targeting

| Law | What it says | Apply when | Drives | Misuse |
|---|---|---|---|---|
| **Fitts's law** | Time to hit a target depends on its distance and size | Primary actions, mobile, motor limits, gloves, motion | Large primary targets (44pt iOS / 48dp Android minimum), placed near the thumb or cursor; edges and corners are infinite on desktop | Giant buttons for everything (no hierarchy); destructive actions placed in easy reach |
| **Steering law** | Moving through a narrow path is slow | Nested hover menus, sliders | Wide menus, forgiving hover zones, mega-menus with delay | — |
| **Thumb zone** (Hoober) | One-handed reach favours the bottom middle of the screen | Mobile one-handed use | Bottom nav, bottom sheets, primary CTA at the bottom | Putting rare actions in prime space |

## Time and responsiveness

| Law | What it says | Apply when | Drives | Misuse |
|---|---|---|---|---|
| **Doherty threshold** | Productivity soars when the system responds in under 400ms | Every interaction | Optimistic UI, skeletons, instant feedback, prefetch | Fake loaders that slow down a fast action |
| **Response time limits** (Nielsen) | 0.1s feels instant, 1s keeps flow, 10s loses attention | Loading, processing | Under 1s: no loader; 1–10s: a spinner or skeleton; over 10s: progress with an estimate and let the user leave | — |
| **Goal-gradient effect** | Motivation rises near the goal | Multi-step flows, onboarding, loyalty | Progress indicators, start partly complete ("2 of 5 done"), short last steps | Endless progress bars, fake progress |
| **Zeigarnik effect** | Unfinished tasks stick in memory | Onboarding, profile completion, drafts | Visible incomplete states, "resume where you left off" | Nagging badges that create anxiety |

## Memory, attention and perception

| Law | What it says | Apply when | Drives | Misuse |
|---|---|---|---|---|
| **Jakob's law** | Users spend most of their time on other sites and expect yours to work the same way | Any common pattern (cart, login, nav, search) | Use platform and category conventions; innovate only where you win | Being "different" on table-stakes patterns |
| **Serial position effect** | First and last items are remembered best | Nav, lists, onboarding | Most important items at the start and end; key nav at the ends of the tab bar | Burying the key item in the middle |
| **Von Restorff** (isolation) | The item that differs is remembered | Primary CTA, recommended plan, key number | Exactly one emphasised element per view | Emphasising everything, so nothing stands out |
| **Peak-end rule** | Experiences are judged by their peak and their end | Flows with emotion: payment, booking, onboarding, errors | Design a delightful peak and a strong end (confirmation, receipt, celebration); soften the worst moment | Celebrating trivial actions; dull end screens |
| **Aesthetic-usability effect** | Beautiful designs are perceived as easier to use and are forgiven more | Trust, first impression, consumer products | Invest in polish where first impressions form | Beauty hiding usability problems in testing |
| **Selective attention / banner blindness** | Users ignore what looks like ads or noise | Promos, alerts | Don't style key info like banners; integrate it into content | Dressing up ads as content (a dark pattern) |
| **Change blindness** | Users miss changes they aren't looking at | Validation, live updates, totals | Animate changes, place feedback at the point of focus | — |
| **Law of Prägnanz** | People see the simplest form | Icons, layout | Simple shapes and silhouettes, clear structure | — |

## Robustness and flexibility

| Law | What it says | Apply when | Drives | Misuse |
|---|---|---|---|---|
| **Postel's law** | Be liberal in what you accept, conservative in what you send | Inputs: phone, date, card, name | Accept spaces and dashes, any format; normalise silently; clear output | Accepting invalid data silently |
| **Flexibility–usability tradeoff** | More flexible means more complex | Pro tools vs consumer apps | Choose flexibility only for power personas; otherwise opinionated defaults | — |
| **Mental model** | Users predict behaviour from what they know | New paradigms | Map to a familiar thing; reuse its vocabulary | Metaphors that break halfway |
| **Paradox of the active user** | Users never read manuals; they start using immediately | Onboarding | Learn-by-doing, contextual hints, no tutorials up front | — |
| **Cognitive load** | Mental resources are limited (intrinsic + extraneous + germane) | Every screen | Cut extraneous load: noise, decoration, unclear labels | — |
