from agents.news_fetcher import fetch_news
from agents.summarizer import summarize_news
from agents.messenger import send_whatsapp_message
from dotenv import load_dotenv
import schedule
import time
import os
from twilio.rest import Client

load_dotenv()

def send_long_whatsapp_message(body, header=""):
    """
    Sends a long WhatsApp message by splitting it into parts of ≤1500 characters.
    """
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH")
    from_number = os.getenv("TWILIO_PHONE")
    to_number = os.getenv("USER_PHONE")

    client = Client(account_sid, auth_token)

    chunk_size = 1500
    chunks = [body[i:i+chunk_size] for i in range(0, len(body), chunk_size)]

    for i, chunk in enumerate(chunks):
        prefix = f"{header} (Part {i+1}/{len(chunks)})\n\n" if len(chunks) > 1 else f"{header}\n\n"
        client.messages.create(
            from_=from_number,
            body=prefix + chunk,
            to=to_number
        )

def run_daily_news_bot():
    print("[+] Fetching news...")
    news = fetch_news()
    print("[+] News fetched.")

    print("[+] Summarizing...")
    summary = summarize_news(news)
    print("[+] Summary complete.")

    print("[+] Sending to WhatsApp...")
    send_whatsapp_message("📰 *Top AI/Tech News Today:*\n\n" + news)
    send_long_whatsapp_message(summary, header="🤖 *LLM Summary:*")

    print("[+] All messages sent.")

if __name__ == "__main__":
    run_daily_news_bot()

schedule.every().day.at("03:30").do(run_daily_news_bot)  # 3:30 UTC = 9:00 IST


while True:
    schedule.run_pending()
    time.sleep(60)
