import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '7533764228:AAEmGqM9W7WDuaakK2DXYxqH6mb7cHxCNYU'
bot = telebot.TeleBot(bot_token)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_info = get_user_info(message.from_user)
    bot.reply_to(message, user_info)

# Function to fetch user information
def get_user_info(user):
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name or "N/A"  # Use "N/A" if last name is not available
    username = user.username or "N/A"    # Use "N/A" if username is not available
    language_code = user.language_code or "N/A"

    # Create a message with all user information
    info = f"🔍 User Information:\n"
    info += f"👤 ID: {user_id}\n"
    info += f"📛 First Name: {first_name}\n"
    info += f"📛 Last Name: {last_name}\n"
    info += f"📜 Username: @{username}\n"
    info += f"🌐 Language Code: {language_code}\n"
    
    return info

# Start polling to keep the bot running
bot.polling()
