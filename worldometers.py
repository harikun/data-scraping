import requests; from bs4 import BeautifulSoup; import time; import pandas as pd;
start_time = time.time()
url = 'https://www.worldometers.info/world-population/population-by-country/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
tr = soup.find_all('tr')
for td in tr:
    print(td.text)