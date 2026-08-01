from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
from main import bot
from utils.buttons import HELP_BUTTONS

HELP_TXT = "⚙️ **Help & Guide Menu** ⚙️\n\nChoose a category below to see commands and usage."

@bot.on_message(filters.command("help"))
async def help_cmd(client, message: Message):
    await message.reply_text(HELP_TXT, reply_markup=HELP_BUTTONS)

@bot.on_callback_query()
async def help_callback(client, query: CallbackQuery):
    data = query.data
    if data == "help_general":
        text = "👥 General Commands\n\n• /start → Show welcome\n• /help → Show help menu"
        await query.message.edit_text(text, reply_markup=HELP_BUTTONS)
    elif data == "help_moderation":
        text = "🛡️ Moderation Commands\n\n• /whitelist @user\n• /unwhitelist @user\n• /mute @user\n• /unmute @user\n• /ban @user\n• /unban @user\n• /tmute @user 10m"
        await query.message.edit_text(text, reply_markup=HELP_BUTTONS)
    elif data == "help_owner":
        text = "👑 Owner Commands\n\n• /stats\n• /broadcast\n• /backup"
        await query.message.edit_text(text, reply_markup=HELP_BUTTONS)
    elif data == "help_back":
        await query.message.edit_text(HELP_TXT, reply_markup=HELP_BUTTONS)
