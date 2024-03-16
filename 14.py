# https://core.telegram.org/bots/tutorial
# https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/blob/main/TutorialBot.py
# https://gitlab.com/Athamaxy/telegram-bot-tutorial
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackContext

# https://developers.giphy.com/docs/resource/#code-examples
import json
from urllib import parse, request

import random

TOKEN = '6980001366:AAECUyqOt21zGtaRR5tO0KNZjMbN3egOjd4'

# https://developers.giphy.com/docs/api/endpoint/#search
GIF_URL = 'https://api.giphy.com/v1/gifs/search'
MY_API_KEY = '4MvKHTrCuFPlaromzbdGRYnYpXddNiuA'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the GIF bot! Send a term or phrase\
 to search for GIFs.')


def echo(update: Update, context: CallbackContext) -> None:
    word = update.message.text

    params = parse.urlencode({
        "q": word,
        "api_key": MY_API_KEY,
        "limit": "5000"
    })

    with request.urlopen("".join((GIF_URL, "?", params))) as response:
        data = json.loads(response.read())

    if data["data"]:
        random_index = random.randint(0, len(data["data"]) - 1)
        gif_url = data["data"][random_index]["images"]["original"]["url"]
        update.message.reply_document(gif_url)
    else:
        update.message.reply_text("No GIF found for the given search term.")


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
