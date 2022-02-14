import json; import time; import requests; import pandas as pd; from bs4 import BeautifulSoup

url = 'https://www.pertamina.com/id/informasi-kapal'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())