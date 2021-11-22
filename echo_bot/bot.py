import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)


def hello(update, context):
    print("Вызван /start")
    update.message.reply_text("Приветствуем тебя, Пользователь!")


def echo(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", hello))
    dp.add_handler(MessageHandler(Filters.text, echo))

    logging.info("Bot starting...")

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
