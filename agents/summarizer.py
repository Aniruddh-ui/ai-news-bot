import os
import requests
import json

def summarize_news(news_text):
    api_key = os.getenv("LLM_API_KEY")
    endpoint = "https://openrouter.ai/api/v1/chat/completions"

    if not api_key:
        print("❌ Missing LLM_API_KEY environment variable.")
        return "⚠️ Missing API key for summarization."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a friendly assistant that summarizes AI and tech news for a daily WhatsApp newsletter. "
                    "Keep the tone simple, natural, and easy for a general audience to understand. "
                    "Start with a short headline or title. Then give 3–5 key points as bullet points. "
                    "Avoid technical jargon. Use emojis only if appropriate."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Summarize the following news articles into a WhatsApp-friendly summary. "
                    f"Use natural language and keep it under 1500 characters:\n\n{news_text}"
                )
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        result = response.json()

        print("🔎 Raw LLM response:\n", json.dumps(result, indent=2))

        if 'choices' in result:
            summary = result['choices'][0]['message']['content']
            return summary.strip()
        elif 'error' in result:
            print("❌ LLM API returned error:", result['error'].get('message'))
            return f"⚠️ LLM Error: {result['error'].get('message')}"
        else:
            print("⚠️ Unexpected LLM response format.")
            return "⚠️ Could not summarize the news. Unexpected response."

    except Exception as e:
        print("❌ Exception occurred while summarizing:", e)
        return "⚠️ Summary failed due to an exception."
