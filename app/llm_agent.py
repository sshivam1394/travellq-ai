import pandas as pd

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/processed/cleaned_reviews.csv"
)

# =========================
# BASIC DATA
# =========================

positive_reviews = df[
    df["review_sentiment"] == "POSITIVE"
]

negative_reviews = df[
    df["review_sentiment"] == "NEGATIVE"
]

# =========================
# AI FUNCTION
# =========================

def ask_ai(question):

    question = question.lower()

    # =====================
    # PRICING
    # =====================

    if (
        "price" in question or
        "pricing" in question or
        "cost" in question
    ):

        return """
### AI Business Insight

Pricing inconsistency appears to be one of the major causes of customer dissatisfaction.

### Recommendation
- Improve pricing transparency
- Align room quality with pricing expectations
- Offer better value-added services
"""

    # =====================
    # ROOM QUALITY
    # =====================

    elif (
        "room" in question or
        "cleanliness" in question
    ):

        return """
### AI Business Insight

Room quality and cleanliness strongly influence customer sentiment.

### Recommendation
- Improve housekeeping consistency
- Upgrade room maintenance standards
- Monitor cleanliness feedback regularly
"""

    # =====================
    # STAFF
    # =====================

    elif (
        "staff" in question or
        "service" in question
    ):

        return """
### AI Business Insight

Positive staff behavior significantly improves customer satisfaction.

### Recommendation
- Continue hospitality training
- Reward high-performing staff
- Improve response speed to complaints
"""

    # =====================
    # GENERAL SUMMARY
    # =====================

    elif (
        "summary" in question or
        "overall" in question
    ):

        return f"""
### Executive Summary

- Total Reviews Analyzed: {len(df)}
- Positive Reviews: {len(positive_reviews)}
- Negative Reviews: {len(negative_reviews)}

### Key Findings
- Customers value comfort and location
- Pricing and room quality are major complaint areas
- Staff service positively impacts customer experience
"""

    # =====================
    # DEFAULT RESPONSE
    # =====================

    else:

        return """
### AI Business Insight

Customer satisfaction is influenced by:
- room quality
- pricing
- staff behavior
- cleanliness
- comfort

### Suggested Questions
- pricing complaints
- room quality issues
- customer satisfaction summary
- staff performance
"""