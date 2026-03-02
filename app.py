from flask import Flask, request
import requests
import os

# Исправлено: добавлены двойные подчеркивания name
app = Flask(__name__)

# Исправлено: названия переменных под твой Render (BOT_TOKEN)
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные от TradingView (как текст)
    signal_text = request.get_data(as_text=True)
    
    if not signal_text:
        return "Empty signal", 400

    # ГЛАВНОЕ УСЛОВИЕ: если в тексте есть "yellow", бот игнорирует это
    if "yellow" in signal_text.lower():
        print("Игнорирую желтую точку")
        return "Ignored", 200

    # Если слова "yellow" нет — это основной сигнал на вход
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Красиво оформляем основной сигнал
    formatted_message = f"🟦 НОВЫЙ СИГНАЛ НА ВХОД 🟦\n\n{signal_text}"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": formatted_message,
        "parse_mode": "Markdown"
    }

    requests.post(url, json=payload)
    return "ok", 200

@app.route('/')
def home():
    return "Bot is running and filtering yellow dots"

if name == "__main__":
    # Порт 10000 для Render
    app.run(host="0.0.0.0", port=10000)
