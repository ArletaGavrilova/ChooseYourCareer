from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import *
from telegram.ext import ApplicationBuilder
from logic import setup_handlers

def main():
    app = ApplicationBuilder().token("7537587684:AAHKZF8vtO5-TsAmgp_BMiBIoLU-GxsCsSo").build()
    setup_handlers(app)
    app.run_polling()

if __name__ == '__main__':
    main()
