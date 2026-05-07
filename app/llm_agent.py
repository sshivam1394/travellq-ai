import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-pro")

def ask_ai(question):

    context = """
    TravelIQ AI Insights:

    - Customers love hotel cleanliness.
    - Staff friendliness is highly appreciated.
    - Negative reviews mention delayed room service.
    - Breakfast quality receives positive feedback.
    """

    try:
        response = model.generate_content(
            f"""
            You are a travel intelligence AI assistant.

            Context:
            {context}

            User Question:
            {question}
            """
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"