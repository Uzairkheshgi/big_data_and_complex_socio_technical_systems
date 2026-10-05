import pandas as pd

from weighting import review_weight, weighted_rating


def add_fake_reviews(df: pd.DataFrame, n: int, rating: int) -> pd.DataFrame:
    """Append n bot reviews: the given rating and no helpfulness votes."""
    fakes = pd.DataFrame({"rating": rating, "useful_votes": 0, "total_votes": 0}, index=range(n))
    return pd.concat([df[["rating", "useful_votes", "total_votes"]], fakes], ignore_index=True)


def compare_ratings(df: pd.DataFrame) -> dict:
    """Plain average vs weighted rating for the same set of reviews."""
    return {"plain": df["rating"].mean(), "weighted": weighted_rating(df, review_weight(df))}


def simulate_attack(df: pd.DataFrame, sizes, rating: int) -> pd.DataFrame:
    """Plain and weighted rating side by side after adding each number of fake reviews in `sizes`.

    `improvement_%` is how much less the weighted rating moved than the plain average.
    """
    rows = {n: compare_ratings(add_fake_reviews(df, n, rating)) for n in sizes}
    result = pd.DataFrame(rows).T.rename_axis("fake_reviews")

    base = compare_ratings(df)
    result["plain_change"] = result["plain"] - base["plain"]
    result["weighted_change"] = result["weighted"] - base["weighted"]
    result["improvement_%"] = (1 - result["weighted_change"] / result["plain_change"]) * 100
    return result
