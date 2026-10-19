"""Independent algebraic audit of committed Study M.2 COMPACT tables only.

Checks source manifest counts, method rankings, confidence interval containment,
the paired-loss difference identities, Holm p-value monotonicity, nested R1/R3
first-series identities, and no accidental seed-0 reuse. Does NOT pretend to
recompute estimates or Monte Carlo uncertainty from locally ignored raw shards.
Run after committing CSV/JSON; no simulation of any size is launched.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


DATA = Path("results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1")
GALLERY = Path("results/pooled_loocv_smoothness/process_examples/gallery_001")


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def close(a: float, b: float, *, atol=5e-12) -> bool:
    return math.isclose(a, b, rel_tol=1e-11, abs_tol=atol)


def audit(source: Path = DATA, gallery: Path | None = GALLERY) -> dict:
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    cfg = manifest["design"]
    methods = cfg["methods"]
    cases = cfg["cases"]
    Rs = cfg["pool_sizes"]
    count = cfg["count"]
    if manifest["status"] != "COMPLETE":
        raise ValueError("input campaign incomplete")
    if count < 1 or len(set(methods)) != len(methods) or len(set(cases)) != len(cases):
        raise ValueError("invalid independent-seed or method design")
    if cfg["seed_start_inclusive"] < 1:
        raise ValueError("gallery seed 0 must not be replayed")
    if cfg["seed_stop_exclusive"] - cfg["seed_start_inclusive"] != count:
        raise ValueError("noncontiguous seed window")
    if Rs != [1, 3]:
        raise ValueError("expected nested R1/R3")
    if manifest["actual_method_rows"] != count * len(cases) * len(Rs) * len(methods):
        raise ValueError("unexpected method-row count")
    if manifest["finished_chunks"] != manifest["expected_chunks"]:
        raise ValueError("not all per-seed shards were written at source")
    risk = load_csv(source / "risk_by_process_method.csv")
    pairs = load_csv(source / "paired_method_mse_differences.csv")
    pooling = load_csv(source / "paired_pooling_first_series.csv")
    if len(risk) != len(cases)*len(Rs)*len(methods):
        raise ValueError("risk count wrong")
    if len(pairs) != len(cases)*len(Rs)*len(methods)*(len(methods)-1)//2:
        raise ValueError("pairwise count wrong")
    if len(pooling) != len(cases)*len(methods):
        raise ValueError("pool count wrong")

    key = lambda x: (x["case"], int(x["R"]), x["method"])
    lookup = {}
    for x in risk:
        k = key(x)
        if k in lookup or x["case"] not in cases or int(x["R"]) not in Rs or x["method"] not in methods:
            raise ValueError("duplicate or unexpected risk group")
        if int(x["n_independent_seeds"]) != count:
            raise ValueError("incorrect effective seed count")
        mean = float(x["mean_pool_mse"])
        lo, hi = float(x["mean_pool_mse_ci95_low_pointwise"]), float(x["mean_pool_mse_ci95_high_pointwise"])
        if not (math.isfinite(mean) and lo <= mean <= hi):
            raise ValueError("risk mean outside CI")
        lookup[k] = x
    for c in cases:
        for r in Rs:
            ordered = sorted((lookup[(c,r,m)] for m in methods),
                             key=lambda x: float(x["mean_pool_mse"]))
            if [int(x["mean_pool_mse_rank"]) for x in ordered] != list(range(1,len(methods)+1)):
                raise ValueError(f"incorrect MSE ranks: {c}, R={r}")
    seen_pairs = set()
    p_holm = []
    n_sig = 0
    for x in pairs:
        c, r, a, b = x["case"], int(x["R"]), x["method_A"], x["method_B"]
        key_pair = (c, r, frozenset((a, b)))
        if key_pair in seen_pairs or a == b:
            raise ValueError("duplicate or self comparison")
        seen_pairs.add(key_pair)
        if int(x["n_matched_independent_seeds"]) != count:
            raise ValueError("pair effective seed count")
        expected = (float(lookup[(c,r,a)]["mean_pool_mse"])
                    - float(lookup[(c,r,b)]["mean_pool_mse"]))
        difference = float(x["mean_mse_A_minus_B_negative_favors_A"])
        if not close(expected, difference):
            raise ValueError("paired risk difference inconsistent")
        lo, hi = float(x["ci95_low_pointwise"]), float(x["ci95_high_pointwise"])
        if not lo <= difference <= hi:
            raise ValueError("paired CI does not contain mean")
        raw = float(x["paired_t_p_uncorrected"])
        adjusted = float(x["paired_t_p_holm_all_processes"])
        if not (0 <= raw <= adjusted+1e-13 <= 1+1e-13):
            raise ValueError("invalid Holm or nominal p")
        n_sig += adjusted < .05
        p_holm.append((raw, adjusted))
    previous = 0.
    for raw, adjusted in sorted(p_holm):
        if adjusted < previous - 1e-12:
            raise ValueError("global Holm p not monotone in raw p")
        previous = adjusted
    seen_pooling = set()
    adverse = {}
    for x in pooling:
        c, m = x["case"], x["method"]
        if (c,m) in seen_pooling:
            raise ValueError("duplicate pooling")
        seen_pooling.add((c,m))
        actual = float(x["mean_first_series_mse_R3_minus_R1_negative_favors_pooling"])
        expected = (float(lookup[(c,3,m)]["mean_first_series_mse"])
                    - float(lookup[(c,1,m)]["mean_first_series_mse"]))
        if not close(actual, expected):
            raise ValueError("pooling mean inconsistent")
        lo, hi = float(x["ci95_low_pointwise"]), float(x["ci95_high_pointwise"])
        if not lo <= actual <= hi:
            raise ValueError("pooling CI does not contain mean")
        if lo > 0:
            adverse[c] = adverse.get(c,0)+1

    gallery_agreement = None
    if gallery is not None and (gallery / "illustrative_winners.csv").is_file():
        old = load_csv(gallery / "illustrative_winners.csv")
        if len(old) != len(cases)*len(Rs):
            raise ValueError("unexpected gallery size")
        gallery_agreement = sum(
            min(methods,key=lambda m:float(
                lookup[(row["case"],int(row["R"]),m)]["mean_pool_mse"]
            )) == row["lowest_MSE_in_THIS_ONE_realization_NOT_DEPLOYABLE_SELECTOR"]
            for row in old
        )

    return {
        "status": "COMPACT_INTERNAL_IDENTITIES_PASS_RAW_SHARDS_NOT_RECOMPUTED",
        "source_manifest_commit": manifest["source_commit_at_start"],
        "base_seed": cfg["base_seed"],
        "seed_window_inclusive": [
            cfg["seed_start_inclusive"], cfg["seed_stop_exclusive"] - 1
        ],
        "independent_seed_count": count,
        "cases": len(cases), "pool_sizes": Rs, "methods": len(methods),
        "method_rows": manifest["actual_method_rows"],
        "risk_rows": len(risk), "paired_method_rows": len(pairs),
        "paired_pooling_rows": len(pooling),
        "holm_significant_of_all_method_pairs": n_sig,
        "n_method_pairs_global_holm_family": len(pairs),
        "methods_with_pointwise_CI_showing_pooling_harm_by_case": adverse,
        "gallery_same_mean_risk_winner_of_total_18": gallery_agreement,
        "limits": [
            "Raw gzip replicate shards are excluded from Git; no independent recomputation of MC MSE, SD, CI or Holm inputs was possible from compact tables alone.",
            "Source code and output internal algebra checks are not a validation of the Gaussian data-generating assumptions.",
            "Only simulated latent reconstruction, not h-step forecasting.",
            "Reproduce the full raw audit on the user's machine before archiving shards."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DATA)
    parser.add_argument("--gallery", type=Path, default=GALLERY)
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()
    result = audit(args.source, args.gallery)
    if args.out_dir is not None:
        args.out_dir.mkdir(parents=True,exist_ok=True)
        (args.out_dir / "audit_summary.json").write_text(
            json.dumps(result,indent=2) + "\n",encoding="utf-8"
        )
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
