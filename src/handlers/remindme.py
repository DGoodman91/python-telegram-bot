import re
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send the alarm message."""

    job = context.job

    if job == None:
        raise Exception('Cannot create an alarm for an empty job')

    await context.bot.send_message(job.chat_id, text=job.data)


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if context == None:
        raise Exception('Unexpected error - message received with no context')

    if context.args != None and (len(context.args) == 0 or context.args[0] == 'help'):
        await update.message.reply_text("Use the <b>/remindme</b> command to have me send you reminders at a specific time \
                \n      /remindme 30 Dinner's ready! -- <i>Send the <b>Dinner's ready!</b> message in 30 minutes</i>",
                                        parse_mode=ParseMode.HTML)
        return

    # first arg should be the time
    # e.g., 3d, 15m, 30s, 5h30m, 1.5h 15/11/2022|15:30
    time_seconds = parse_time_arg(context.args[0])

    # remaining args make up the text
    message = ' '.join(context.args[1:])

    context.job_queue.run_once(
        alarm, time_seconds,
        chat_id=update.effective_message.chat_id,
        name=str(update.effective_message.chat_id),
        data=message)

    await update.message.reply_text("Reminder set!")

    """
    TODO
    removereminder functionality (would be easiest if the user is returned a Job ID when they set it)
    repeating reminders? using the job_queue's run_daily and run_repeating methods https://pythontelegramrobot.readthedocs.io/en/latest/telegram.ext.jobqueue.html
    """


def parse_time_arg(time: str) -> float:
    """
    Takes a string representing the user's desired reminder time, and converts it to a seconds count

    Examples:
    12              Twelve minutes. Plain integers are interpreted as a minute count
    """

    seconds = 0

    if time == None:
        raise Exception('Can\'t set a reminder with no time requirement')

    if time.isdigit():
        seconds = 60 * int(time)

    exp = re.compile('[a-zA-Z]')
    letters = exp.findall(time)
    if letters == None or len(letters) == 0:
        """ We're either working with an expression like 5h10m or we have an invalid string """

    return seconds
