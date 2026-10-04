import numpy as np
import pandas as pd

PRIOR_VOTES = 2  # pseudo-votes added to each side of the helpful/not-helpful split
MIN_WEIGHT = 0.1


def helpfulness(df: pd.DataFrame) -> pd.Series:
    """Smoothed share of readers who found the review helpful (0.5 when there are no votes)."""
    return (df["useful_votes"] + PRIOR_VOTES) / (df["total_votes"] + 2 * PRIOR_VOTES)


def review_weight(df: pd.DataFrame) -> pd.Series:
    """weight = helpfulness² × √log(1 + total votes), at least MIN_WEIGHT."""
    w = helpfulness(df) ** 2 * np.sqrt(np.log1p(df["total_votes"]))
    return w.clip(lower=MIN_WEIGHT)


def weighted_rating(df: pd.DataFrame, weights: pd.Series) -> float:
    """Σ(w × rating) / Σ(w)."""
    return (weights * df["rating"]).sum() / weights.sum()
