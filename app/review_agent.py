import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_reviews.csv"
)

def analyze_reviews():

    positive = len(
        df[df["review_sentiment"] == "POSITIVE"]
    )

    negative = len(
        df[df["review_sentiment"] == "NEGATIVE"]
    )

    return {
        "positive_reviews": positive,
        "negative_reviews": negative,
        "total_reviews": len(df)
    }