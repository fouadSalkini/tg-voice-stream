from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # youtube variables
    YT_USERNAME = getenv("YT_USERNAME", None)               
    YT_PASSWORD = getenv("YT_PASSWORD", None)               
    YT_COOKIEFILE = getenv("YT_COOKIEFILE", None)  
    YT_USERAGENT =  getenv("YT_USERAGENT", None)        

    # required config variables
    API_HASH = getenv("API_HASH", None)                # get from my.telegram.org
    API_ID = int(getenv("API_ID", 0))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", None)              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", None)        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", None)  # enter your session string here
    LOGGER_CHANNEL = int(getenv("LOGGER_CHANNEL", 0))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "")                  # enter your id here
    MUSIC_SESSION = getenv("MUSIC_SESSION", None)  # enter your session name here
    CLIENT_SESSION = getenv("CLIENT_SESSION", None)  # enter your session name here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/01/Telegram-920x518.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "VoiceStreamingBot")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/01/Telegram-920x518.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    SUPER_USERS = filters.user()
    PLAYER_CACHE = {}
    BTNS_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]