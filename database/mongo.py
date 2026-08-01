from pymongo import MongoClient
from config.config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
db = mongo_client["NovaDB"]

warns_col = db["user_warns"]
users_col = db["registered_users"]
groups_col = db["registered_groups"]
settings_col = db["group_settings"]
whitelist_col = db["whitelisted_users"]
