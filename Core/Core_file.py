import telebot
import requests
import datetime
from threading import Thread
import time

userlist =[]


bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')


class Fact:

    def __init__(self, url='https://cat-fact.herokuapp.com/facts/random'):
        self.url = url

    @property
    def some_fact(self):
        fact_request = requests.get(self.url)
        fact = fact_request.json()['text']
        return fact


def send_notifications():
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


@bot.message_handler(content_types=['text'])
def get_send_message(message):
    if message.text.lower() == 'enable notifications':
        userlist.append(message.from_user.id)

    elif message.text.lower() == 'disable notifications':
        userlist.remove(message.from_user.id)


repeatable_func.run()
bot.polling()
