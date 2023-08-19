import requests

import bs4

url = "https://www.w3schools.com/"

r = requests.get(url)

s = bs4.BeautifulSoup(r.text, 'html.parser')

print("The website links are :")

for a in s.find_all('a'):
    print(a.get('href'))