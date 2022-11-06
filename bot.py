from jproperties import Properties

from telegram import Update
from telegram.ext import Application

import routing

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

api_key = configs.get('api_key')
if api_key == None:
    raise Exception(
        'API key now found - add to app-config.properties file w/ key \'api_key\'')

app = Application.builder().token(api_key.data).build()

routing.add_handlers(app)

app.run_polling()
