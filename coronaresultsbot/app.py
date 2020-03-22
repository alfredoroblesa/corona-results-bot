import sys
import datetime
import logging
from coronaresultsbot.settings import config
from coronaresultsbot.modules import handlers
from coronaresultsbot.modules import utilities
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    """Log errors caused by updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Starting the bot."""
    logging.info('Starting at %s' % datetime.datetime.now())
    updater = Updater(token=config.BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handlers.start))
    dp.add_handler(CommandHandler("help", handlers.help))
    dp.add_handler(CommandHandler("covid_spain", handlers.covid_spain))
    dp.add_handler(CommandHandler("covid_italy", handlers.covid_italy))
    dp.add_handler(CommandHandler("covid_france", handlers.covid_france))
    dp.add_handler(CommandHandler("covid_germany", handlers.covid_germany))
    dp.add_handler(CommandHandler("covid_china", handlers.covid_china))
    dp.add_handler(CommandHandler("covid_usa", handlers.covid_usa))
    dp.add_handler(CommandHandler("covid_uk", handlers.covid_uk))
    dp.add_handler(CommandHandler("covid", handlers.covid_other))

    # Log all errors
    dp.add_error_handler(error)

    # Configure mode of operation
    mode = config.ENV
    if mode == "dev":
        updater.start_polling()
        updater.idle()
    elif mode == "prod":
        updater.start_webhook(listen="0.0.0.0", port=config.PORT, url_path=config.BOT_TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(config.HEROKU_APP_NAME, config.BOT_TOKEN))
    else:
        logger.error("No environment mode was specified. Exiting...")
        sys.exit()