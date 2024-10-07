from config import *
from pyrogram.client import Client

app = Client(
    "AniFrost",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=TOKEN
)
