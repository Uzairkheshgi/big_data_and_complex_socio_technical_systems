from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "STS Module 1 Team Task Data.csv"

COLUMNS = {
    "Date of Review": "date",
    "User": "user",
    "Usefulness Vote": "useful_votes",
    "Total Votes": "total_votes",
    "User's Rating out of 10": "rating",
    "Review Title": "title",
    "Review": "review",
}


def load_and_clean(path: Path = DATA_PATH) -> pd.DataFrame:
    """load the CSV, fix types and drop rows without a numeric rating."""
    df = pd.read_csv(path).rename(columns=COLUMNS)
    raw_rows = len(df)

    #Convert date and rating columns to appropriate types, coerce errors to NaT/NaN
    df["date"] = pd.to_datetime(df["date"], format="%d %B %Y", errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    df = df.dropna(subset=["rating"])
    df["rating"] = df["rating"].astype(int)

    df["title"] = df["title"].str.strip()
    df["review"] = df["review"].str.strip()
    df["review_length"] = df["review"].str.split().str.len()

    print(f"Loaded {raw_rows} rows, kept {len(df)} with a valid rating, "
          f"({raw_rows - len(df)} dropped).")
    return df.reset_index(drop=True)
