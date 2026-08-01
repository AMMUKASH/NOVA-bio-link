import asyncio
from aiohttp import web
from pyrogram import Client
from config.config import API_ID, API_HASH, BOT_TOKEN, PORT

bot = Client("NovaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers
import handlers.start
import handlers.help
import handlers.stats
import handlers.moderation
import handlers.owner
import handlers.security

# Health check route
async def handle(request):
    return web.Response(text="✅ NovaBot Engine Active")

def run_web():
    app = web.Application()
    app.router.add_get("/", handle)
    web.run_app(app, port=PORT)

async def main():
    await bot.start()
    print("NovaBot started successfully!")
    run_web()

if __name__ == "__main__":
    asyncio.run(main())
