import telebot
import os
from dotenv import load_dotenv

def main():
    load_dotenv()  # Завантажує змінні оточення з файлу .env в системні змінні
    bot = telebot.TeleBot(os.getenv("TOKEN"))  # Ініціалізує бот за токеном з оточення

    @bot.message_handler(func=lambda message: True)  # Обробник усіх вхідних повідомлень
    def echo(message):
        bot.reply_to(message, message.text)  # Відповідає тим же текстом, що отримав

    print("Bot is running...")  # Виводить у консоль повідомлення про запуск бота
    bot.infinity_polling()  # Запускає безкінечний цикл прослуховування повідомлень

if __name__ == "__main__":  # Перевіряє, чи запускається цей скрипт напряму
    main()  # Викликає головну функцію для запуску бота
