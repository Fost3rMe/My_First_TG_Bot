from bot import notification_core
from bot import bot_core
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters)
from os import getenv


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(getenv("TOKEN"))
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", bot_core.send_welcome))
    dispatcher.add_handler(CommandHandler("commands", bot_core.get_commands))
    dispatcher.add_handler(CommandHandler("fact", bot_core.get_fact))
    dispatcher.add_handler(CommandHandler("enable", notification_core.enable))
    dispatcher.add_handler(CommandHandler("disable", notification_core.disable))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot_core.get_send_message))

    # Start the Bot
    updater.start_polling()

    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()