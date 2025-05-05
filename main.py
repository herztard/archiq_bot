import logging
import os

import requests
from dotenv import load_dotenv
from icecream import ic
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import telegram.ext.filters as filters
from telegram.constants import ParseMode

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, готов принимать сообщения.')

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    user_first_name = update.message.from_user.first_name
    user_last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    user_telegram_id = update.message.from_user.id

    created_at = update.message.date
    chat_id = update.message.chat_id

    ic(update, context)
    logger.info(f"Получено сообщение от {user_first_name} {user_last_name}: {user_message}")

    stop_typing = asyncio.Event()

    async def send_typing_action():
        try:
            while not stop_typing.is_set():
                await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
                await asyncio.sleep(3)
        except Exception as e:
            logger.error(f"Ошибка в отправке статуса typing: {e}")

    typing_task = asyncio.create_task(send_typing_action())

    try:
        params = {
            "query": user_message,
            "user_details": {
                "first_name": user_first_name,
                "last_name": user_last_name,
                "username": username,
                "user_telegram_id": user_telegram_id,
            },
            "message_details": {
                "chat_id": chat_id,
                "created_at": created_at.isoformat(),
            }
        }
        response = requests.post(f"{API_BASE_URL}", json=params)
        response.raise_for_status()
        result = response.json()
        result_text = result.get("result")
        ic(response)
    except Exception as e:
        logger.error(f"Ошибка при запросе к API: {e}")
        result_text = "Ошибка при выполнении запроса к API."
    finally:
        stop_typing.set()
        await typing_task


    await update.message.reply_text(result_text, parse_mode=ParseMode.MARKDOWN)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))

    logger.info("Бот запущен и готов к работе!")
    await app.run_polling(close_loop=False)

if __name__ == '__main__':
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()
    asyncio.run(main())
