from pyrogram import Client
from config import Config

from pyrogram.types import (
                    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)


# Replace with your API ID, API Hash, and session name
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
session_string = None #Config.HELLBOT_SESSION
session_name = Config.MUSIC_SESSION

print(Config.MUSIC_SESSION)
# Initialize the client
app = Client(
    name=Config.MUSIC_SESSION,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    #plugins=dict(root="Music.plugins"),
    #workers=100,
    )

id = -1002173254098 
print(id)

# Start the client
with app:
    app.send_message(
        id, 
        "Hello, this is a message from Pyrogram reply markup!",
        disable_notification=True,
        disable_web_page_preview=True,
        protect_content=True,
        reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Data", callback_data="callback_data")],
                            [InlineKeyboardButton("Docs", url="https://docs.pyrogram.org")]
                        ])
        )
    
    
    