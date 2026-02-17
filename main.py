import os
from flask import Flask, request, send_from_directory
import telebot
import logging

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

app = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)

# Enable logging
d_logging = logging.getLogger('werkzeug')
d_logging.setLevel(logging.INFO)

# Track receipts
receipts = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Welcome to the Receipt Tracker! Use /track to start tracking your receipts.")

@bot.message_handler(commands=['track'])
def track_receipt(message):
    receipts.append(message.text)
    bot.reply_to(message, "Receipt tracked! Use /view to see all tracked receipts.")

@bot.message_handler(commands=['view'])
def view_receipts(message):
    if receipts:
        bot.reply_to(message, "Tracked Receipts:\n" + '\n'.join(receipts))
    else:
        bot.reply_to(message, "No receipts tracked yet!")

# Flask route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "", 200

# Setting webhook
def set_webhook():
    bot.remove_webhook()  # Remove old webhook
    bot.set_webhook(url=WEBHOOK_URL)

if __name__ == '__main__':
    set_webhook()
    app.run(host='0.0.0.0', port=8443)
