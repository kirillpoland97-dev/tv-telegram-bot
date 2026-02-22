from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "Signal")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)
    return "ok"

@app.route('/')
def home():
    return "Bot is running"
