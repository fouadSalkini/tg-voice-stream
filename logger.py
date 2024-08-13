from Music.core.clients import hellbot
from config import Config


async def start():
    await hellbot.start()
    await hellbot.app.send_message(
                    int(Config.LOGGER_ID),
                    "hello"
                )

hellbot.run(start())