# AI_HANDOFF — Numerical-methods checkpoint

**Status:** historical checkpoint summary. The canonical current handoff is \`../AI_HANDOFF.md\`.

## Frozen work preserved from the pre-split paper

- Primary adaptive-\(S\) numerical search is frozen.
- Principal adversarial, synthetic, and real-geometry numerical benchmarks are complete.
- Applied multiple-minimum case studies are complete and remain useful for interpretation.
- The copied SMCCA manuscript is a pre-split draft and must be refactored so that the forecast-optimal-smoothness criterion is attributed to the companion \`paper_smoothness-cv/\` paper while this paper isolates the numerical contribution.

## Current next action

Read, in order:

1. \`../AI_HANDOFF.md\`
2. \`../notes/research_objective.md\`
3. \`../notes/paper_split_2026-10-05.md\`
4. \`../todo/NEXT.md\`
5. \`../notes/results.md\`
6. \`../notes/sturm_minicheck.md\`

Do not reopen tuning of the frozen adaptive search unless a genuine implementation error is found.

The main open strategic decision is whether to finish the current adaptive-discovery + Brent paper as-is or strengthen it by generalizing the rational/Sturm root-isolation direction into a certified stationary-point enumeration method.
