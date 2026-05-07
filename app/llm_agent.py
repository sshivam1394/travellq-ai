import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "models/text-bison-001"
)

def ask_ai(question):

    context = """
    TravelIQ AI Hotel Insights:

    - Customers appreciate cleanliness.
    - Staff friendliness improves ratings.
    - Delayed room service causes complaints.
    - Breakfast quality drives positive reviews.
    """

    try:

        response = model.generate_content(
            f"""
            You are a travel business intelligence AI assistant.

            Context:
            {context}

            User Question:
            {question}
            """
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"