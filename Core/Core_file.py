import telebot
import requests
import datetime
from threading import Thread
import time

userlist = []
bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')


class Fact:
    """
    Class created for request some information from url
    By default class already have url of repository with random facts about cats
    """

    def __init__(self, url='https://cat-fact.herokuapp.com/facts/random'):
        self.url = url

    @property
    def some_fact(self):
        """
        Function for request fact in json format from repository
        :return: string with some information from repository
        """
        fact_request = requests.get(self.url)
        fact = fact_request.json()['text']
        return fact


def send_notifications():
    """
    Function created for start sending notifications with some format.
    It will send notifications every pointed period of time
    :return: String with information about today's date and time.
    some information. that were requested earlier
    """
    send_fact = Fact()
    send_text = send_fact.some_fact
    for user in userlist:
        bot.send_message(user,

                         f"Hello, my dear friend!\n"
                         f"today is {datetime.datetime.now()}\n"
                         f"Today some interesting fact about cats is:\n"
                         f"{send_text}"

                         )
    time.sleep(60)


class Repeated_func:

    def __init__(self, func):
        self.func = func
        self.isCancel = False

    def _run(self):
        while not self.isCancel:
            self.func()

    def run(self):
        self.isCancel = False
        thread = Thread(target=Repeated_func._run, args={self})
        thread.start()

    def stop(self):
        self.isCancel = True


repeatable_func = Repeated_func(send_notifications)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    This function created for sending welcome by bot
    Bot will answer to commands 'start' and 'help'
    :return: String with answer to command
    """
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def get_send_message(message):
    """
    This function appending user, who send message with text
    'enable notifications' to the userlist, who receive notifications.
    'disable notifications' will delete user from userlist
    """
    if message.text.lower() == 'enable notifications':
        userlist.append(message.from_user.id)

    elif message.text.lower() == 'disable notifications':
        userlist.remove(message.from_user.id)


@bot.message_handler(commands=['commands'])
def send_welcome(message):
    """
    This function sending message with all available commands in answer
    to next command '/commands'
    :return: Strings with all available commands
    """
    bot.reply_to(message, f"Вы можете использовать следующие команды:\n"
                          "\n"
                          "/start - Инициализация\n"
                          "/commands - Вывести список доступных команд\n"
                          "/fact - получить интересный факт\n"
                          "бот понимает следующие слова и предложения:\n"
                          "привет, пока, как дела?, как тебя зовут?")


@bot.message_handler(content_types=['text'])
def get_send_message(message):
    """
    This function created for bot's answering to simple messages
    by user
    :param message:
    :return: string with answer to user's message
    """
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Пока')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо, спасибо!')
    elif message.text.lower() == 'как тебя зовут?':
        bot.send_message(message.from_user.id, 'Бот. Джеймс Бот.')
    else:
        bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю.. '
                                               'Воспользуйся списком доступных команд / commands')


@bot.message_handler(commands=['fact'])
def get_fact(message, url_for_get = 'https://cat-fact.herokuapp.com/facts/random'):
    """
    This function created for getting only one fact
    :param message:
    :return:
    """
    fact_request = requests.get(url_for_get)
    bot.reply_to(message, (fact_request.json()['text']))


repeatable_func.run()
bot.polling()
