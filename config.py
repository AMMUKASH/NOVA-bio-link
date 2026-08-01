API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
MONGO_URL = "mongodb://localhost:27017"
LOG_GROUP = -100123456789
PORT = 8080
START_IMG = "https://example.com/start.jpg"
BOT_USERNAME = "NovaBot"
UPDATE_CH = "NovaUpdates"
SUPPORT_CH = "NovaSupport"
OWNER_ID = 123456789
OWNER_USERNAME = "NovaOwner"

from pyrogram.types import ChatPermissions
RESTRICTED_PERMISSIONS = ChatPermissions(can_send_messages=False)
FULL_PERMISSIONS = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
)
