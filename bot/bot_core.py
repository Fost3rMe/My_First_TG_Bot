from telegram import Update
from telegram.ext import CallbackContext
import requests


def send_welcome(update: Update, ctx: CallbackContext) -> None:
    """
    Function that sending welcome message
    """
    update.message.reply_video('https://media.tenor.com/images/3cb6d1676da200afa69c3c9417f14338/tenor.gif')
    update.message.reply_text("I'm glad to see you, my friend!")
    update.message.reply_text("Для получения списка всех возможных команд введите /commands")


def get_commands(update: Update, ctx: CallbackContext) -> None:
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


def get_fact(update: Update, ctx: CallbackContext) -> None:
    """
    This function request information from repository and
    send message to the chat with information that was requested
    """
    fact_request = requests.get('https://cat-fact.herokuapp.com/facts/random')
    update.message.reply_text((fact_request.json()['text']))


def get_send_message(update: Update, ctx: CallbackContext) -> None:
    """
    This function created for sending messages
    in reply to users messages
    """
    if update.message.text.lower() == 'привет':
        update.message.reply_text('Привет!')
    elif update.message.text.lower() == 'пока':
        update.message.reply_video('https://media1.tenor.com/images/32208bdd6985e281961bf837710ad5a1/tenor.gif?itemid'
                                   '=9703234')
        update.message.reply_text('Пока-пока:)')
    elif update.message.text.lower() == 'как дела?':
        update.message.reply_text('Хорошо, спасибо!')
    elif update.message.text.lower() == 'как тебя зовут?':
        update.message.reply_text('ББот.')
    else:
        update.message.reply_text('Прости, я тебя не понимаю.. '
                                  'Воспользуйся списком доступных команд / commands')
