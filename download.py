import yt_dlp

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'
ydl_opts = {
    'format': 'best',
    "outtmpl": "downloads/%(id)s.%(ext)s",
    'username': 'fouadsa91@gmail.com',
    'password': 'Fouad.salkini@91',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
