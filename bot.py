from telegram.ext import Application, CommandHandler

TOKEN = "8577813513:AAGQVgFm45nBLog6ZIK6Ui7fU8dqCiwGpxE"

async def start(update, context):
    await update.message.reply_text("سلام! ربات روشن شد.")

async def help_command(update, context):
    await update.message.reply_text(
        "راهنما:\n"
        "/start - شروع ربات\n"
        "/help - راهنمای دستورات"
    )
async def love(updete, context):
    await updete.message.reply_text("عاشقتم سحر (:")
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("love",love))
    
    app.run_polling()

if __name__ == "__main__":
    main()
