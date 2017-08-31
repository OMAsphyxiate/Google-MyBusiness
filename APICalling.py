import sys, pyodbc, requests
#sys.path.insert(0, 'C:/Users/Reaper/Dropbox/Blah/')
sys.path.insert(0, 'C:/Users/Christian/Dropbox/Blah/')
sys.path.insert(0, 'E:/GitHub/FacebookInsights/')
import Connect #Import connection file
import Functions #Import Functions for creating file

#location = '6792341780129689742'
access_token = ''
#url = ("https://mybusiness.googleapis.com/v3/accounts/107604422420814997819/locations/%s/reviews?access_token=" % location)

#for location in Connect.LocationList:
for location in Connect.LocationList:
    print(location)
    print(str(location))
    url = ("https://mybusiness.googleapis.com/v3/accounts/107604422420814997819/locations/%s/reviews?access_token=" % location)
    post_url = requests.get(url+access_token)
    print(post_url.url)
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
            Functions.PrintValues('GoogleReviews', locations,var1,var2,var3,var4,var5,var6) #Write data to file