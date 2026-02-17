import telebot
import requests

# Replace these with your own values
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Web Integration URL
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Bot! I'm here to help you track your receipts.")

@bot.message_handler(commands=['track'])
def track_receipt(message):
    bot.reply_to(message, "Please send me the receipt details.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Here you would normally process the receipt
    # For now, we'll just acknowledge receipt
    bot.reply_to(message, "Receipt received! I'll track this for you.")
    # Optionally, send data to the web integration URL
    send_to_web_integration(message.text)

def send_to_web_integration(data):
    response = requests.post(WEBHOOK_URL, json={'receipt_data': data})
    if response.status_code == 200:
        print('Data sent to web integration successfully.')
    else:
        print('Failed to send data to web integration.')

if __name__ == '__main__':
    bot.polling()