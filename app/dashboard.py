from review_agent import analyze_reviews
from recommendation_agent import generate_recommendations
from trend_agent import analyze_trends
from executive_agent import executive_summary
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from llm_agent import ask_ai
from report_agent import generate_report

from review_agent import analyze_reviews
from recommendation_agent import generate_recommendations
from trend_agent import analyze_trends
from executive_agent import executive_summary

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="TravellQ AI",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/processed/cleaned_reviews.csv"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #050816;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Titles */
h1, h2, h3, h4 {
    color: white;
}

/* KPI Cards */
[data-testid="metric-container"] {
    background: #111827;
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
}

/* Buttons */
.stButton > button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

/* Hover */
.stButton > button:hover {
    background-color: #ff2e2e;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🌍 TravellQ AI")

    menu = st.radio(
        "Navigation",
        [
            "Dashboard",
            "AI Insights",
            "Reviews",
            "AI Copilot",
            "Multi-Agent AI"
        ]
    )

# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":

    st.title("🌍 TravellQ AI")

    st.subheader(
        "AI-Powered Travel Intelligence Dashboard"
    )

    st.markdown("---")

    # =====================
    # KPI METRICS
    # =====================

    total_reviews = len(df)

    positive_reviews = len(
        df[df["review_sentiment"] == "POSITIVE"]
    )

    negative_reviews = len(
        df[df["review_sentiment"] == "NEGATIVE"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Reviews",
        f"{total_reviews:,}"
    )

    col2.metric(
        "Positive Reviews",
        f"{positive_reviews:,}"
    )

    col3.metric(
        "Negative Reviews",
        f"{negative_reviews:,}"
    )

    st.markdown("---")

    # =====================
    # PDF REPORT
    # =====================

    st.subheader("📄 Executive AI Report")

    if st.button("Generate PDF Report"):

        report_path = generate_report(df)

        with open(report_path, "rb") as file:

            st.download_button(
                label="⬇ Download Executive PDF",
                data=file,
                file_name="TravellQ_AI_Report.pdf",
                mime="application/pdf"
            )

        st.success(
            "Executive report generated successfully!"
        )

    st.markdown("---")

    # =====================
    # PIE CHART
    # =====================

    st.subheader("📊 Sentiment Distribution")

    sentiment_counts = (
        df["review_sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_counts.columns = [
        "Sentiment",
        "Count"
    ]

    fig = px.pie(
        sentiment_counts,
        names="Sentiment",
        values="Count",
        hole=0.5
    )

    fig.update_layout(
        paper_bgcolor="#050816",
        plot_bgcolor="#050816",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # =====================
    # WORD CLOUD
    # =====================

    st.subheader(
        "☁️ Customer Review Word Cloud"
    )

    review_text = " ".join(
        df["cleaned_review"]
        .dropna()
        .astype(str)
        .tolist()
    )

    wordcloud = WordCloud(
        width=1200,
        height=500,
        background_color="white"
    ).generate(review_text)

    fig_wc, ax = plt.subplots(
        figsize=(15, 7)
    )

    ax.imshow(
        wordcloud,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig_wc)

# =====================================================
# AI INSIGHTS
# =====================================================

elif menu == "AI Insights":

    st.title("🤖 AI Business Insights")

    st.markdown("---")

    positive_percentage = round(
        (
            len(
                df[
                    df["review_sentiment"]
                    == "POSITIVE"
                ]
            ) / len(df)
        ) * 100,
        2
    )

    negative_percentage = round(
        (
            len(
                df[
                    df["review_sentiment"]
                    == "NEGATIVE"
                ]
            ) / len(df)
        ) * 100,
        2
    )

    st.success(
        f"✅ {positive_percentage}% customers are satisfied."
    )

    st.error(
        f"⚠️ {negative_percentage}% customers are dissatisfied."
    )

    st.markdown("---")

    st.subheader(
        "💡 Strategic Recommendations"
    )

    st.markdown("""
    - Improve room cleanliness consistency

    - Increase pricing transparency

    - Enhance hospitality staff training

    - Improve complaint response speed

    - Monitor customer feedback regularly
    """)

# =====================================================
# REVIEWS PAGE
# =====================================================

elif menu == "Reviews":

    st.title("🗨️ Customer Reviews")

    st.markdown("---")

    sentiment_filter = st.selectbox(
        "Filter by Sentiment",
        [
            "All",
            "POSITIVE",
            "NEGATIVE"
        ]
    )

    filtered_df = df.copy()

    if sentiment_filter != "All":

        filtered_df = filtered_df[
            filtered_df["review_sentiment"]
            == sentiment_filter
        ]

    st.dataframe(
        filtered_df[
            [
                "cleaned_review",
                "review_sentiment",
                "confidence"
            ]
        ].head(100),

        use_container_width=True
    )

# =====================================================
# AI COPILOT
# =====================================================

elif menu == "AI Copilot":

    st.title("🤖 TravellQ AI Copilot")

    st.subheader(
        "AI-Powered Travel Intelligence Assistant"
    )

    st.markdown("---")

    user_question = st.text_input(
        "Ask a business question:"
    )

    if user_question:

        with st.spinner(
            "Analyzing customer reviews..."
        ):

            answer = ask_ai(
                user_question
            )

        st.success(answer)

# =====================================================
# MULTI-AGENT AI
# =====================================================

elif menu == "Multi-Agent AI":

    st.title(
        "🤖 Multi-Agent AI Control Center"
    )

    st.markdown("""
    Multiple AI agents collaboratively analyze
    customer intelligence and business insights.
    """)

    st.markdown("---")

    # =====================
    # REVIEW AGENT
    # =====================

    st.subheader(
        "📊 Review Intelligence Agent"
    )

    review_data = analyze_reviews()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Reviews",
        review_data["total_reviews"]
    )

    col2.metric(
        "Positive Reviews",
        review_data["positive_reviews"]
    )

    col3.metric(
        "Negative Reviews",
        review_data["negative_reviews"]
    )

    st.markdown("---")

    # =====================
    # RECOMMENDATION AGENT
    # =====================

    st.subheader(
        "💡 Recommendation Agent"
    )

    recommendations = (
        generate_recommendations()
    )

    for rec in recommendations:

        st.success(rec)

    st.markdown("---")

    # =====================
    # TREND AGENT
    # =====================

    st.subheader(
        "📈 Trend Analysis Agent"
    )

    trends = analyze_trends()

    for trend in trends:

        st.info(trend)

    st.markdown("---")

    # =====================
    # EXECUTIVE AGENT
    # =====================

    st.subheader(
        "🧠 Executive Summary Agent"
    )

    summary = executive_summary()

    st.warning(summary)