from pyrogram.types import Message
from config.config import OWNER_ID
from main import bot

async def is_user_admin(message: Message) -> bool:
    if message.sender_chat and message.sender_chat.id == message.chat.id:
        return True
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return False
    if str(user_id) == str(OWNER_ID):
        return True
    try:
        member = await bot.get_chat_member(message.chat.id, user_id)
        return member.status in ["administrator", "creator"]
    except:
        return False

async def get_target_user(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            return await client.get_users(message.command[1])
        except:
            return None
    return None
