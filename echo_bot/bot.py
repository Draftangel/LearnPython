import ephem
import logging
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
from variables import PLANETS

logging.basicConfig(filename="bot.log", level=logging.INFO)


def hello(update, context):
    print("Call method /start")
    logging.info("Call method /start")

    message = '''
{username}, тебя приветствует бот!
Чтобы узнать возможности бота введи команду /help
    '''.format(username=update.message.chat.username)

    update.message.reply_text(message)


def info(update, context):
    print("Call method /help")
    logging.info("Call method /help")

    command_list = '''
Данный бот является подпольной разработкой и имеет следующий набор команд:
/start - выводит приветственное сообщение
/help - выводит список доступных команд
/planet [имя_планеты] - возвращает название созвездия (eng), где в данный момент находится указанная планета Солнечной системы
    '''

    update.message.reply_text(command_list)


def get_constellation_by_planet(update, context):
    print("Call method /planet")
    logging.info("Call method /planet")

    today = date.today()
    command_words = update.message.text.split()  # /planet Mars

    solar_structure_message = '''\n
⚠️ Текущая структура Солнечной системы (за исключением Земли (Earth)) следующая:
    - Mercury (Меркурий)
    - Venus (Венера)
    - Mars (Марс)
    - Jupiter (Юпитер)
    - Saturn (Сатурн)
    - Uranus (Уран)
    - Neptune (Нептун)
    '''

    if len(command_words) < 2:
        message = "‼️ Вы не указали название планеты!" + solar_structure_message
    elif len(command_words) > 2:
        message = "‼️ Вы указали слишком много данных! Нужно указать только название планеты"
    else:
        planet = command_words[1].lower()
        if planet not in PLANETS:
            message = "‼️ Вы указали неверное название планеты!" + solar_structure_message
        else:
            if planet in ["sun", "солнце"]:
                message = "Солнце ☀️ - это звезда, а не планета"
            elif planet in ["земля", "earth"]:
                message = "Вы находитесь как раз на Земле 🌎"
            elif planet in ["луна", "moon"]:
                message = "Луна 🌛 является спутником Земли 🌎"
            elif planet in ["плутон", "pluto"]:
                message = "Плутон, к сожалению, с 2006 года не является планетой Солнечной системы"
            else:
                planet_api = getattr(ephem, PLANETS[planet])(today.strftime("%Y/%m/%d"))
                (_, constellation_name) = ephem.constellation(planet_api)

                message = f"Сегодня планета {planet.capitalize()} находится в созвездии {constellation_name}"

    update.message.reply_text(message)


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
