from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CH, SUPPORT_CH

MAIN_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("🤖 Add Me To Your Group 🤖", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME}"),
     InlineKeyboardButton("⚙️ Help & Commands", callback_data="help_menu")],
    [InlineKeyboardButton("🔕 Update", url=f"https://t.me/{UPDATE_CH}"),
     InlineKeyboardButton("💌 Support", url=f"https://t.me/{SUPPORT_CH}")]
])

ALERT_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Add Me To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("📢 Update", url=f"https://t.me/{UPDATE_CH}"),
     InlineKeyboardButton("💌 Support", url=f"https://t.me/{SUPPORT_CH}")]
])

HELP_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("👥 General", callback_data="help_general")],
    [InlineKeyboardButton("🛡️ Moderation", callback_data="help_moderation")],
    [InlineKeyboardButton("👑 Owner", callback_data="help_owner")],
    [InlineKeyboardButton("⬅️ Back", callback_data="help_back")]
])
