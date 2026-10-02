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
    """Step 1: load the CSV, fix types and drop rows without a numeric rating."""
    df = pd.read_csv(path).rename(columns=COLUMNS)
    raw_rows = len(df)

    df["date"] = pd.to_datetime(df["date"], format="%d %B %Y", errors="coerce")
    df["useful_votes"] = pd.to_numeric(df["useful_votes"], errors="coerce")
    df["total_votes"] = pd.to_numeric(df["total_votes"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    df = df.dropna(subset=["rating", "useful_votes", "total_votes"])
    df = df.astype({"rating": int, "useful_votes": int, "total_votes": int})

    df["title"] = df["title"].fillna("").str.strip()
    df["review"] = df["review"].fillna("").str.strip()
    df["review_length"] = df["review"].str.split().str.len()

    print(f"Loaded {raw_rows} rows, kept {len(df)} with a valid rating, "
          f"({raw_rows - len(df)} dropped).")
    return df.reset_index(drop=True)
