from telegram import Update
from telegram.ext import ContextTypes


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if user != None:
        await update.message.reply_text("You are user {0}, {1}".format(user.id, user.full_name))
    else:
        print('[ERROR] Message received with no effective user')
