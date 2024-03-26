
from telegram.ext import Updater, CommandHandler

# Define a function to handle the /hi command
def hi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")

def main():
    # Create the Updater and pass in your bot's token
    updater = Updater("6150264074:AAG03lem66RvmlMBowL5zO584RWiZi_RiYk", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the command handler for the /hi command
    dp.add_handler(CommandHandler("hi", hi))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
