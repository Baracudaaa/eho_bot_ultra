import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config

async def main() -> None:

    # Загружаем конфиг в переменную конфиг
    config: Config = load_config()
    # Задаем базовую конфигурацию логирования
    logging.basicConfig(
        level=logging.getLevelName(config.log.level),
        format=config.log.format
    )

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())