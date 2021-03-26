import telebot
import requests

bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')
fact_request = requests.get('https://cat-fact.herokuapp.com/facts/random')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['commands'])
def send_welcome(message):
    bot.reply_to(message, "Вы можете использовать следующие "
                          "команды:{"
                          "/start - Инициализация"
                          "/commands - Вывести список доступных команд]"
                          "/fact - получить интересный факт"
                          "бот понимает следующие слова и предложения:"
                          "привет, пока, как дела?, как тебя зовут?")


@bot.message_handler(commands=['fact'])
def get_fact(message):
    bot.reply_to(message, (fact_request.json()['text']))


@bot.message_handler(content_types=['text'])
def get_send_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    if message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Пока')
    if message.text.lower() == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо, спасибо!')
    if message.text.lower() == 'как тебя зовут?':
        bot.send_message(message.from_user.id, 'Бот. Джеймс Бот.')
    else:
        bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю.. '
                                               'Воспользуйся списком доступных команд / commands')




bot.polling()
