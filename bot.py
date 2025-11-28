from telegram.ext import Application, CommandHandler
TOKEN = "8577813513:AAGQVgFm45nBLog6ZIK6Ui7fU8dqCiwGpxE"
proxy =


async def start(update, context):
    await update.message.reply_text("سلام ! ربات روشن شد ")
async def help_command(update, context):
    await update.message.reply_text(
        "راهنما:\n"
        "/start - شروع ربات \n"
        "help - راهنمای دستورات \n"
        "هرچی بنویسی تکرار میکنم !"
    ) 
App= Application.builder().token(TOKEN).build()

App.add_handler(CommandHandler("start" , start))
App.add_handler(CommandHandler("help",help_command))

App.run_polling()