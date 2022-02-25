import requests; import pandas as pd; from bs4 import BeautifulSoup
url_topseller_windows = 'https://store.steampowered.com/search/?filter=topsellers&os=win'
res = requests.get(url_topseller_windows)
soup = BeautifulSoup(res.text, 'lxml')
a = soup.find_all('a', class_='search_result_row')
top_sellers_windows = []; no = 0
for data in a:
    no += 1
    link = data.get('href')
    img = data.find('img').get('src')
    name = data.find('span', class_='title').text
    released = data.find('div', class_='search_released').text
    if data.find('div', class_='search_price').find('strike') is None:
        price = data.find('div', class_='search_price').text.strip()
    else:
        price = data.find('div', class_='search_price').contents[3].text
    print(no, name)


print('Support me on karyakarsa: https://karyakarsa.com/ciptosuhari')