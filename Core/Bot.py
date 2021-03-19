import telebot

bot = telebot.TeleBot('1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['commands'])
def send_welcome(message):
    bot.reply_to(message, "Вы можете использовать следующие "
                          "команды:{Здесь должен быть список команд}")


@bot.message_handler(content_types=['text'])
def get_send_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'привет')
    else:
        bot.send_message(message.from_user.id, 'what are u want?')


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, "i don't understand, sorry")


bot.polling()
