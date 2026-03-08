import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from handlers import admin_commands, moderation, ai_handler
from utils.memory import load_memory

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Загружаем память при старте
    load_memory()
    
    # Initialize bot with default parse mode
    bot = Bot(
        token=BOT_TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Register routers in correct order
    # Admin commands (бан/мют) should be first
    dp.include_router(admin_commands.router)
    # Moderation (links/bad words) second
    dp.include_router(moderation.router)
    # AI Communication last (handles general text)
    dp.include_router(ai_handler.router)

    logging.info("Бот Шота запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")
