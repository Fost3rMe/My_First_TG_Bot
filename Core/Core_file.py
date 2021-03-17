import telebot

bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")