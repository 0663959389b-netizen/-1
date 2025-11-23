from keyboards.reply import get_reply_keyboard

def register_handlers(bot):
    @bot.message_handler(commands=["start", "help"])
    def start_cmd(msg):
        bot.send_message(
            msg.chat.id,
            "Привіт! Обери настрій:",
            reply_markup=get_reply_keyboard()
        )

def main():
    print("start.py ready.")