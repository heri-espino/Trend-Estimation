# Paper 3 — Figure-by-figure presentation storyboard

**Design:** one scientific question per visual. A 16:9 landscape layout, consistent fonts and the same accessible color vocabulary across all panels. Each graph is reproducible with the one-command builder.

**Interpretation key:** *Illustration* = explanatory example rather than performance evidence. *Frozen result* = visualization of archived result files. *Small exact case* = previously documented rational Sturm example with floating-point plots.

| ID / generated PDF basename | The question this slide answers | Type | Suggested manuscript use |
| --- | --- | --- | --- |
| 01_rolling_cv_definition | What data does the historical h-step validation objective use? | Illustration | Intro or supplement |
| 02_smoothing_family | What does changing smoothness do to the trend estimate? | Illustration | Intro |
| 03_lambda_to_s | Why map an unbounded penalty to S in [0,1]? | Exact-spectrum illustration | Core theory |
| 04_effective_degrees_of_freedom | How does complexity change with S and d? | Mathematical identity | Supplement |
| 05_exact_endpoints | What do S=0 and the S=1 polynomial limit mean? | Illustration | Theory |
| 06_loss_pooling | What happens when multiple completed forecast losses are averaged? | Small constructed example | Talk/supplement |
| 07_objective_derivative_curvature | Why do we need analytic gradient and curvature? | Small exact case | Method |
| 08_adaptive_search_steps | Which sampling/refinement operations occur before selecting an optimum? | Actual final toy-search sample set, staged diagram | Method |
| 09_endpoint_refinement_ablation | What empirical failure appears without boundary refinement? | Frozen sensitivity results | Method/results |
| 10_sturm_worked_example | How does an exact root count coexist with approximate plotted roots? | Small exact case | Method/results |
| 11_lambda_vs_s_landscape | How does the very same objective appear in different coordinates? | Small exact case | Talk |
| 12_adversarial_gallery | Which types of minima, inflections and endpoints challenge an optimizer? | Analytic test definitions | Methods supplement |
| 13_adaptive_sampling_density | Where does the toy adaptive search actually evaluate the objective? | Actual toy-search outputs | Talk/method |
| 14_selected_s_agreement | Do numerical and dense-reference selected S values agree? | Frozen synthetic + financial | Main results |
| 15_evaluation_efficiency | How many evaluations are needed compared with fixed dense scans? | Frozen three-family benchmarks | Main results |
| 16_selection_error_distributions | How is numerical error distributed over surfaces? | Frozen synthetic + financial | Results supplement |
| 17_cost_by_order_horizon_window | How does search cost vary by d, h and L? | Frozen synthetic | Supplement |
| 18_sensitivity_tradeoff | What is the cost/robustness tradeoff of the frozen settings? | Frozen sensitivity | Main results |
| 19_exact_endpoint_frequencies | How often are exact boundary models selected? | Frozen synthetic + financial | Main/supplement |
| 20_adversarial_method_comparison | What does the known-truth adversarial benchmark actually recover? | Frozen adversarial | Main/supplement |
| 21_epsilon_candidate_spacing | What does candidate-spacing change *after* minima are discovered? | Frozen synthetic candidate sweep | Talk/supplement |
| 22_gdp_unimodal_contrast | Is multimodality present on every data series? | Frozen applied GDP | Applied results |
| 23_spy_rank_reversal | How can validation and untouched-test candidate ranking disagree? | Frozen applied SPY | Main applied figure |
| 24_aapl_separated_minima | Can minima be far apart without giving competitive test outcomes? | Frozen applied AAPL | Supplement |
| 25_btc_three_minima | What does a three-candidate forecast geometry look like? | Frozen applied BTC | Main/supplement |
| 26_validation_test_rank_comparison | How different are validation and external-test candidate losses? | Frozen SPY and BTC | Applied results |
| 27_multimodality_by_asset | How often do *these pre-specified configurations* have multiple spaced candidates? | Frozen development scans | Applied results |
| 28_actual_temporal_splits | How were historical folds and the external test separated in actual dates? | Frozen SPY split protocol | Method or appendix |

## Concise proposed talk (approximately 20–25 minutes)

Open with 01, 02, 03, 05. Show the hard objective and discovery method using 07, 08, 09, 10. Establish empirical credibility with 12, 14, 15, 18, 19. Close with 22, 23, 25, 26 and 28. Keep the remaining figures for questions or appendix.

## For a journal article

Do **not** include all 28 automatically; many slides intentionally overlap with existing manuscript figures. Prefer selecting 6–10 distinct, explanatory figures, moving large galleries and diagnostics to an appendix or supplementary material. The final article figure numbering and captions must be decided independently of this slide catalog.

The benchmark figures retain the historical comparison semantics and should not be presented as proof of stationary-root completeness. The small Sturm figure must distinguish exact rational root counts from approximate reported coordinates. The SPY rank reversal must retain its frozen validation ranks, even though test rankings differ.
