from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_ai(question):

    sample_context = """
    TravelIQ AI Hotel Review Insights:

    - Most customers liked hotel cleanliness.
    - Staff friendliness is highly appreciated.
    - Negative reviews mention room service delays.
    - Breakfast quality is praised frequently.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    You are a travel intelligence AI assistant.

                    Use this hotel review context:

                    {sample_context}
                    """
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"