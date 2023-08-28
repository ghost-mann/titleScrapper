import re
import requests
import bs4
from urllib.parse import urlparse

url = "https://www.google.com"

r = requests.get(url)

s = bs4.BeautifulSoup(r.text, 'html.parser')

print("The website links are :")

links = []
for a in s.find_all('a'):
    href = a.get('href')

    if not re.match(r'^[a-zA-Z]+://', href):
        continue

    if not urlparse(href).netloc:
        href = url + href

    links.append(href)

for link in links:
    print(link)
