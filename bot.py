import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك يا عبدالرحمن، البوت يعمل بنجاح تام!")

if __name__ == '__main__':
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()
    
