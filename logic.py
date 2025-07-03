from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters

career_questions = [
    "Ты предпочитаешь работу с людьми или с компьютерами?",
    "Тебе нравится решать логические задачи или придумывать новые идеи?",
    "Ты хотел(а) бы работать в офисе или на свежем воздухе?"
]

career_suggestions = {
    ("c людьми", "придумывать новые идеи", "в офисе"): "Маркетолог 🎯",
    ("c компьютерами", "логические задачи", "в офисе"): "Программист 👨‍💻",
    ("c людьми", "логические задачи", "на свежем воздухе"): "Инженер-строитель 🏗️",
    ("c компьютерами", "придумывать новые идеи", "на свежем воздухе"): "Дизайнер интерьеров 🖌️"

}

user_answers = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_answers[user_id] = []
    await update.message.reply_text("Привет! Я помогу тебе с выбором профессии.")
    await update.message.reply_text(career_questions[0])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    text = update.message.text.lower()
    
    if user_id not in user_answers:
        user_answers[user_id] = []

    user_answers[user_id].append(text)

    if len(user_answers[user_id]) < len(career_questions):
        next_question = career_questions[len(user_answers[user_id])]
        await update.message.reply_text(next_question)
    else:
        key = tuple(user_answers[user_id])
        suggestion = career_suggestions.get(key, 'У тебя индивидуальный выбор!')
        await update.message.reply_text(f"На основе твоих ответов я думаю, тебе подойдет профессия: {suggestion}")
        user_answers.pop(user_id)

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))