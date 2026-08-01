from pyrogram import filters
from pyrogram.types import Message
from main import bot
from database.mongo import whitelist_col
from utils.permissions import is_user_admin, get_target_user
from config.config import RESTRICTED_PERMISSIONS, FULL_PERMISSIONS
import datetime

# /whitelist
@bot.on_message(filters.command("whitelist") & filters.group)
async def whitelist_add(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    whitelist_col.update_one(
        {"chat_id": message.chat.id, "user_id": target.id},
        {"$set": {"chat_id": message.chat.id, "user_id": target.id, "username": target.username}},
        upsert=True
    )
    await message.reply_text(f"✅ {target.mention} is now Whitelisted!")

# /unwhitelist
@bot.on_message(filters.command("unwhitelist") & filters.group)
async def whitelist_remove(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    whitelist_col.delete_one({"chat_id": message.chat.id, "user_id": target.id})
    await message.reply_text(f"🚫 {target.mention} removed from Whitelist!")

# /mute
@bot.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    await bot.restrict_chat_member(message.chat.id, target.id, RESTRICTED_PERMISSIONS)
    await message.reply_text(f"🔇 {target.mention} has been muted.")

# /unmute
@bot.on_message(filters.command("unmute") & filters.group)
async def unmute_user(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    await bot.restrict_chat_member(message.chat.id, target.id, FULL_PERMISSIONS)
    await message.reply_text(f"🔊 {target.mention} has been unmuted.")

# /ban
@bot.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    await bot.ban_chat_member(message.chat.id, target.id)
    await message.reply_text(f"🚫 {target.mention} has been banned.")

# /unban
@bot.on_message(filters.command("unban") & filters.group)
async def unban_user(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    await bot.unban_chat_member(message.chat.id, target.id)
    await message.reply_text(f"✅ {target.mention} has been unbanned.")

# /tmute
@bot.on_message(filters.command("tmute") & filters.group)
async def temp_mute(client, message: Message):
    if not await is_user_admin(message):
        return await message.reply_text("❌ You are not an Admin!")
    if len(message.command) < 2:
        return await message.reply_text("Usage: /tmute 10m or /tmute @username 2h")
    target = await get_target_user(client, message)
    if not target:
        return await message.reply_text("❌ No target user found!")
    time_str = message.command[-1]
    try:
        value = int(time_str[:-1])
        unit = time_str[-1]
    except:
        return await message.reply_text("❌ Wrong format! Use 10m/2h/1d")
    if unit == 'm': duration = datetime.timedelta(minutes=value)
    elif unit == 'h': duration = datetime.timedelta(hours=value)
    elif unit == 'd': duration = datetime.timedelta(days=value)
    else: return await message.reply_text("❌ Wrong format! Use 10m/2h/1d")
    until_date = datetime.datetime.now(datetime.timezone.utc) + duration
    await bot.restrict_chat_member(message.chat.id, target.id, RESTRICTED_PERMISSIONS, until_date=until_date)
    await message.reply_text(f"⏳ {target.mention} muted for {time_str}.")
