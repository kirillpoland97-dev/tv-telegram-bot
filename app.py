from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/')
def home():
    return f"Bot is running. TOKEN={TOKEN}, CHAT_ID={CHAT_ID}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("Incoming data:", data)
    print("TOKEN:", TOKEN)
    print("CHAT_ID:", CHAT_ID)

    if not data:
        return "no data"

    message = data.get("message", "Signal")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)

    print("Telegram response:", response.text)

    return response.text
