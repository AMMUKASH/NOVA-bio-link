# ⚡ NovaBot Security Engine ⚡

NovaBot is an advanced Telegram security bot that protects your groups from spam, unwanted links, and malicious users.  
It comes with **moderation tools, owner commands, and auto security scanning**.

---

## 🚀 Features
- Bio & Name Scanner
- Admin Bypass
- Whitelist System
- Auto Actions (Warn / Mute / Ban)
- Owner Commands (Stats, Broadcast, Backup)
- Interactive Help Menu

---

## 📂 Repo StructureNovaBot/ │── config/          → Bot settings & environment │── database/        → MongoDB connection │── handlers/        → Commands (start, help, moderation, owner, security) │── utils/           → Helpers, permissions, buttons │── main.py          → Entry point │── requirements.txt → Dependencies │── README.md        → Documentation │── .gitignore       → Ignore unnecessary files │── Dockerfile       → Containerized deployment │── render.yaml      → Render deployment config │── Procfile         → Heroku deployment config

---

## ⚙️ Setup

1. Clone repo:
   ```bash
   git clone https://github.com/yourusername/NovaBot.git
   cd NovaBotCreate virtual environment:bashCopypython -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # WindowsInstall dependencies:bashCopypip install -r requirements.txt

Configure .env file:envCopyAPI_ID=12345
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_URL=mongodb://localhost:27017
OWNER_ID=123456789Run bot:bashCopypython main.py☁️ Deployment Options🔥 HerokuAdd Procfile → worker: python main.pySet environment variables via heroku config:set⚡ Renderhttps://render.com/deployAdd render.yaml → Render auto builds worker serviceConfigure secrets in Render dashboard

VPSca://s?q=Deploy_NovaBot_on_VPSInstall Python + MongoDBRun docker-compose up -d (optional)Add cronjobs.sh in crontab for auto restart🛠️ Cronjobs Example (VPS)bashCopy0 0 * * * /path/to/cronjobs.sh📊 Owner Commands/stats → Show bot stats/broadcast → Broadcast message to all users/backup → Export MongoDB backup🛡️ Moderation Commands/whitelist @user → Whitelist user/unwhitelist @user → Remove from whitelist/mute @user → Mute user/unmute @user → Unmute user/ban @user → Ban user/unban @user → Unban user/tmute @user 10m → Temp mute

General Commands/start → Welcome caption + buttons/help → Interactive help menu
