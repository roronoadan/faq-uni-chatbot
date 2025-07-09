from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import csv

def load_faq_from_csv(filename="faq_data.csv"):
    faq = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = row["question"].strip().lower()
            answer = row["answer"].strip()
            faq[question] = answer
    return faq

faq_data = load_faq_from_csv()


def get_answer(user_input: str) -> str:
    user_input = user_input.lower().strip()
    for question, answer in faq_data.items():
        if question in user_input:
            return answer
    return "🤖 Sorry, I don't know that yet. Try asking something else!"

from telegram import ReplyKeyboardMarkup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["How do I register for classes", "What are the admission dates"],
        ["Where is the university located", "How to contact administration"],
        ["What is the grading system"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome! I’m your university assistant. Tap a question below or ask anything.",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    answer = get_answer(user_input)
    await update.message.reply_text(answer)

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(telegram_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running... (no AI)")
    app.run_polling()
