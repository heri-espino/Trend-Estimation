# Research objective — method-dependent weighted-F branch tracking

**Active prospective redesign | 2026-10-08.** The current hypothesis is that
temporal **trajectories of local minima of weighted forecast-loss surfaces**
can support a better smoothing decision at a declared horizon \(h\).
This paper is distinct from pooled forecast-CV: it preserves the history
and identity of competing minima rather than selecting one global
minimum of the latest aggregate.

At the current outer origin \(T\), freeze \((m,d,L,h)\) and the
method's recency lookback/weights. \(m\) **weights historical loss curves**,
not previous S values. For completed origins \(t_q+h\le T\),

\[
\ell_{t_q}(S)=h^{-1}\|y_{t_q+1:t_q+h}
-G_{d,h}H_{d,L}(S)y_{t_q-L+1:t_q}\|^2,
\quad
F_r^{(m,d,L,h)}(S)=
\frac{\sum_{q\in I_m(r)}w^{(m)}_{r,q}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w^{(m)}_{r,q}}.
\]

For **each** predeclared method \(m\) and order \(d\), identify and
track local minima of \(F_r\), including eligible endpoints. Associate
minima between adjacent completed historical surfaces with one-to-one
distance-limited correspondence. New/unmatched minima create new
branches, lost minima retire. Multiple branches are *possible*, not
assumed, for any \((m,d,L,h)\).

Store \(V_j=[(r,t_r,S^*_{j,r},F_r(S^*_{j,r}))]\).
Choose an active branch \(\widehat j_T=\psi(V)\) from **completed
historical** evidence using a fixed support and loss-ranking policy.
Then map the selected branch to one operational S via a separately
specified \(\phi\), initially **mean of its last three minima**.
Refit on the newest length-\(L\) window, issue a fresh \(h\)-step
forecast, and evaluate against an untouched outer block. Neither
branch construction nor selection requires a second inner Val2.

This is the **new** protocol, not the Val1/Val2 transformed-loss method
used in historical CP04–CP08. Those frozen results must not be
relabelled as tests of the proposed redesign. The objective remains
empirical: when, if ever, does retaining the temporal identities
of local minima improve genuinely out-of-sample prediction relative
to simply minimizing the latest weighted surface?

Full common definition: [Weighted-surface protocol](../../WEIGHTED_SURFACE_PROTOCOL.md).
Implementation: [Dynamic decision notes](dynamic_tracked_smoothness.md).
