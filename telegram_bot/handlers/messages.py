from states.user_states import get_spotify_tracks, get_favorites
from keyboards.inline import get_inline_keyboard

def register_handlers(bot):

    @bot.message_handler(func=lambda m: m.text == "⭐ Вподобані треки")
    def show_favorites(msg):
        favs = get_favorites(msg.chat.id)

        if not favs:
            bot.send_message(msg.chat.id, "Поки що немає вподобаних треків.")
            return

        for tr in favs:
            kb = get_inline_keyboard(tr, show_delete=True)
            bot.send_message(
                msg.chat.id,
                f"{tr['title']} — {tr['artist']} {tr['link']}",
                reply_markup=kb
            )

def main():
    print("messages.py готовий.")