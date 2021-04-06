import telegram
from Core import Core_file
from Core import Bot
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1643056128:AAHIS74BGDDf7ldzj5DQLCFC1ZQv4JOvVEE")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", Bot.send_welcome))
    dispatcher.add_handler(CommandHandler("commands", Bot.get_commands))
    dispatcher.add_handler(CommandHandler("fact", Bot.get_fact))
    dispatcher.add_handler(CommandHandler("enable", Core_file.enable))
    dispatcher.add_handler(CommandHandler("disable", Core_file.disable))
    # dispatcher.add_handler(CommandHandler("help", help_command))
    #
    # # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, Bot.get_send_message))

    # Start the Bot
    updater.start_polling()

    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()