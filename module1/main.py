from data_cleaning import load_and_clean
from simulation import compare_ratings, simulate_attack


def main():
    df = load_and_clean()

    ratings = compare_ratings(df)
    print(f"Plain average rating:    {ratings['plain']:.2f}")
    print(f"Weighted average rating: {ratings['weighted']:.2f}")

    print("\nAfter adding fake 1-star reviews:")
    print(simulate_attack(df, sizes=[0, 100, 500, 1000], rating=1).round(2))


if __name__ == "__main__":
    main()
