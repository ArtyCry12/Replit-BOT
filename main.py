import telebot

# Initialize the bot with your token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Command to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Receipt Processing Bot!\nClick the button below to process your receipts.", reply_markup=get_keyboard())

# Function to create a keyboard with a web link button
def get_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    button = telebot.types.InlineKeyboardButton(text="Process Receipts", url="https://example.com/process")
    keyboard.add(button)
    return keyboard

# Run the bot
if __name__ == '__main__':
    bot.polling(none_stop=True)