from twilio.rest import Client
import os

def send_whatsapp_message(body):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    message = client.messages.create(
        from_=os.getenv("TWILIO_PHONE"),
        body=body,
        to=os.getenv("USER_PHONE")
    )
    return message.sid
