import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
# params = 'ippd=www.detik.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

res = requests.get(url, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

#Scraping process
contents = soup.find_all('article', {'class': 'list-content__item'})
# print(contents)

#pick item
 # * News title
 # * News link
 # * News Time
 # * News Image

news_list = []
for item in contents:
    title = item.find('h3', {'class': 'media__title'}).text.strip("\n")
    link = item.find('a')['href']
    time = item.find('div', {'class': 'media__date'})
    time_detail = time.find('span')['title']
    image = item.find('img')['src']

    # Sorting Data
    data_dict ={
        'title': title,
        'link': link,
        'time': time_detail,
        'image': image
    }
    news_list.append(data_dict)

# print('Jumlah Datanya adalah ', len(news_list))
#writing to json file
try:
    os.mkdir('data_json')
except FileExistsError:
    pass
with open('data_json/detik.json', 'w') as f:
    json.dump(news_list, f)
    f.close()
print('Successfully written to json file')


