import telebot

bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")




@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "i don't understand, sorry")

bot.polling()