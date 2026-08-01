import asyncio
import datetime
import json
import io
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from main import bot
from database.mongo import users_col, groups_col
from config.config import OWNER_ID

# /stats
@bot.on_message(filters.command("stats") & filters.private)
async def stats_cmd(client, message: Message):
    if str(message.from_user.id) != str(OWNER_ID):
        return
    total_users = users_col.count_documents({})
    total_groups = groups_col.count_documents({})
    seven_days_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
    recent_users = users_col.count_documents({"date": {"$gte": seven_days_ago}})
    stats_text = (
        f"📊 **REAL-TIME BOT STATS**\n"
        f"👥 Users: `{total_users}`\n"
        f"🏰 Groups: `{total_groups}`\n"
        f"🆕 New (7 days): `{recent_users}`\n"
    )
    await message.reply_text(stats_text)

# /broadcast
@bot.on_message(filters.command("broadcast") & filters.private)
async def broadcast_cmd(client, message: Message):
    if str(message.from_user.id) != str(OWNER_ID):
        return
    if not message.reply_to_message:
        return await message.reply_text("❌ Reply to a message to broadcast.")
    users = list(users_col.find({}))
    success, failed = 0, 0
    status_msg = await message.reply_text(f"📢 Broadcasting to `{len(users)}` users...")
    for u in users:
        if "user_id" in u:
            try:
                await message.reply_to_message.copy(u["user_id"])
                success += 1
                await asyncio.sleep(0.05)
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except:
                failed += 1
    await status_msg.edit_text(f"✅ Broadcast Done\n🎯 Success: {success}\n❌ Failed: {failed}")

# /backup
@bot.on_message(filters.command("backup") & filters.private)
async def backup_cmd(client, message: Message):
    if str(message.from_user.id) != str(OWNER_ID):
        return
    status = await message.reply_text("🎒 Creating Backup...")
    backup_data = {
        "users": list(users_col.find({}, {"_id": 0})),
        "groups": list(groups_col.find({}, {"_id": 0}))
    }
    file = io.BytesIO(json.dumps(backup_data, default=str).encode('utf-8'))
    file.name = "Database_Backup.json"
    await bot.send_document(chat_id=message.chat.id, document=file, caption="✅ Backup Exported Successfully")
    await status.delete()
