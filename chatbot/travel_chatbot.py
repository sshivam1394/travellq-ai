import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- LOAD DATA ----------------

df = pd.read_csv("data/processed/cleaned_reviews.csv")

reviews = (
    df["clean_positive_review"]
    .dropna()
    .astype(str)
    .tolist()
)

# Use only first 2000 reviews for speed
reviews = reviews[:2000]

# ---------------- TF-IDF MODEL ----------------

vectorizer = TfidfVectorizer()

review_vectors = vectorizer.fit_transform(reviews)

# ---------------- RESPONSE FUNCTION ----------------

def generate_response(user_query):

    query_vector = vectorizer.transform([user_query])

    similarities = cosine_similarity(
        query_vector,
        review_vectors
    )

    best_match_index = similarities.argmax()

    best_review = reviews[best_match_index]

    return f"""
### AI Insight

Most relevant customer feedback:

> {best_review}

### Business Interpretation

This review is closely related to your query and reflects customer sentiment patterns from the dataset.
"""

# ---------------- STREAMLIT UI ----------------

st.set_page_config(
    page_title="TravelIQ AI Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 TravelIQ AI Copilot")
st.subheader("AI-Powered Travel Intelligence Assistant")

st.markdown("---")

# User Input
user_input = st.text_input(
    "Ask a business question:"
)

if user_input:

    response = generate_response(user_input)

    st.markdown(response)