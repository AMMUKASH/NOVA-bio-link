import os
from pyrogram.types import ChatPermissions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID", 38138069))
API_HASH = os.getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8707537667:AAHJAu79qPHuvhp_Em60VDOB-2kjJDkCHJY")
BOT_USERNAME = os.getenv("BOT_USERNAME", "BioCleanX_bot")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = int(os.getenv("LOG_GROUP", -1003960961858))

OWNER_ID = int(os.getenv("OWNER_ID", 8724182918))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "CoderNova")

UPDATE_CH = os.getenv("UPDATE_CH", "https://t.me/NovaBot_Support")
SUPPORT_CH = os.getenv("SUPPORT_CH", "https://t.me/+BTg9b8Xw9lhkMWUx")

START_IMG = os.getenv("START_IMG", "https://graph.org/vTelegraphBot-08-01-80")

PORT = int(os.getenv("PORT", 8080))

# Permissions
RESTRICTED_PERMISSIONS = ChatPermissions(can_send_messages=False)

FULL_PERMISSIONS = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
)
