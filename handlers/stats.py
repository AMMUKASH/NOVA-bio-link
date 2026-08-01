from pyrogram import filters
from pyrogram.types import Message
from main import bot
from database.mongo import users_col, groups_col
from config.config import OWNER_ID
import datetime

@bot.on_message(filters.command("stats") & filters.private)
async def stats_cmd(client, message: Message):
    if str(message.from_user.id) != str(OWNER_ID):
        return
    total_users = users_col.count_documents({})
    total_groups = groups_col.count_documents({})
    seven_days_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
    recent_users = users_col.count_documents({"date": {"$gte": seven_days_ago}})
    stats_text = f"📊 Stats\nUsers: {total_users}\nGroups: {total_groups}\nNew (7 days): {recent_users}"
    await message.reply_text(stats_text)
