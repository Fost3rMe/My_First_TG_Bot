import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests


# from Core import Core_file


def send_welcome(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Howdy, how are you doing?")


def get_commands(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Вы можете использовать следующие "
                              "команды:{"
                              "/start - Инициализация"
                              "/commands - Вывести список доступных команд]"
                              "/fact - получить интересный факт"
                              "бот понимает следующие слова и предложения:"
                              "привет, пока, как дела?, как тебя зовут?")


def get_fact(update: Update, _: CallbackContext) -> None:
    fact_request = requests.get('https://cat-fact.herokuapp.com/facts/random')
    update.message.reply_text((fact_request.json()['text']))


def get_send_message(update: Update, _: CallbackContext) -> None:
    if update.message.text.lower() == 'привет':
        update.message.reply_text('Привет!')
    elif update.message.text.lower() == 'пока':
        update.message.reply_text('Пока')
    elif update.message.text.lower() == 'как дела?':
        update.message.reply_text('Хорошо, спасибо!')
    elif update.message.text.lower() == 'как тебя зовут?':
        update.message.reply_text('ББот.')
    else:
        update.message.reply_text('Прости, я тебя не понимаю.. '
                                  'Воспользуйся списком доступных команд / commands')
