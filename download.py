import yt_dlp

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'
ydl_opts = {
    'format': 'best',
    "outtmpl": "downloads/%(id)s.%(ext)s",
    'username': 'fouadsa91@gmail.com',
    'password': 'Fouad.salkini@91',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'cookiefile': 'youtube.com_cookies.txt',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
