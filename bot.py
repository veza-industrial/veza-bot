import telebot
from flask import Flask

TOKEN = "8504429096:AAG05ods1PkzB439YtiI1VA19wFqykMsFrU"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "VEZA AU 135 калькулятор\n\nВведите тоннаж металлоконструкций (в тоннах):"
    )

@bot.message_handler(func=lambda message: message.text.replace('.', '', 1).isdigit())
def calculate(message):
    tonnage = float(message.text)

    consumption_per_ton = 10
    total_consumption = tonnage * consumption_per_ton
    barrels = total_consumption / 25

    production_per_hour = 5
    hours_needed = tonnage / production_per_hour
    shifts_8h = hours_needed / 8
    shifts_16h = hours_needed / 16

    result = f"""
VEZA AU 135 — расчет

Объем: {tonnage} т

Расход: {total_consumption:.0f} кг
Бочек 25 кг: {barrels:.0f}

Производительность: 5 т/час
Часов работы: {hours_needed:.1f}

Смен (8 часов): {shifts_8h:.1f}
Смен (2 смены): {shifts_16h:.1f}

Сопло:
крупные конструкции — 317
мелкие конструкции — 215

Высыхание до кантования — 1 час
Отгрузка — через 24 часа
"""
    bot.reply_to(message, result)

@app.route('/')
def home():
    return "VEZA bot is running"

if __name__ == "__main__":
    print("Bot started")
    bot.infinity_polling()
