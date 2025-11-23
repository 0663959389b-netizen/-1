from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_reply_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton("⚡ Енергійний"),
        KeyboardButton("😢 Сумний"),
        KeyboardButton("😄 Щасливий"),
        KeyboardButton("😌 Спокійний"),
    )
    kb.add(
        KeyboardButton("⭐ Вподобані треки")
    )

    return kb

def main():
    print("reply ok")