from telegram.ext import Application, CommandHandler, MessageHandler
import telegram.ext.filters

import handlers.help
import handlers.start
import handlers.unknown_command
import handlers.unknown_msg
import handlers.whoami


def add_handlers(app: Application):
    app.add_handler(CommandHandler('start', handlers.start.handle))
    app.add_handler(CommandHandler('help', handlers.help.handle))
    app.add_handler(CommandHandler('whoami', handlers.whoami.handle))
    app.add_handler(MessageHandler(telegram.ext.filters.COMMAND,
                    handlers.unknown_command.handle))
    app.add_handler(MessageHandler(
        telegram.ext.filters.TEXT, handlers.unknown_msg.handle))

