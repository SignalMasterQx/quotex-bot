import os
import telebot
from flask import Flask, request

# আপনার আসল তথ্য দিয়ে কোডটি রেডি করা হলো
BOT_TOKEN = "9231537358:AAHZDvb76MY-MC710_67dnX3Tfz"
CHANNEL_ID = "-1004299201984"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Quotex Signal Bot is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.data.decode('utf-8')
        if data:
            # সরাসরি আপনার নতুন চ্যানেলে সিগনাল পাঠাবে
            bot.send_message(chat_id=CHANNEL_ID, text=f"📊 **NEW SIGNAL**\n\n{data}")
            return "Signal Sent", 200
    except Exception as e:
        print(f"Error: {e}")
        return "Error", 500
    return "No Data", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
