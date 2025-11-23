from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard(track, show_delete=False):
    kb = InlineKeyboardMarkup()
    if show_delete:
        kb.add(
            InlineKeyboardButton("Видалити ❌", callback_data=f"del_{track['id']}")
        )
    else:
        kb.add(
            InlineKeyboardButton("Вподобати ❤️", callback_data=f"fav_{track['id']}"),
            InlineKeyboardButton("Ще трек ▶️", callback_data="more")
        )
    return kb

def main():
    print("inline ok")