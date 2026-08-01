import asyncio
import datetime
import re
from pyrogram import filters
from pyrogram.types import Message
from main import bot
from database.mongo import warns_col, groups_col, settings_col
from utils.permissions import is_user_admin
from config.config import RESTRICTED_PERMISSIONS
from utils.helpers import auto_delete_msg

URL_PATTERN = re.compile(r'(https?://[^\s]+|t\.me/[^\s]+|@\w+\.\w+|www\.[^\s]+)')
BIO_CACHE = {}

def get_group_settings(chat_id):
    settings = settings_col.find_one({"chat_id": chat_id})
    if not settings:
        default = {"chat_id": chat_id, "action": "all"} 
        settings_col.insert_one(default)
        return default
    return settings

@bot.on_message(filters.group & ~filters.service)
async def group_security_scanner(client, message: Message):
    chat_id = message.chat.id
    user = message.from_user

    groups_col.update_one({"chat_id": chat_id}, {"$set": {"chat_id": chat_id}}, upsert=True)

    if await is_user_admin(message):
        return
    if not user:
        return

    has_link = False
    text_content = message.text or message.caption or ""

    if URL_PATTERN.search(text
