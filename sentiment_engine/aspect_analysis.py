import pandas as pd
from transformers import pipeline

# Load processed dataset
df = pd.read_csv("data/processed/cleaned_reviews.csv")

# Initialize sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Travel-related aspects
aspects = [
    "location",
    "service",
    "staff",
    "cleanliness",
    "food",
    "price",
    "comfort",
    "room"
]

# Use first 20 reviews
reviews = df["clean_positive_review"].head(20)

results = []

print("Running aspect-based sentiment analysis...\n")

for review in reviews:

    review = str(review).lower()

    for aspect in aspects:

        # Check if aspect exists in review
        if aspect in review:

            result = sentiment_pipeline(review[:512])[0]

            results.append({
                "aspect": aspect,
                "sentiment": result["label"],
                "confidence": round(result["score"], 4),
                "review_snippet": review[:120]
            })

# Convert to dataframe
results_df = pd.DataFrame(results)

# Display results
print(results_df)