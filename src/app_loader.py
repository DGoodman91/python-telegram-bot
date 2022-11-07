from telegram import Update
from telegram.ext import Application

from config_loader import ConfigLoader
from routing import RouterBuilder


class AppLoader():
    """
    A class responsible for initializing and running the application
    """

    def run(self) -> None:

        config = ConfigLoader().load_app_config()

        app = Application.builder().token(config['api_key']).build()

        # TODO without the assignment, the code behaves the same but with a problem -
        # the application has a race condition where sometimes it exits immediately
        app = RouterBuilder().add_handlers(app)

        app.run_polling()
