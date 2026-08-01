from pyrogram import filters
from pyrogram.types import Message
from main import bot
from utils.buttons import MAIN_BUTTONS
from config.config import START_IMG

START_TXT = """
⚡ **NovaBot Security Engine** ⚡

👋 Hello {mention} !
I am an advanced security bot that keeps your groups safe from spammers and unwanted links.
"""

@bot.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    user = message.from_user
    mention_str = user.mention if user else "User"
    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=START_TXT.format(mention=mention_str),
            reply_markup=MAIN_BUTTONS
        )
    except:
        await message.reply_text(
            text=START_TXT.format(mention=mention_str),
            reply_markup=MAIN_BUTTONS,
            disable_web_page_preview=True
        )
