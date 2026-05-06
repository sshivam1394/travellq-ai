import pandas as pd
from transformers import pipeline

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/processed/cleaned_reviews.csv"
)

# =========================
# LOAD MODEL
# =========================

sentiment_pipeline = pipeline(
    "sentiment-analysis"
)

# =========================
# CREATE CLEANED REVIEW COLUMN
# =========================

df["cleaned_review"] = (
    df["clean_positive_review"]
    .fillna("")
    .astype(str)
)

# =========================
# RUN SENTIMENT ANALYSIS
# =========================

sentiments = []
confidences = []

reviews = df["cleaned_review"].head(1000)

for review in reviews:

    if review.strip() == "":

        sentiments.append("NEUTRAL")
        confidences.append(0)

    else:

        result = sentiment_pipeline(
            review[:512]
        )[0]

        sentiments.append(
            result["label"]
        )

        confidences.append(
            round(result["score"], 4)
        )

# =========================
# SAVE RESULTS
# =========================

df = df.head(1000)

df["review_sentiment"] = sentiments
df["confidence"] = confidences

df.to_csv(
    "data/processed/cleaned_reviews.csv",
    index=False
)

print(
    "Sentiment analysis completed successfully."
)