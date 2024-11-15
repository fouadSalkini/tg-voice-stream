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


# Authenticate using Google API
credentials = Credentials.from_authorized_user_file(AUTHORIZED_USER_FILE)
print(credentials)


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
