from flask import Flask, request
import requests
import os

# Исправлено: добавлены подчеркивания name
app = Flask(__name__)

# Проверь названия в Render (Environment): если там BOT_TOKEN, исправь ниже на BOT_TOKEN
TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/')
def home():
    return "Bot is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные от TradingView
    data = request.json

    if not data:
        return "no data", 400

    # Берем текст сообщения из поля "message"
    message = data.get("message", "Signal")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    # Отправка запроса в Telegram
    requests.post(url, json=payload)
    
    return "ok", 200

# Исправлено: добавлены подчеркивания name == "__main__"
if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
