import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5312976487:AAGDlqSROxTftUMQeJr5CJBIqacBLnQEL24")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "4247973"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "590d5655575ed171bb9c6cffbcf5fbb7")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001559016174"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1070126339"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://modtroda:eDb38lla2lq2jNc_S7x7WxZiNPtgR620@otto.db.elephantsql.com/modtroda")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001503257843"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {username}\n\n😄I can send Files to you 😄")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>🤖You need to join the Channel to use me🤖\n\n😸Please join Channel😸</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get('CUSTOM_CAPTION', '<b>@IVALDENA😍</b>\n<b>{previouscaption}</b>')

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>⚠️ Don't send me messages directly 🤬</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1070126339)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
