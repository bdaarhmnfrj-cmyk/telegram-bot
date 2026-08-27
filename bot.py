from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '8929194933:AAFTd1rauysGpWs7GLhMJkhM9JCq-0HxQw8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('أهلاً بك! أنا بوت حفظ الأكواد والمشاريع، أعمل الآن على السيرفر 24/7.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'تم استلام نصك:\n\n{update.message.text}')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    print("البوت يعمل على السيرفر...")
    app.run_polling()
  
