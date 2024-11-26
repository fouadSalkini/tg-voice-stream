import yt_dlp
from config import Config
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import json

id = "rCC70UbMuFY"
video_url = 'https://www.youtube.com/watch?v=rCC70UbMuFY'


# CLIENT_SECRETS_FILE='yt_client_secret_268203469430-le3hgnn3elv45kcu3iekj9nj7qctqbp9.apps.googleusercontent.com.json'


# # Define the required scopes (YouTube Data API v3 scopes)
# SCOPES = ['https://www.googleapis.com/auth/youtube']

# # Run the OAuth flow
# flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
# credentials = flow.run_local_server(port=8080)

# # Save the authorized user credentials to a file
# with open('authorized_user.json', 'w') as token_file:
#     token_file.write(credentials.to_json())

# print("Credentials saved to 'authorized_user.json'")

AUTHORIZED_USER_FILE = 'authorized_user.json'


# # Authenticate using Google API
# credentials = Credentials.from_authorized_user_file(AUTHORIZED_USER_FILE)
# print(credentials)

##############################
##############################
## youtube download command ##
##############################
##############################
## playlists: 
#1 86 [done] https://www.youtube.com/watch?v=KsG5KtGSZm8&list=PLr7X7rIaev6LAsGDoVZrDBTWmyXeD0L7h
#2 23 [done] https://www.youtube.com/playlist?list=PLWA9mQ1O5nGWrtDqAsdRT2ObEZ7xmOucd
#3 113 [done] https://www.youtube.com/playlist?list=PLGbzILZDD0i9eFWuQ3JO1y_pwMYqDBsRY
#4 165 [done] https://www.youtube.com/playlist?list=PLGbzILZDD0i-FvgUWhs73CG7dUrphqfVF
#5 700 https://www.youtube.com/watch?v=e-9dVwLWiAo&list=PLGbzILZDD0i-92GW5L8HKRu2Owdjw6n1L
#6 1282 https://www.youtube.com/playlist?list=PLYhaCT6xCcqkRESabizGrRnUJCJEorsXx
#7 10 [done] https://www.youtube.com/watch?v=AS-iUTQ_VqE&list=PLr7X7rIaev6IPBW6q9oPWAsOzAmqLPey_
#8 31 [done] https://www.youtube.com/watch?v=7yfZXDf7y9U&list=PLyKSKLsF2ArSP_JUyUlztenakNtVaj4Nz
#9 19 [done] https://www.youtube.com/watch?v=9tlzYANgbcQ&list=PLJdyh1foKTw02WimqlLja3YwWeqTuOepi
#10 11 [done] https://www.youtube.com/watch?v=IGlVZIxLGKE&list=PLcJLYVXnDZbPqsGSkILg4W0wv5gqvk2b9
#11 21 [done] https://www.youtube.com/watch?v=fZxVXXNycGk&list=PL9DwJ7DL3FOuAVRKYVw_6SMRiH3yEC7rz
#12 29 [done] https://www.youtube.com/watch?v=AoeVUPy5e6c&list=PL3lnNg8CXAt_iRC6hHz6ocgvUg4K3E3NA
#13 17 [done] https://www.youtube.com/watch?v=aBVEiiVU7tQ&list=PL3451BCE803EC9119
#14 43 [done] https://www.youtube.com/watch?v=BuTM5lIlBjw&list=PL3lnNg8CXAt9DvQtTHAE7YXg6JSle_gu9
#15 20 [done] https://www.youtube.com/playlist?list=PLQtPEQcFOMBax0xP7ZPYp8IkAmiTPw1WQ

# tar --remove-files --exclude=archive_600_700.tar.gz -czvf archive_600_700.tar.gz .

# yt-dlp --cookies youtube.com_cookies.txt --playlist-items 1 -f bestaudio --extract-audio --audio-format opus --audio-quality 64K -o "%(title)s.%(ext)s" "URL"
# --playlist-items 1,2,3,...
# --playlist-start 130 --playlist-end 600
# --no-warnings "VIDEO_URL" > /dev/null 2>&1
# -q (for less output)
# yt-dlp --cookies youtube.com_cookies.txt --limit-rate 2M --sleep-interval 10 --max-sleep-interval 20 -f  bestaudio --extract-audio --audio-format opus --audio-quality 64K -o "test/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLYhaCT6xCcqkRESabizGrRnUJCJEorsXx"

##############################
##############################
## youtube download command ##
##############################
##############################

authconfig = {
            # "username": Config.YT_USERNAME,
            # "password": Config.YT_PASSWORD,
            # "cookies": Config.YT_COOKIEFILE,
            "cookiefile": Config.YT_COOKIEFILE,
            # 'cookiefile': credentials.token_uri,  # Save token for reuse
            "user_agent": Config.YT_USERAGENT
        }
ydl_opts = {
    'format': 'bestaudio',
    "outtmpl": "downloads/%(id)s.%(ext)s"
}
ydl_opts.update(authconfig)


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
