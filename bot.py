import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text('السيرفر يعمل 24/7')

async def echo(update: Update, context):
    await update.message.reply_text(f'تم استلام نصك: {update.message.text}')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("البوت يعمل على السيرفر...")
    app.run_polling()
    
