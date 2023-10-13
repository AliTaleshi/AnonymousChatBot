import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = os.environ.get('ANONYMOUS_CHAT_BOT_TOKEN')
BOT_USERNAME: Final = '@AnonymousChat0_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")
