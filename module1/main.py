from data_cleaning import load_and_clean
from weighting import review_weight, weighted_rating


def main():
    df = load_and_clean()
    df["weight"] = review_weight(df)

    print(f"Plain average rating:    {df['rating'].mean():.2f}")
    print(f"Weighted average rating: {weighted_rating(df, df['weight']):.2f}")


if __name__ == "__main__":
    main()
