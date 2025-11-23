from telegram_bot.states.user_states import add_favorite, remove_favorite, clear_history, get_spotify_tracks
from telegram_bot.keyboards.inline import get_inline_keyboard

user_moods = {}
user_tracks = {}

def register_handlers(bot):

    @bot.message_handler(func=lambda m: m.text in ["⚡ Енергійний", "😢 Сумний", "😄 Щасливий", "😌 Спокійний"])
    def set_user_mood(message):
        mood = message.text.split(" ", 1)[1]  # прибираємо смайлик
        user_moods[message.chat.id] = mood

        clear_history(message.chat.id)  # очищення історії треків перед новим пошуком

        tracks = get_spotify_tracks(mood, count=3, chat_id=message.chat.id)
        user_tracks[message.chat.id] = tracks

        for tr in tracks:
            bot.send_message(
                message.chat.id,
                f"{tr['title']} — {tr['artist']} {tr['link']}",
                reply_markup=get_inline_keyboard(tr, show_delete=False)
            )

    @bot.callback_query_handler(func=lambda call: call.data == "more")
    def more_track(call):
        mood = user_moods.get(call.message.chat.id, "Спокійний")
        tracks = get_spotify_tracks(mood, count=1, chat_id=call.message.chat.id)
        if call.message.chat.id in user_tracks:
            user_tracks[call.message.chat.id].extend(tracks)
        else:
            user_tracks[call.message.chat.id] = tracks

        tr = tracks[0] if tracks else None
        if tr:
            bot.send_message(
                call.message.chat.id,
                f"{tr['title']} — {tr['artist']} {tr['link']}",
                reply_markup=get_inline_keyboard(tr, show_delete=False)
            )
        else:
            bot.send_message(call.message.chat.id, "Більше немає треків для цього настрою.")
        bot.answer_callback_query(call.id)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("fav_"))
    def callback_fav(call):
        track_id = call.data[4:]
        tracks = user_tracks.get(call.message.chat.id, [])
        tr = next((t for t in tracks if t["id"] == track_id), None)
        if tr:
            add_favorite(call.message.chat.id, tr)
            bot.answer_callback_query(call.id, "Додано у вподобані!")
        else:
            bot.answer_callback_query(call.id, "Трек не знайдено.")

    @bot.callback_query_handler(func=lambda call: call.data.startswith("del_"))
    def callback_del(call):
        track_id = call.data[4:]
        remove_favorite(call.message.chat.id, track_id)
        bot.answer_callback_query(call.id, "Видалено з вподобаних.")
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            print(f"Не вдалося видалити повідомлення: {e}")

def main():
    print("callbacks.py готов.")