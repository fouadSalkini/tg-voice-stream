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
# 86 done https://www.youtube.com/watch?v=KsG5KtGSZm8&list=PLr7X7rIaev6LAsGDoVZrDBTWmyXeD0L7h
# 23 https://www.youtube.com/playlist?list=PLWA9mQ1O5nGWrtDqAsdRT2ObEZ7xmOucd
# https://www.youtube.com/playlist?list=PLGbzILZDD0i9eFWuQ3JO1y_pwMYqDBsRY
# https://www.youtube.com/playlist?list=PLGbzILZDD0i-FvgUWhs73CG7dUrphqfVF
# https://www.youtube.com/watch?v=e-9dVwLWiAo&list=PLGbzILZDD0i-92GW5L8HKRu2Owdjw6n1L
# https://www.youtube.com/playlist?list=PLYhaCT6xCcqkRESabizGrRnUJCJEorsXx

# yt-dlp --cookies ../youtube.com_cookies.txt -f bestaudio --extract-audio --audio-format opus --audio-quality 64K -o "%(title)s.%(ext)s" "URL"
# --playlist-items 1,2,3,...
# --no-warnings "VIDEO_URL" > /dev/null 2>&1
# -q (for less output)
# yt-dlp --cookies youtube.com_cookies.txt --limit-rate 500K --sleep-interval 10 --max-sleep-interval 20 -f  bestaudio --extract-audio --audio-format opus --audio-quality 64K --no-warnings -o "downloads2/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLWA9mQ1O5nGWrtDqAsdRT2ObEZ7xmOucd"

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
