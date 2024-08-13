from Music.core.clients import hellbot
from config import Config

hellbot.app.send_message(
                int(Config.LOGGER_ID),
                "hello"
            )