import Environment as environment
from telegram.ext import *
import Responses as responses

print("Bot Launched!")


def start_command(update, context):
    update.message.reply_text('Hello there!')


def help_command(update, context):
    update.message.reply_text('What is thy bidding, master?')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(environment.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

main()
