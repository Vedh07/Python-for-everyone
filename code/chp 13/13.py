import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import xml.etree.ElementTree as ET

url = input("Enter - ")
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count = 0
sum = 0
for item in results:
    x = int(item.find('count').text)
    count = count + 1
    sum = sum + x

print("Count : ",count)
print("Sum : ",sum)

#https://py4e-data.dr-chuck.net/comments_737912.xml