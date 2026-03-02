from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Берем настройки из Render
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные как текст (это надежнее для TradingView)
    signal_text = request.get_data(as_text=True)
    
    if not signal_text:
        return "Empty signal", 400

    # Твоё условие: игнорируем желтые точки
    if "yellow" in signal_text.lower():
        return "Ignored", 200

    # Отправляем основной сигнал
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🟦 НОВЫЙ СИГНАЛ 🟦\n\n{signal_text}",
        "parse_mode": "Markdown"
    }

    requests.post(url, json=payload)
    return "ok", 200

@app.route('/')
def home():
    return "Bot is running"

if name == "__main__":
    # Сразу шлем тест в группу при запуске
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": "✅ Бот успешно обновился и готов к работе!"})
    except:
        pass
    app.run(host="0.0.0.0", port=10000)
