# Handoff — Smoothness Cross-Validation

**Active independent working paper.** The main estimator selects a
normalized index S in [0,1] by the **pooled chronological h-step future-block
MSE** for fixed order d, window L and horizon h. All validation futures
are already realized by the operational forecast origin T; today's
future is not used until outer evaluation. After choosing S, refit on
the latest observed L-window. No branch tracking is required.

See notes/INDEX.md, notes/mathematical_foundations.md,
notes/validation_semantics.md, and manuscript/main.tex.

For standard D_d, rank(D_d)=L-d, ker(Q)=ker(D_d) has dimension d,
I+lambda Q is SPD for every finite lambda>=0, and the PLS fit is unique.
The exact S=1 limit is the singular projection U0 U0^T, with a
unique constrained least-squares fitted polynomial.
The full pooled F(S) is continuous on compact [0,1] and attains
a global minimum; uniqueness of the selected S is NOT guaranteed.

Historical CP03 evidence is retained as exploratory/frozen (3,000
scenarios, 72,000 decisions). No new solver simulation is asserted.
Novelty relative to prior smoothing and predictive CV is still open.
This manuscript is a working draft, not the final published article.
