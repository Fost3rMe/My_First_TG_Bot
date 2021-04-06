import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests


def send_welcome(update: Update, _: CallbackContext) -> None:
    """
    Function that sending welcome message
    """
    update.message.reply_text("Для получения списка всех возможных команд введите /commands")


def get_commands(update: Update, _: CallbackContext) -> None:
    """
    Function for describing all functional of this bot
    """
    update.message.reply_text(f"Вы можете использовать следующие\n "
                              "команды:\n"
                              "/start - Инициализация\n"
                              "/commands - Вывести список доступных команд\n"
                              "/fact - получить интересный факт\n"
                              "/enable - включить уведомления \n"
                              "/disable - откючить уведомления \n"
                              "бот понимает следующие слова и предложения:\n"
                              "привет, пока, как дела?, как тебя зовут?")


def get_fact(update: Update, _: CallbackContext) -> None:
    """
    This function request information from repository and
    send message to the chat with information that was requested
    """
    fact_request = requests.get('https://cat-fact.herokuapp.com/facts/random')
    update.message.reply_text((fact_request.json()['text']))


def get_send_message(update: Update, _: CallbackContext) -> None:
    """
    This function created for sending messages
    in reply to users messages
    """
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
