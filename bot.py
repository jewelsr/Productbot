
import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Replace this with your bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)

# Setup Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Replace with your actual Google Sheet name
sheet = client.open("Your Sheet Name").sheet1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! আপনি অর্ডার দিতে চাইলে /order লিখুন।")

@bot.message_handler(commands=['order'])
def order_product(message):
    user = message.from_user.first_name
    user_id = message.from_user.id
    sheet.append_row([str(user), str(user_id), "Order Placed"])
    bot.reply_to(message, "আপনার অর্ডার গ্রহণ করা হয়েছে।")

bot.polling()
