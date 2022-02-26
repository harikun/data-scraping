import requests; import pandas as pd; from bs4 import BeautifulSoup
page = 1; no = 0
while page is not None:
    url = 'https://www.ebay.com/b/Sony-Digital-Cameras/31388/bn_772?'
    params = {
        'pgn': page,
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    li_all = soup.find_all('li', class_='s-item s-item--large s-item--bgcolored')
    for data in li_all:
        no += 1
        link = data.find('a', class_='s-item__link')['href']
        title = data.find('h3', class_='s-item__title').text
        price = data.find('span', class_='s-item__price').text
        img = data.find('img', class_='s-item__image-img').get('src')
        try:
            review = data.find('span', class_='s-item__reviews-count').find('span', {'aria-hidden': 'true'}).text.replace('(', '').replace(')', '')
        except:
            review = ''
        print(no, title)
    page += 1

