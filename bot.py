
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from motor.motor_asyncio import AsyncIOMotorClient

# Logging setup
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# Environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB setup
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client.telegram_bot
users_collection = db.users

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the File Renamer Bot!\n\n"
        "Commands:\n"
        "/setsource [channel_id] - Set the source channel.\n"
        "/setoutput [channel_id] - Set the output channel.\n"
        "/setformat [format] - Set the file renaming format.\n"
        "/setthumbnail - Upload a custom thumbnail.\n"
        "/status - Check the current task status.\n"
        "/start - Display this help message."
    )

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
