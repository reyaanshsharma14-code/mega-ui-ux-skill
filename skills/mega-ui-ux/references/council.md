# The review council

A design is done only when every council member passes it. The builder never grades its own work: each reviewer is a separate agent with one lens, a fixed checklist, and no access to the builder's reasoning, so it judges what is on the screen, not what was intended.

## When it runs

| Run size | Council |
|---|---|
| Full run, redesign | All six members, after step 9's self-critique |
| Light run (one screen, one fix) | One reviewer holding the Persona, Craft and Layout checklists together |
| Critique only | No council; the critique is the output |

## Members

Each member gets the same packet (below) and its own checklist. Each item is answered PASS or FAIL. A FAIL names the screen, the element, and a concrete fix. "Consider…" is not a finding.

1. **Persona stand-in.** It reads every screen as the persona would, in the persona's language and literacy, and does the main job without help.
   - Can the persona finish the main job on the first try? Write the taps.
   - Is every word one the persona uses? List each jargon word.
   - Is the answer to the persona's real question visible without scrolling or opening anything?
   - Is anything frightening, shaming or confusing to this persona?
2. **Craft critic.** It judges the rendered screenshots.
   - Is there one focal point per screen, and does the screen read correctly in black and white?
   - Is there at most 2 short lines of text per block, with reasons shown as chips, meters, dots, charts or icons?
   - Do the type scale, spacing scale and radii follow the tokens, with no arbitrary values?
   - Is the design free of the generic tells in `taste-signature.md` (category-cliché colour, cards around everything, stock imagery)?
   - Is the signature moment visibly crafted, and everything else quiet?
3. **Layout and accessibility auditor.** It works from the HTML and the screenshots, and computes values instead of estimating them.
   - Does every text and background pair meet 4.5:1 (3:1 for large text and UI)? List the computed ratios.
   - Are all targets at least 44–48px?
   - At 360px wide and in the longest language, does every row wrap cleanly, with no button touching a container edge (including overlays and centred cards)?
   - Is colour never the only signal, does reduced motion work, and does dark mode work if it is in scope?
4. **States and completeness auditor.**
   - Does every key screen have loading, empty, error and offline states, plus any state a persona trait makes likely?
   - Are empty, offline and error states useful (saved content, an illustration, something to do, what is safe), never a lone line?
   - Do destinations that show progress have first visit, in progress, just finished, done for today and return visit?
   - Does every paid or limited feature have free, premium, quota used, buy more, payment failed and bought?
   - Is every pushed flow of each destination present, with its states?
   - Does each feature stay independent, with no invented coupling?
5. **Ethics and honesty reviewer.**
   - Are there no dark patterns: confirm-shaming, fake urgency, hidden costs, pre-ticked upsells or roach motels?
   - Are prices and limits stated before commitment, with "later" given equal weight?
   - Is there no fear framing (bad, danger, doom) where a calm word would do?
   - Is user data, privacy and consent handled visibly at the moment it matters?
   - Does every promise on screen (refunds, "always free", delivery times, cancel terms) come from the brief? An invented promise is a FAIL; mark it as an assumption for the person to confirm.
6. **Brief keeper.**
   - Was everything the person asked for delivered, at the scope they asked for?
   - Is every shipped feature in the inventory kept, moved or dropped with a reason?
   - Are peers equal, with an order rule? Has each new or renamed destination passed its name check?
   - Is every assumption written down, and does no decision contradict something the person said?

## The packet each member gets

- The brief, in the person's words.
- The persona card, feel statement and principles (steps 2–4).
- Screenshots of every screen and state, at 360px wide. The packet holds the file paths; the member opens them. Headless Chrome will not shrink its window below about 500px, so render the screen inside a 360px-wide container (or use device emulation) rather than trusting `--window-size=360`. Also the HTML path, or the text spec if nothing can be rendered.
- Its own checklist from above.

Leave out the builder's rationale and its self-critique. A member handed the builder's conclusion tends to agree with it.

## The loop

1. Start all members at once. Each returns `PASS` or `FAIL` plus a list of findings: `screen · element · problem · fix`.
2. If every member passes, the council is done.
3. Otherwise the builder fixes every finding, re-renders, and sends the updated packet to the members that failed, plus any member whose area the fixes touched.
4. Before hand-over, run one final round with all members on the final version, so a fix in one area has not broken another.
5. Stop after 3 fix rounds. If anything still fails, hand over with an **Unresolved** list (member, finding, why it is not fixed). Never call the design passed when it is not.

**Conflicts between members** are settled by the order in SKILL.md: accessibility, then ethics, then persona, then convention, then taste. Record each ruling in the hand-over.

**If you cannot start agents** (you are already a subagent, or there is no agent tool), run the members yourself one after another. Use a fresh pass for each, with only its checklist and the screenshots, and write each verdict down before starting the next. Label it in the hand-over as `Council (self-run, sequential)`, so the caller knows it is weaker than separate agents and can re-run it with real ones.

## Prompt template for one member

```
You are the <member> on a design review council. Judge only what you see in the files; you have not seen the designer's reasoning.
Brief: <the person's words>
Persona, feel and principles: <steps 2–4>
Screens: <paths to screenshots>; HTML: <path>
Checklist: <this member's items>
Open every screenshot. For each checklist item answer PASS or FAIL. For each FAIL give: screen · element · problem · concrete fix.
End with one line: VERDICT: PASS or VERDICT: FAIL.
```

## Hand-over line

Add this to the output contract: `Council: <member → PASS/FAIL per round>; rounds: N; unresolved: <none, or the list>`.
