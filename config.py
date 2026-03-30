# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7986732741:AAHl9AStZgcF5Wu1CBHYTfpaIA4HsEimCIc")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003703174588")) #Your db channel Id
OWNER = os.environ.get("OWNER", "itsuhito") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "19467056")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/itsuhito")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "gplinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "f98a359c682f52fb3705f15909a4253392e11ea2")
TUT_VID = os.environ.get("TUT_VID","https://t.me/kazukailinks")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>This is a file link bot for @kazukai\n\n❏ Bot Commands\n├ /start : Start the bot\n├ /about : View bot information\n└ /help : Get help related to the bot\n\nSimply click on the link, start the bot, join the required channels, and try again.\n\nDeveloped by <a href=https://t.me/itsuhito>itsuhito</a></blockquote></b>"

ABOUT_TXT = "<b><blockquote>◈ Owner: <a href=https://t.me/itsuhito>itsuhito</a>\n◈ Developer: <a href=https://t.me/itsuhito>itsuhito</a></blockquote></b>"

#--------------------------------------------
#--------------------------------------------

START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention}\n\n<blockquote>I am a file store bot. I can store private files in a specified channel, and other users can access them using a special link.</blockquote></b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b><blockquote>Please join our channels first, then click on the reload button to access your requested file.</blockquote></b>")

CMD_TXT = """<blockquote><b>» 𝘈𝘋𝘔𝘐𝘕 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚:</b></blockquote>

<b>›› /dlt_time :</b> 𝘚𝘦𝘵 𝘢𝘶𝘵𝘰 𝘥𝘦𝘭𝘦𝘵𝘦 𝘵𝘪𝘮𝘦
<b>›› /check_dlt_time :</b> 𝘊𝘩𝘦𝘤𝘬 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘥𝘦𝘭𝘦𝘵𝘦 𝘵𝘪𝘮𝘦
<b>›› /dbroadcast :</b> 𝘉𝘳𝘰𝘢𝘥𝘤𝘢𝘴𝘵 𝘥𝘰𝘤𝘶𝘮𝘦𝘯𝘵 / 𝘷𝘪𝘥𝘦𝘰
<b>›› /ban :</b> 𝘉𝘢𝘯 𝘢 𝘶𝘴𝘦𝘳
<b>›› /unban :</b> 𝘜𝘯𝘣𝘢𝘯 𝘢 𝘶𝘴𝘦𝘳
<b>›› /banlist :</b> 𝘎𝘦𝘵 𝘭𝘪𝘴𝘵 𝘰𝘧 𝘣𝘢𝘯𝘯𝘦𝘥 𝘶𝘴𝘦𝘳𝘴
<b>›› /addchnl :</b> 𝘈𝘥𝘥 𝘧𝘰𝘳𝘤𝘦 𝘴𝘶𝘣 𝘤𝘩𝘢𝘯𝘯𝘦𝘭
<b>›› /delchnl :</b> 𝘙𝘦𝘮𝘰𝘷𝘦 𝘧𝘰𝘳𝘤𝘦 𝘴𝘶𝘣 𝘤𝘩𝘢𝘯𝘯𝘦𝘭
<b>›› /listchnl :</b> 𝘝𝘪𝘦𝘸 𝘢𝘥𝘥𝘦𝘥 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴
<b>›› /fsub_mode :</b> 𝘛𝘰𝘨𝘨𝘭𝘦 𝘧𝘰𝘳𝘤𝘦 𝘴𝘶𝘣 𝘮𝘰𝘥𝘦
<b>›› /pbroadcast :</b> 𝘚𝘦𝘯𝘥 𝘱𝘩𝘰𝘵𝘰 𝘵𝘰 𝘢𝘭𝘭 𝘶𝘴𝘦𝘳𝘴
<b>›› /add_admin :</b> 𝘈𝘥𝘥 𝘢𝘯 𝘢𝘥𝘮𝘪𝘯
<b>›› /deladmin :</b> 𝘙𝘦𝘮𝘰𝘷𝘦 𝘢𝘯 𝘢𝘥𝘮𝘪𝘯
<b>›› /admins :</b> 𝘎𝘦𝘵 𝘭𝘪𝘴𝘵 𝘰𝘧 𝘢𝘥𝘮𝘪𝘯𝘴
<b>›› /addpremium :</b> 𝘈𝘥𝘥 𝘢 𝘱𝘳𝘦𝘮𝘪𝘶𝘮 𝘶𝘴𝘦𝘳
<b>›› /premium_users :</b> 𝘓𝘪𝘴𝘵 𝘢𝘭𝘭 𝘱𝘳𝘦𝘮𝘪𝘶𝘮 𝘶𝘴𝘦𝘳𝘴
<b>›› /remove_premium :</b> 𝘙𝘦𝘮𝘰𝘷𝘦 𝘱𝘳𝘦𝘮𝘪𝘶𝘮 𝘧𝘳𝘰𝘮 𝘢 𝘶𝘴𝘦𝘳
<b>›› /myplan :</b> 𝘊𝘩𝘦𝘤𝘬 𝘺𝘰𝘶𝘳 𝘱𝘳𝘦𝘮𝘪𝘶𝘮 𝘴𝘵𝘢𝘵𝘶𝘴
<b>›› /count :</b> 𝘊𝘰𝘶𝘯𝘵 𝘷𝘦𝘳𝘪𝘧𝘪𝘤𝘢𝘵𝘪𝘰𝘯𝘴
<b>›› /delreq :</b> 𝘙𝘦𝘮𝘰𝘷𝘦 𝘭𝘦𝘧𝘵𝘰𝘷𝘦𝘳 𝘯𝘰𝘯-𝘳𝘦𝘲𝘶𝘦𝘴𝘵 𝘶𝘴𝘦𝘳𝘴
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>✦ 𝘣𝘺 @kazukai</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "YOU ARE NOT AN ADMIN!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "itsuhito")
UPI_ID = os.environ.get("UPI_ID", "rohit23pnb@axl")
QR_PIC = os.environ.get("QR_PIC", "https://telegra.ph/file/3e83c69804826b3cba066-16cffa90cd682570da.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/itsuhito")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")

#===================(END)========================#

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
   
