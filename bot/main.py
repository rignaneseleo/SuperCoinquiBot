# SuperCoinquiBot is an Open Source bot developed by Leonardo Rignanese <dev.rignanese@gmail.com>
# GNU General Public License v3.0
# GITHUB: https://github.com/rignaneseleo/SuperCoinquiBot

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CallbackQueryHandler, CommandHandler, ChosenInlineResultHandler

from bot_token import get_token
from src.flat import Flat

flats = {}

updater = Updater(get_token())
dispatcher = updater.dispatcher

# Setup the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# To create a button response
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


# Define the replies
def get_flatmates_names(bot, update):
    message = ""
    chat_id = update.message.chat_id

    # Check if the flat is registered
    if chat_id not in flats:
        bot.send_message(chat_id=chat_id, text="La tua casa non esiste ancora, creane una! (es: '/start Falentex')")
        return
    flat = flats[chat_id]

    flatmates_names = flat.get_flatmates_names().strip(',.')
    # Check if there are flatmates
    if flatmates_names is not '':
        message = "I coinqui di " + flat.name + " sono: " + flatmates_names
    else:
        message = "Non ci sono ancora conquilini registrati. Aggiungili con /nuovoCoinqui *nome*"

    # If there is a message to send, send it
    if message: bot.send_message(chat_id=chat_id, text=message)


def add_flatmate(bot, update, args):
    message = ""
    chat_id = update.message.chat_id

    # Check if the flat is registered
    if chat_id not in flats:
        bot.send_message(chat_id=chat_id, text="La tua casa non esiste ancora, creane una! (es: '/start Falentex')")
        return
    flat = flats[chat_id]

    nickname = ' '.join(args).strip(',.')
    if nickname is not '':
        # Try to add the new flatmate
        if flat.add_flatmate(nickname):
            message = nickname + " aggiunto alla casa " + flat.name
        else:
            message = nickname + " esiste già"
    else:
        message = "Scrivere il nome del coinqui (es: '/nuovoCoinqui Leo')"

    # If there is a message to send, send it
    if message: bot.send_message(chat_id=chat_id, text=message)


def remove_flatmate(bot, update, args):
    message = ""
    chat_id = update.message.chat_id

    # Check if the flat is registered
    if chat_id not in flats:
        bot.send_message(chat_id=chat_id, text="La tua casa non esiste ancora, creane una! (es: '/start Falentex')")
        return
    flat = flats[chat_id]

    nickname = ' '.join(args).strip(',.')
    if nickname is not '':
        # Try to add the new flatmate
        if flat.remove_flatmate(nickname):
            message = nickname + " rimosso dalla casa " + flat.name
        else:
            flatmates_names = flat.get_flatmates_names().strip(',.')
            # Check if there are flatmates
            if flatmates_names is not '':
                message = "I coinqui di " + flat.name + " sono: " + flatmates_names + ". " + nickname + " non esiste."
            else:
                message = "Non ci sono ancora conquilini registrati. Aggiungili con /nuovoCoinqui *nome*"
    else:
        message = "Scrivere il nome del coinqui (es: '/cacciaCoinqui Leo')"

    # If there is a message to send, send it
    if message: bot.send_message(chat_id=chat_id, text=message)


def start(bot, update, args):
    message = ""
    chat_id = update.message.chat_id
    name = ' '.join(args).strip()

    # Check if it is null
    if name is not '':
        # Check if it already exist
        if chat_id not in flats:
            flats[chat_id] = Flat(name)
            message = "Creata la casa numero " + str(flats.__len__()) + ": " + name
        else:
            message = "Esiste già una casa per questa chat (guarda i /comandi)"
    else:
        message = "Scrivere il nome della casa (es: '/start Falentex')"

    # If there is a message to send, send it
    button_list = [
        InlineKeyboardButton("nuovo", callback_data="/coinqui"),
        InlineKeyboardButton("credits", callback_data="/credits"),
        InlineKeyboardButton("coinqui", callback_data="/coinqui")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="A two-column menu", reply_markup=reply_markup)
    # if message: bot.send_message(chat_id=chat_id, text=message)


def inl(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="o")


def credits(bot, update):
    message = ""
    chat_id = update.message.chat_id

    message = "Bot realizzato da Leonardo Rignanese <dev.rignaneseleo@gmail.com>"

    # If there is a message to send, send it
    if message: bot.send_message(chat_id=chat_id, text=message)


# Attach the replies to the queries
dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
<<<<<<< HEAD
dispatcher.add_handler(CallbackQueryHandler(inl))

=======
>>>>>>> origin/master

dispatcher.add_handler(CommandHandler('nuovoCoinqui', add_flatmate, pass_args=True))

dispatcher.add_handler(CommandHandler('cacciaCoinqui', remove_flatmate, pass_args=True))

dispatcher.add_handler(CommandHandler('coinqui', get_flatmates_names))

dispatcher.add_handler(CommandHandler('credits', credits))

# Start the service
updater.start_polling()
