from flask import Flask, request
import requests
import os

# ИСПРАВЛЕНО: Добавлены подчеркивания name
app = Flask(__name__)

# Данные из Render
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные от TradingView
    signal_text = request.get_data(as_text=True)
    
    if not signal_text:
        return "Empty", 400

    # ТВОЕ УСЛОВИЕ: Игнорируем желтые точки
    if "yellow" in signal_text.lower():
        return "Ignored", 200

    # Отправляем только важные сигналы на вход
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🟦 НОВЫЙ СИГНАЛ НА ВХОД 🟦\n\n{signal_text}",
        "parse_mode": "Markdown"
    }

    requests.post(url, json=payload)
    return "ok", 200

@app.route('/')
def home():
    return "Bot is running"

# ИСПРАВЛЕНО: Добавлены подчеркивания name и main
if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
