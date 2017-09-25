import requests
import Connect


from oauth2client import client
import httplib2

CLIENT_ID=
CLIENT_SECRET=
SCOPE="https://www.googleapis.com/auth/plus.business.manage"

# credentials is the JSON credentials you obtain and saved previously

credentials = client.OAuth2Credentials.from_json(credentials)
if credentials.access_token_expired:
    # refresh it
    http = httplib2.Http()
    http = credentials.authorize(http)
    credentials.refresh(http)
    access_token = credentials.token_response["access_token"]
else:
    access_token = credentials.token_response["access_token"]