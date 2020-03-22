import os


ENV = os.getenv('ENV')
BOT_TOKEN = os.getenv('BOT_TOKEN')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
PORT = int(os.environ.get("PORT", "8443"))