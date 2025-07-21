# 📰 AI News WhatsApp Bot 🤖

A Python bot that fetches the latest AI/Tech news, summarizes it using an LLM, and sends the update to your WhatsApp every day.

## 🚀 Features

- Automatically fetches top AI/Tech news using [Tavily Search API](https://www.tavily.com/)
- Summarizes news into simple, clear bullet points using an LLM (e.g., OpenAI, Groq, etc.)
- Sends both raw headlines and LLM-generated summaries to WhatsApp via Twilio
- Fully automated and runs daily at your chosen time

## 🧠 Tech Stack

- Python
- Tavily Search API (news fetching)
- OpenAI / Groq LLM API (summarization)
- Twilio WhatsApp API (message delivery)
- `schedule` (daily automation)

## 💬 Message Format

- 🗞️ *Headline section* with major news links
- 🧠 *LLM Summary* in simple natural language
- ✅ Bullet points for quick understanding

## ⚙️ How It Works

1. Fetches top tech/AI articles from Tavily
2. Summarizes them using an LLM in beginner-friendly language
3. Sends them to your WhatsApp daily using Twilio

## 🛠 Run Locally

```bash
git clone https://github.com/your-username/ai-news-whatsapp-bot.git
cd ai-news-whatsapp-bot
pip install -r requirements.txt
python app.py
