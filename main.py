from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

app = Flask(__name__)

# Replace 'your_bot_token_here' with your actual bot token
TOKEN = 'your_bot_token_here'

# Function to calculate the parity of a number
def calculate_parity(number):
    return "Red" if number % 2 == 0 else "Green"

# Command handler for /predict command
def predict(update: Update, context: CallbackContext) -> None:
    try:
        # Extract the number from the user's message
        current_number = int(request.args.get('text'))

        # Predict the color for the next number
        next_color = calculate_parity(current_number + 1)

        # Reply with the prediction
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"For the current number {current_number}, the predicted color is {next_color}.")
    except (ValueError, TypeError):
        # Handle invalid input
        context.bot.send_message(chat_id=update.message.chat_id, text="Please provide a valid number after /predict.")

# Endpoint for receiving updates from Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return 'ok'

if __name__ == '__main__':
    # Set up the bot
    bot = Updater(TOKEN, use_context=True)
    dp = bot.dispatcher

    # Register /predict command handler
    dp.add_handler(CommandHandler("predict", predict))

    # Start the Flask web server
    app.run(host='0.0.0.0', port=8080)
    
