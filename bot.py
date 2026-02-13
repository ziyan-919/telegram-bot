from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8192710763:AAGSaqsmPBK9GIJSpD0jHqdAGposmD5lUf0"
SOURCE_CHAT_ID = -1002746643910
TARGET_CHAT_ID = -1003000120235

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text

        # 修改内容
        new_text = text.replace("@yangbenqiang", "@qiudaoyu11")

        await context.bot.send_message(chat_id=TARGET_CHAT_ID, text=new_text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
