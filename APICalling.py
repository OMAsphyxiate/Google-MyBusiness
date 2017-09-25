import sys, pyodbc, requests, os
import Connect #Import connection file
from FacebookInsights import Functions #Import Functions for creating file
from DatabaseSyncs import DBFunctions as dbf

#Generated Access Token for GMB
access_token = input('Enter access token: ')

FileName = 'GoogleReviews.txt'
FileLocation = Connect.GMBPath + FileName

try:
    os.remove(FileLocation) #Remove file if it already exists
except OSError:
    pass

CentralDatabase = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
    Connect.MSDriver,
    Connect.MSServer,
    Connect.MSDatabase,
    Connect.MSUID,
    Connect.MSPWD)) #Connect to Central Database

GMBCursor = CentralDatabase.cursor()
GoogleIDs = GMBCursor.execute('SELECT GoogleID FROM [Clinic].[Master] WHERE GoogleID IS NOT NULL ')

for item in GoogleIDs:
    dbf.GoogleList.extend(item)

for location in dbf.GoogleList:
    url = ("https://mybusiness.googleapis.com/v3/accounts/107604422420814997819/locations/%s/reviews?access_token=" % location)
    post_url = requests.get(url+access_token)
    posts = post_url.json()

    for post in posts['reviews']:
            try:
                var1 = post['comment'].replace('\n',' ')
            except:
                var1 = 'No Comment'
            var2 = post['updateTime']
            try:
                var3 = post['reviewId'].replace('\n',' ')
            except:
                var3 = 'No ReviewID'
            try:
                var4 = post['starRating']
            except:
                var4 = 'No Rating'
            try:
                var5 = post['reviewer']['displayName']
            except:
                var5 = 'No Display Name'
            var6 = post['createTime']
            Functions.WriteFile(FileLocation,location,var1,var2,var3,var4,var5,var6) #Write data to file