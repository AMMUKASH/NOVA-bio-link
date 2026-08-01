import os
from pyrogram.types import ChatPermissions
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
LOG_GROUP = int(os.getenv("LOG_GROUP"))
PORT = int(os.getenv("PORT", 8080))
START_IMG = os.getenv("START_IMG")
BOT_USERNAME = os.getenv("BOT_USERNAME")
UPDATE_CH = os.getenv("UPDATE_CH")
SUPPORT_CH = os.getenv("SUPPORT_CH")
OWNER_ID = int(os.getenv("OWNER_ID"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME")

RESTRICTED_PERMISSIONS = ChatPermissions(can_send_messages=False)
FULL_PERMISSIONS = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
)
