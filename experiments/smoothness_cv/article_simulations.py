"""Two reproducible trend designs from the supplied simulation excerpt.

For t=1,...,N, the linear design is tau_t=4t/N.
The nonlinear design is .6*BetaPDF(t/N;30,17)+.4*BetaPDF(t/N;3,11).
Quarterly additive seasonality is optional and is NOT part of latent tau_t.
The article uses N in {50,200} and Gaussian noise SD in {.5,2}; the API
also accepts other valid lengths and noise settings for reproducibility.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import beta

from experiments.smoothness_cv.live_lab import make_synthetic


ARTICLE_TRENDS = {
    "Lineal del artículo: 4t/N": "linear",
    "No lineal del artículo: mezcla de betas": "beta_mixture",
}


def article_trend(kind: str, n: int) -> np.ndarray:
    """Return tau_1,...,tau_N using article time t/N, including t=N."""
    if type(n) is not int or not 30 <= n <= 3000:
        raise ValueError("N debe ser un entero entre 30 y 3000.")
    u = np.arange(1, n+1, dtype=float)/n
    if kind == "linear":
        return 4.0*u
    if kind == "beta_mixture":
        return 0.6*beta.pdf(u, 30, 17) + 0.4*beta.pdf(u, 3, 11)
    raise ValueError("Tendencia desconocida: utilice linear o beta_mixture.")


def quarterly_seasonality(n: int) -> np.ndarray:
    """xi_t = D_1,t - .5 D_2,t - 2.5 D_3,t + 2 D_4,t, t=1,...,N."""
    return np.array([1.0, -0.5, -2.5, 2.0], dtype=float)[
        np.arange(n) % 4
    ]


def make_article_synthetic(
    kind: str,
    n: int = 200,
    noise_sd: float = 0.5,
    *,
    seasonality: bool = False,
    seed: int = 42,
) -> pd.DataFrame:
    """Return observed=tau+xi+epsilon, latent=tau with Gaussian iid noise.

    Reuse the existing standard-normal generator with the zero trend to
    preserve exact noise seeding conventions across the two Streamlit labs.
    Turning seasonality on/off does not change tau or epsilon.
    """
    trend = article_trend(kind, n)
    if not np.isfinite(noise_sd) or noise_sd < 0:
        raise ValueError("La desviación estándar del ruido debe ser no negativa.")
    noise = make_synthetic(
        "0", n=n, noise_sd=float(noise_sd),
        noise="Gaussian", phi=0.0, seed=int(seed),
    )["observed"].to_numpy(dtype=float)
    seasonal = quarterly_seasonality(n) if seasonality else np.zeros(n)
    return pd.DataFrame({
        "t": np.arange(1, n+1),
        "observed": trend+seasonal+noise,
        "latent": trend,
        "seasonal": seasonal,
    })
