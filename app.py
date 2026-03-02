import os
import telebot
from flask import Flask, request

# 1. Настройка ключей из Render
TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 2. Обработка сигналов от TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем текст алерта
    signal_text = request.data.decode('utf-8')
    
    if signal_text:
        # Проверяем, есть ли в тексте слово для желтой точки
        if "yellow" in signal_text.lower() or "точка" in signal_text.lower():
            formatted_text = f"🟡 **YELLOW DOT SIGNAL**\n\n{signal_text}"
        else:
            # По умолчанию — ярко-голубой сигнал
            formatted_text = f"🟦 **BRIGHT BLUE SIGNAL**\n\n{signal_text}"
        
        # Отправка в группу
        bot.send_message(CHAT_ID, formatted_text, parse_mode='Markdown')
    
    return 'OK', 200

# 3. Тестовая команда /start для проверки в личке
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, f"Бот на связи! Твой текущий Chat ID: {message.chat.id}")

# --- ТОТ САМЫЙ ТЕСТОВЫЙ БЛОК ---
# Этот код сработает ОДИН РАЗ при каждом запуске сервера на Render
try:
    bot.send_message(CHAT_ID, "🚀 Бот успешно запущен на Render!\nГотов принимать алерты из TradingView.")
except Exception as e:
    print(f"Ошибка при отправке тестового сообщения: {e}")
# -------------------------------

if name == "__main__":
    # Запуск сервера на порту 10000 (стандарт для Render)
    app.run(host="0.0.0.0", port=10000)
