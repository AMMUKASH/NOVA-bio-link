import asyncio
from aiohttp import web
from pyrogram import Client
from config.config import API_ID, API_HASH, BOT_TOKEN, PORT

bot = Client("NovaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers
import handlers.start
