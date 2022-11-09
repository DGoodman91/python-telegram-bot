from telegram import Update
from telegram.ext import Application

from config_loader import ConfigLoader
from routing import RouterBuilder


class AppLoader():
    """
    A class responsible for initializing and running the application
    """

    async def post_init(self, app: Application) -> None:
        """ Post-initialization function, called before polling starts """
        print("Bot init complete, starting polling...")

    async def post_shutdown(self, app: Application) -> None:
        """ Shutdown function, use to close e.g., db connections """
        print("Bot shutting down. Beep boop bop....")

    def run(self) -> None:

        config = ConfigLoader().load_app_config()

        app = Application.builder().post_init(self.post_init).post_shutdown(
            self.post_shutdown).token(config['api_key']).build()

        # TODO without the assignment, the code behaves the same but with a problem -
        # the application has a race condition where sometimes it exits immediately
        app = RouterBuilder().add_handlers(app)

        app.run_polling()
