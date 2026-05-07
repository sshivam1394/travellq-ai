import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def ask_ai(question):

    context = """
    TravelIQ AI Hotel Insights:

    - Customers appreciate cleanliness.
    - Friendly staff improves ratings.
    - Poor WiFi creates complaints.
    - Good breakfast increases satisfaction.
    - Slow room service causes negative reviews.
    """

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    payload = {
        "inputs": prompt
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        # Debug output
        print(response.text)

        if response.status_code != 200:
            return f"HF API Error: {response.text}"

        result = response.json()

        if isinstance(result, list):
            return result[0]["generated_text"]

        return str(result)

    except Exception as e:
        return f"AI Error: {str(e)}"