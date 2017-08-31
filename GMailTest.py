import requests
from requests_oauthlib import OAuth2Session


client_id = r'' #Google MB API client ID
client_secret = r'' #Google MB secrete
redirect_local = 'localhost:8080'
redirect_url = '' #Redirect URL

scope = ['https://www.googleapis.com/auth/userinfo.email',
		'https://www.googleapis.com/auth/userinfo.profile']

oauth = OAuth2Session (client_id, redirect_uri=redirect_url, scope=scope)

authorization_url, state = oauth.authorization_url(
	'https://accounts.google.com/o/oauth2/auth',
	access_type="offline", approval_prompt="force")

print ('Please go to %s and authorize access.' %authorization_url)
authorization_response = raw_input('Enter the full callback URL')