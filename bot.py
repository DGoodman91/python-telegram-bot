from jproperties import Properties

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler
import telegram.ext.filters


configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)


app = Application.builder().token(configs.get('api_key').data).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Some helpful text..")


async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry I can't recognize you , you said {}".format(update.message.text))


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry {} is not a valid command".format(update.message.text))

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(telegram.ext.filters.COMMAND, unknown))
app.add_handler(MessageHandler(telegram.ext.filters.TEXT, unknown_text))
app.run_polling()
