import requests
from requests_oauthlib import OAuth2Session


client_id = r'ClientID' #Google MB API client ID
client_secret = r'ClientSecret' #Google MB secrete
redirect_url = 'http://ddsview.com/GMB/MyBusiness' #Redirect URL
redirect_local = 'localhost:8080'
scope_url = ['https://www.googleapis.com/auth/plus.business.manage', '']

oauth = OAuth2Session(client_id, redirect_uri=redirect_local, scope=scope_url) #Declare Authorization object

authorization_url, state = oauth.authorization_url('https://accounts.google.com/o/oauth2/auth', access_type="offline", approval_prompt="force") #Pull the authorization URL to allow for OAuth2 authentication

print('Please go to %s and authorize access.' %authorization_url)
authorization_response = raw_input('Enter the full callback URL')


token = oauth.fetch_token('https://accounts.google.com/o/oauth2/token', authorization_response=authorization_response, client_secret=client_secret)

r = oauth.get('https://mybusiness.googleapis.com/v3/accounts/AccountID/locations') #Submit get request using token just fetched
print(r.text)
#Request URL: https://mybusiness.googleapis.com/v3/accounts
