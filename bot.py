from jproperties import Properties

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)


updater = Updater(
    configs.get('api_key').data, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Yo!")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Some helpful text..")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said {}".format(update.message.text))


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry {} is not a valid command".format(update.message.text))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()
