import os
from dotenv import load_dotenv
import telebot
from telegram_bot.handlers import start, messages, callbacks

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def main():
    start.register_handlers(bot)
    messages.register_handlers(bot)
    callbacks.register_handlers(bot)

    print("Starting bot polling...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
