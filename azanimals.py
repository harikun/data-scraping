import json; import time; import requests; import pandas as pd; from bs4 import BeautifulSoup
url = 'https://a-z-animals.com/animals/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
no = 0; animal_list = []
list_item = soup.find_all('li', {'class': 'list-item'})
for i in list_item:
    no += 1
    animal_list.append({
        'no': no,
        'animal': i.text,
        'link': i.find('a').get('href')
    })
