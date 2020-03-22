from coronaresultsbot.modules.get_covid_data import get_covid_data


def covid_spain(update, context):
    msg = get_covid_data('spain')
    update.message.reply_markdown(msg)


def covid_italy(update, context):
    msg = get_covid_data('italy')
    update.message.reply_markdown(msg)


def covid_france(update, context):
    msg = get_covid_data('france')
    update.message.reply_markdown(msg)


def covid_germany(update, context):
    msg = get_covid_data('germany')
    update.message.reply_markdown(msg)


def covid_china(update, context):
    msg = get_covid_data('china')
    update.message.reply_markdown(msg)


def covid_usa(update, context):
    msg = get_covid_data('us')
    update.message.reply_markdown(msg)


def covid_uk(update, context):
    msg = get_covid_data('uk')
    update.message.reply_markdown(msg)


def covid_other(update, context):
    country = context.args[0].lower()
    msg = get_covid_data(country)
    update.message.reply_markdown(msg)


def start(update, context):
    update.message.reply_text('Hey! How are you? You can take a look at my commands or type /help for more info.')


def help(update, context):
    update.message.reply_markdown("These are my available commands. You can also find them below, next to the message input.\
                                    \n\n*Statistics for most affected countries:*\
                                    \n/covid\_spain - Spain 🇪🇸\
                                    \n/covid\_italy - Italy 🇮🇹\
                                    \n/covid\_france - France 🇫🇷\
                                    \n/covid\_germany - Germany 🇩🇪\
                                    \n/covid\_china - China 🇨🇳\
                                    \n/covid\_usa - USA 🇺🇸\
                                    \n/covid\_uk - UK 🇬🇧\
                                    \n\nYou can also try other countries that are not in the previous list. Start typing /covid and the name of the country.\
                                    \n\nFor example:\
                                    \n/covid sweden")
