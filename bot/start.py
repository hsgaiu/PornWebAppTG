import asyncio
import logging
from aiogram import Bot, Dispatcher
from data.config import token

logging.basicConfig(level=logging.INFO, format='%(actime)s - %(levelname)s - %(message)s')

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    try: 
        await bot.delete_webhook()
        logging.info("Webhook | Deleted")

        await dp.start_polling(bot)
        logging.info("Polling | Started")
    except Exception as e:
        logging.error(f"Error | {e}")

    finally:
        await bot.session.close()
        logging.info("Bot | Closed")

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exiting...")