Feature Importance Analysis: California Housing Model
This analysis summarizes the results of the ablation study, highlighting which engineered feature groups provide the most predictive power and which are redundant.

# Top Tier: High Impact Features
These groups provided the most significant improvements to the model's RMSE.

## 1. Distance Features (+0.0135 RMSE)

Components: Distance to coast, distance to city centers.

Insight: Captures the "economic geography" of California.

Conclusion: Housing prices are heavily driven by spatial proximity to hubs and amenities.

## 2. Ratios (+0.0113 RMSE)

Components: Income-per-room, people-per-room, rooms-per-household.

Insight: Normalizes scale and accounts for crowding/density effects.

Conclusion: Engineered ratios provide a much cleaner signal than raw counts alone.

## 3. Nonlinear Transforms (+0.0094 RMSE)

Components: Log, square root, and inverse transformations.

Insight: Reduces feature skew and stabilizes variance.

Conclusion: These transformations are essential for linear models to handle non-linear relationships.

# Mid-Tier: Moderate Impact
These features augment the model but are secondary to the top-tier groups.

## 1. Raw Features (+0.0080 RMSE)

Insight: Despite 50+ new features, the original data still contains unique signals.

Conclusion: Feature engineering should be additive; original features should rarely be discarded entirely.

## 2. Interactions (+0.0051 RMSE)

Insight: Captures how features behave in combination (e.g., Age × Income).

Conclusion: Useful, but easier to over-engineer; they offer diminishing returns compared to ratios.

# Low Tier: Specialized Impact
These provide niche improvements or structural benefits.

## 1. Geographic Grouping (+0.0034 to +0.0025 RMSE)

Groups: geo_clusters (K-Means) and geo_bins (Quantile Binning).

Insight: Continuous spatial features (distances) vastly outperform discrete buckets (bins).

Conclusion: Discrete bins are better for interpretability, but worse for raw accuracy.

## 2. Quantiles & Binary Flags (+0.0011 to +0.0008 RMSE)

Insight: Minimal predictive gain.

Conclusion: Best used for regularization or making the model easier for humans to explain.

# Redundant: Zero Impact
These features showed ~0.0000 change in RMSE when removed.

## Differences & Aggregates

Observation: These features provided no unique signal.

Conclusion: Their predictive value was already fully captured by the Ratios or Distance groups. They can be removed to simplify the model.