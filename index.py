from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TELEGRAM_BOT_TOKEN = '7447541615:AAG4kskqSZyaP6Yoi5ulzMD1Z6Yi4VKpQGE'
TARGET_CHAT_ID = 7106111501

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a file and I will forward it to the specified chat.')

def handle_file(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file.download('downloaded_file')

    with open('downloaded_file', 'rb') as f:
        context.bot.send_document(chat_id=TARGET_CHAT_ID, document=InputFile(f))

    update.message.reply_text('File has been forwarded!')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_file))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
