import ephem
import logging
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
from variables import PLANETS, INFO_TEXT, SOLAR_STRUCTURE_TEXT, HELLO_TEXT

logging.basicConfig(filename="bot.log", level=logging.INFO)


def hello(update, context):
    logging.info("Call method /start")

    update.message.reply_text(HELLO_TEXT.format(username=update.message.chat.username))


def info(update, context):
    logging.info("Call method /help")

    update.message.reply_text(INFO_TEXT)


def get_constellation_by_planet(update, context):
    logging.info("Call method /planet")

    today = date.today()
    command_words = update.message.text.split()  # /planet Mars

    if len(command_words) < 2:
        update.message.reply_text("‼️ Вы не указали название планеты!" + SOLAR_STRUCTURE_TEXT)
        return

    if len(command_words) > 2:
        update.message.reply_text("‼️ Вы указали слишком много данных! Нужно указать только название планеты")
        return

    planet = command_words[1].lower()
    if planet not in PLANETS:
        update.message.reply_text("‼️ Вы указали неверное название планеты!" + SOLAR_STRUCTURE_TEXT)
        return

    if planet in ["sun", "солнце"]:
        update.message.reply_text("Солнце ☀️ - это звезда, а не планета")
        return

    if planet in ["земля", "earth"]:
        update.message.reply_text("Вы находитесь как раз на Земле 🌎")
        return

    if planet in ["луна", "moon"]:
        update.message.reply_text("Луна 🌛 является спутником Земли 🌎")
        return

    if planet in ["плутон", "pluto"]:
        update.message.reply_text("Плутон, к сожалению, с 2006 года не является планетой Солнечной системы")
        return

    planet_api = getattr(ephem, PLANETS[planet])(today.strftime("%Y/%m/%d"))
    _, constellation_name = ephem.constellation(planet_api)

    update.message.reply_text(f"Сегодня планета {planet.capitalize()} находится в созвездии {constellation_name}")


def echo(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", hello))
    dp.add_handler(CommandHandler("help", info))
    dp.add_handler(CommandHandler("planet", get_constellation_by_planet))
    dp.add_handler(MessageHandler(Filters.text, echo))

    logging.info("Bot starting...")

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
