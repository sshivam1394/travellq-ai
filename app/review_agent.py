import pandas as pd

sample_reviews = [
    "Amazing hotel with friendly staff",
    "Room was clean and comfortable",
    "Excellent location and breakfast",
    "Very bad service and dirty room",
    "Staff was helpful and polite",
    "Fantastic experience overall",
]

df = pd.DataFrame({
    "review": sample_reviews,
    "sentiment": [
        "POSITIVE",
        "POSITIVE",
        "POSITIVE",
        "NEGATIVE",
        "POSITIVE",
        "POSITIVE"
    ]
})

def analyze_reviews():
    positive = len(df[df["sentiment"] == "POSITIVE"])
    negative = len(df[df["sentiment"] == "NEGATIVE"])

    return {
        "total_reviews": len(df),
        "positive_reviews": positive,
        "negative_reviews": negative,
        "dataframe": df
    }