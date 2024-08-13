import yt_dlp
from config import Config

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'
authconfig = {
            "username": Config.YT_USERNAME,
            "password": Config.YT_PASSWORD,
            "cookies": Config.YT_COOKIEFILE,
            "user_agent": Config.YT_USERAGENT
        }
ydl_opts = {
    'format': 'best',
    "outtmpl": "downloads/%(id)s.%(ext)s"
}.update(authconfig)

merged = ydl_opts.copy()  # Make a copy of arr1
merged.update(authconfig) 

print(ydl_opts)
print(merged)

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])
