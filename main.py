import requests

from bs4 import BeautifulSoup

url = input("Enter url here:")

r = requests.get(url)

s = BeautifulSoup(r.text, 'html.parser')

print("The website title is :")

for title in s.find_all('title'):
    print(title.get_text())