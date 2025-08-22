import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hi! I am your NEET PG bot. How can I help you today?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == "__main__":
    bot.polling()
