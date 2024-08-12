import yt_dlp
from config import Config

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'
ydl_opts = {
    'format': 'best',
    "outtmpl": "downloads/%(id)s.%(ext)s",
    'username': Config.YT_USERNAME,
    'password': Config.YT_PASSWORD,
    'user_agent': Config.YT_USERAGENT,
    'cookies': Config.YT_COOKIEFILE,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
