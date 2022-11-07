from telegram.ext import Application, CommandHandler, MessageHandler, filters

import handlers.help
import handlers.remindme
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

        app.add_handlers([CommandHandler('start', handlers.start.handle),
                          CommandHandler('help', handlers.help.handle),
                          CommandHandler('remindme', handlers.remindme.handle),
                          CommandHandler('whoami', handlers.whoami.handle),
                          MessageHandler(
                              filters.TEXT, handlers.unknown_msg.handle),
                          MessageHandler(filters.COMMAND,
                                         handlers.unknown_command.handle)
                          ])

        return app
