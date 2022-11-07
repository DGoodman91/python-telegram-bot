from telegram.ext import Application, CommandHandler, MessageHandler, filters

import handlers.help
import handlers.start
import handlers.unknown_command
import handlers.unknown_msg
import handlers.whoami


class RouterBuilder():
    """
    A class to handle the routing of telegram messages/commands to the rest of our app
    """

    def add_handlers(self, app: Application):
        """
        Attach handlers (BaseHandler instances) to the telegram Application instance
        """

        app.add_handler(CommandHandler('start', handlers.start.handle))
        app.add_handler(CommandHandler('help', handlers.help.handle))
        app.add_handler(CommandHandler('whoami', handlers.whoami.handle))
        app.add_handler(MessageHandler(filters.COMMAND,
                        handlers.unknown_command.handle))
        app.add_handler(MessageHandler(
            filters.TEXT, handlers.unknown_msg.handle))

        return app
