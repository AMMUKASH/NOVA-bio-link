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

    # ✅ Corrected line
    if URL_PATTERN.search(text_content):
        has_link = True

    if has_link:
        settings = get_group_settings(chat_id)
        action = settings.get("action", "all")

        if action == "warn":
            warns_col.update_one({"chat_id": chat_id, "user_id": user.id}, {"$inc": {"warns": 1}}, upsert=True)
            await message.reply_text("⚠️ Link detected! You have been warned.")
            await auto_delete_msg(message)

        elif action == "mute":
            await client.restrict_chat_member(chat_id, user.id, RESTRICTED_PERMISSIONS)
            await message.reply_text("🔇 Link detected! User muted.")
            await auto_delete_msg(message)

        elif action == "ban":
            await client.ban_chat_member(chat_id, user.id)
            await message.reply_text("🚫 Link detected! User banned.")
            await auto_delete_msg(message)

        elif action == "all":
            warns_col.update_one({"chat_id": chat_id, "user_id": user.id}, {"$inc": {"warns": 1}}, upsert=True)
            await client.restrict_chat_member(chat_id, user.id, RESTRICTED_PERMISSIONS)
            await message.reply_text("⚠️ Link detected! Warn + Mute applied.")
            await auto_delete_msg(message)
