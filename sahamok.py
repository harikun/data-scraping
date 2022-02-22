from wsgiref import headers
import requests; from bs4 import BeautifulSoup; import pandas as pd; import time;
url = 'https://www.sahamok.net/perusahaan-publik-terbuka-tbk-emiten-bei-bursa-efek-indonesia/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
all_tr = soup.find_all('tr')[1:]
for data in all_tr:
    print(data.text)