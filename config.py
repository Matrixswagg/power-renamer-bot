import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "6061220802:AAG6yfIJDN2qXure7NGG0YedNfuYCiq6qTo")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", "12859216"))
API_HASH = os.environ.get("API_HASH", "6061220802:AAG6yfIJDN2qXure7NGG0YedNfuYCiq6qTo")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5821611295').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "autofilter")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "mongodb+srv://autofilter:autofilter@cluster0.yreiwux.mongodb.net/?retryWrites=true&w=majority")

START_PIC = (os.environ.get("START_PIC", "")).split()

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "")

FLOOD = int(os.environ.get("FLOOD", "5"))
