# Research objective — dynamic branch selection

**Status:** active, independent exploratory working paper.

At each historical forecast origin t, consider the future-block MSE
surface F_t(S) with S in [0,1], and detect local minimizing candidates.
Match candidates between chronologically adjacent origins only when
their validation blocks are **fully completed** by the operational
forecast origin. A one-to-one correspondence may be chosen using
a proximity radius epsilon or a more sophisticated matching rule;
branch identities are data- and algorithm-dependent.

Store each branch as
\[
V_j=[(S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t})]_t.
\]
Choose a branch j with \(\psi(V_1,\ldots,V_J)\), obtain today's
smoothness \(\widehat S_T=\phi(V_j)\), refit the trend using the newest
available window, and forecast the untouched future.

Core empirical questions:
1. Is the branch correspondence stable to stride, losses, crossings
   and disappearing minima?
2. Which, if any, branch decision maps beat pooled historical
   forecast-CV on out-of-sample data?
3. How should validation stride, order, window and horizon be frozen or
   selected without looking at future test outcomes?

Do not mistake per-fold grid minima for certified interior minima;
do not treat the existence of V as evidence that its decisions improve forecasts.
