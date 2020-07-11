import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import json
count = 0

url = input("Enter - ")
data = urllib.request.urlopen(url).read()

info = json.loads(data)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number
print (count)

#https://py4e-data.dr-chuck.net/comments_737913.json

#https://py4e-data.dr-chuck.net/comments_42.json