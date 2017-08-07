import json
import csv
import os
import io
from pprint import pprint


jsonFile = '42_Reviews.json'
CSVFile = '42_Parse.csv'
all_fields = ["comment", "updateTime", "reviewId", "starRating", "reviewer", "reviewReply", "createTime"]

with open(jsonFile) as review_file: #Open JSON file
	review_load = json.load(review_file) #Load JSON data into parser

review_parse = review_load['reviews']

#Delete existing file if it exists
try:
	os.remove('ReviewTest.csv')
except OSError:
	pass
#Open file to write JSON data in CSV format
review_data = open(CSVFile, 'w', newline='', encoding="utf-8")

#Create CSV writer object
csv_writer = csv.DictWriter(review_data,delimiter="|",fieldnames=all_fields)
csv_writer.writeheader()
csv_writer.writerows(review_parse)