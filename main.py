import asyncio
from aiohttp import web
from pyrogram import Client, idle

from config.config import API_ID, API_HASH, BOT_TOKEN, PORT

bot = Client("NovaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Import handlers so they register
import handlers.start
import handlers.security
# agar aur handlers hain to unko bhi yahan import karo

app = web.Application()

async def run_web():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

async def main():
    asyncio.create_task(run_web())
    await bot.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
