import asyncio

from aiogram import Bot, Dispatcher

from handlers.user_handlers import router
from data.config import TOKEN_TG


async def start_tg() -> None:
    """Entry point"""
    while True:
        bot = Bot(TOKEN_TG)
        dp = Dispatcher()
        dp.include_router(router)
        try:
            await dp.start_polling(bot)
        except:
            await asyncio.sleep(10)


print("tg bot started")
if __name__ == '__main__':
    try:
        asyncio.run(start_tg())
    except Exception as _ex:
        print(_ex)