import Environment as environment

import Responses as responses

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Filters, Updater, MessageHandler, CommandHandler, CallbackQueryHandler, CallbackContext

print("Bot Launched!")

############################ Handlers #########################################
def start(update, context):
    update.message.reply_text(main_menu_message(),reply_markup=main_menu_keyboard())

def help(update, context):
    update.message.reply_text(main_menu_message(),reply_markup=main_menu_keyboard())

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

# Keyboard button
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == 'help_pattern':
        query.edit_message_text(text='I know a lot of movies, type something and I will try to answer with some movie quotes!')

    elif query.data == 'movie_pattern':
        query.edit_message_text(text='Hmmmm...\n1. The Thing.\n2. Alien\n3. Lord of the Rings\n4. The Matrix\n5. Snatch\n6. Shawshank Redemption\n7. Forrest Gump\n8. The Green Mile\n9. Gladiator\n10. Schindlers List')

    elif query.data == 'contact_pattern':
        query.edit_message_text(text='@Gregory_Savitsky')

# Keyboard menu
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Help', callback_data='help_pattern')],
              [InlineKeyboardButton('Contacts', callback_data='contact_pattern')],
              [InlineKeyboardButton('Movie recommendations', callback_data='movie_pattern')]]
  return InlineKeyboardMarkup(keyboard)

# Menu messages
def main_menu_message():
  return 'Take your pick:'

############################# Main func #########################################
def main():
    updater = Updater(environment.API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
