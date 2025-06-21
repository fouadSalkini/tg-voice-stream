from pyrogram import Client
from config import Config


app = Client(
    name=Config.CLIENT_SESSION,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.HELLBOT_SESSION,
    no_updates=True,
    )

with app:
    chat_id = 777000
    
    # Convert async generator to list
    messages = list(app.get_chat_history(chat_id, limit=3))
    
    for message in messages:
        print(f"[{message.date}] {message.from_user.first_name}: {message.text}")