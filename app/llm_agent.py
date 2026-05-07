import requests
import os

API_KEY = os.getenv("GEMINI_API_KEY")

def ask_ai(question):

    context = """
    TravelIQ AI Hotel Insights:

    - Customers appreciate cleanliness.
    - Staff friendliness improves ratings.
    - Breakfast quality drives positive reviews.
    - Delayed room service causes complaints.
    - Poor WiFi causes negative reviews.
    """

    prompt = f"""
    You are an AI business intelligence assistant.

    Context:
    {context}

    User Question:
    {question}
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        result = response.json()

        print(result)

        if "candidates" in result:

            return result["candidates"][0]["content"]["parts"][0]["text"]

        elif "error" in result:

            return f"Gemini API Error: {result['error']['message']}"

        else:

            return f"Unexpected Response: {result}"

    except Exception as e:

        return f"AI Error: {str(e)}"