import yt_dlp
from config import Config

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'
authconfig = {
            # "username": Config.YT_USERNAME,
            # "password": Config.YT_PASSWORD,
            "cookies": Config.YT_COOKIEFILE,
            "user_agent": Config.YT_USERAGENT
        }
ydl_opts = {
    'format': 'bestaudio',
    "outtmpl": "downloads/%(id)s.%(ext)s"
}
ydl_opts.update(authconfig)


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
