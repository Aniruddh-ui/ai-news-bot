import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_news(topic="AI and Tech developments"):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}"}
    payload = {
        "query": topic,
        "search_depth": "basic",
        "include_answer": True,
        "include_raw_content": False
    }

    response = requests.post(url, json=payload, headers=headers)
    results = response.json()
    articles = results.get("results", [])

    content = "\n\n".join([f"{i+1}. {a['title']}\n{a['url']}" for i, a in enumerate(articles[:5])])
    return content
