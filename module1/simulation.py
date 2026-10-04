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
    """Both ratings after adding each number of fake reviews in `sizes`."""
    rows = {n: compare_ratings(add_fake_reviews(df, n, rating)) for n in sizes}
    return pd.DataFrame(rows).T.rename_axis("fake_reviews")
