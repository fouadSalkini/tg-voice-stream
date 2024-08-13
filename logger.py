from Music.core.clients import hellbot
from config import Config
from pyrogram import Client


async def start():
    await hellbot.start()
    await hellbot.app.send_message(
                    int(Config.LOGGER_ID),
                    "hello"
                )

Client.restart()
hellbot.run(start())