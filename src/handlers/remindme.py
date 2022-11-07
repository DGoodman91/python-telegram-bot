from telegram import Update
from telegram.ext import ContextTypes


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send the alarm message."""

    job = context.job

    if job == None:
        raise Exception('Cannot create an alarm for an empty job')

    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if context == None:
        raise Exception('Unexpected error - message received with no context')

    if context.args != None and (len(context.args) == 0 or context.args[0] == 'help'):
        await update.message.reply_text('TODO helpful text explaining the remindme command! :D')
        return

    # first arg should be the time
    # e.g., 3d, 15m, 30s, 15/11/2022|15:30
    time_seconds = 60

    # second arg should be the text
    message = 'Testing the reminder blud'

    context.job_queue.run_once(
        alarm, time_seconds, chat_id=update.effective_message.chat_id, name=str(update.effective_message.chat_id), data=time_seconds)

    await update.message.reply_text("Reminder set!")
