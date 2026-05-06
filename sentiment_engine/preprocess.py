import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("data/raw/Hotel_Reviews.csv").head(5000)# Show column names
print(df.columns)

# Text cleaning function
def clean_text(text):

    # Convert to string and lowercase
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Keep only letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Rejoin properly
    return " ".join(words)
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\\s]", "", text)

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Clean positive reviews
df["clean_positive_review"] = df["Positive_Review"].apply(clean_text)

# Clean negative reviews
df["clean_negative_review"] = df["Negative_Review"].apply(clean_text)

# Save processed dataset
df.to_csv("data/processed/cleaned_reviews.csv", index=False)
print("Preprocessing completed successfully.")