import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from review_agent import analyze_reviews
from llm_agent import ask_ai
from report_agent import generate_report


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="TravelIQ AI",
    page_icon="🌍",
    layout="wide"
)

# =========================
# SAMPLE DATA
# =========================
sample_data = {
    "review": [
        "Excellent hotel and friendly staff",
        "Room was clean and beautiful",
        "Bad room service experience",
        "Amazing breakfast and hospitality",
        "Very slow check-in process",
        "Wonderful stay and excellent food",
        "Dirty bathroom and rude staff",
        "Loved the ambience and location"
    ],
    "sentiment": [
        "POSITIVE",
        "POSITIVE",
        "NEGATIVE",
        "POSITIVE",
        "NEGATIVE",
        "POSITIVE",
        "NEGATIVE",
        "POSITIVE"
    ]
}

df = pd.DataFrame(sample_data)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🌍 TravelIQ AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Insights",
        "Reviews",
        "AI Copilot",
        "PDF Report"
    ]
)

# =========================
# DASHBOARD
# =========================
if page == "Dashboard":

    st.title("🌍 TravelIQ AI")
    st.subheader("AI-Powered Travel Intelligence Dashboard")

    total_reviews = len(df)

    positive_reviews = len(
        df[df["sentiment"] == "POSITIVE"]
    )

    negative_reviews = len(
        df[df["sentiment"] == "NEGATIVE"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Reviews",
        total_reviews
    )

    col2.metric(
        "Positive Reviews",
        positive_reviews
    )

    col3.metric(
        "Negative Reviews",
        negative_reviews
    )

    st.divider()

    # =========================
    # SENTIMENT CHART
    # =========================
    st.subheader("📊 Sentiment Distribution")

    sentiment_counts = (
        df["sentiment"]
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
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # WORD CLOUD
    # =========================
    st.subheader("☁️ Review Word Cloud")

    text = " ".join(df["review"])

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    fig_wc, ax = plt.subplots()

    ax.imshow(
        wordcloud,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig_wc)

# =========================
# AI INSIGHTS
# =========================
elif page == "AI Insights":

    st.title("🤖 AI Insights")

    insights = analyze_reviews()

    st.success(
        f"""
        Positive Reviews: {insights['positive_reviews']}

        Negative Reviews: {insights['negative_reviews']}
        """
    )

# =========================
# REVIEWS PAGE
# =========================
elif page == "Reviews":

    st.title("📝 Hotel Reviews")

    st.dataframe(df)

# =========================
# AI COPILOT
# =========================
elif page == "AI Copilot":

    st.title("🧠 AI Travel Copilot")

    user_question = st.text_input(
        "Ask anything about hotel reviews:"
    )

    if st.button("Ask AI"):

        if user_question:

            with st.spinner("Thinking..."):

                answer = ask_ai(user_question)

                st.success(answer)

# =========================
# PDF REPORT
# =========================
elif page == "PDF Report":

    st.title("📄 AI PDF Report")

    if st.button("Generate PDF Report"):

        report_path = generate_report()

        with open(report_path, "rb") as file:

            st.download_button(
                label="Download Report",
                data=file,
                file_name="TravelIQ_Report.pdf",
                mime="application/pdf"
            )