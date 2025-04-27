from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import os

# Initialize Flask and Telegram Bot
app = Flask(__name__)
API_TOKEN = 'YOUR_BOT_API_TOKEN'  # Replace with your Bot's token
bot = Bot(API_TOKEN)
dispatcher = Dispatcher(bot, update_queue=None, workers=0)

# Command to start the bot and send a welcome message
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the RPG Game!")

# Add other commands like /stats, /fight, etc.
def stats(update: Update, context: CallbackContext):
    update.message.reply_text("Here are your stats...")

# Register the command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("stats", stats))

# Set up the webhook endpoint
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return 'OK'

# Start the Flask web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
