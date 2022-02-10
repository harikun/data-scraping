import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/mobile-phones-338/iphones-1235/?'
site = 'https://id.carousell.com'
params = {
 'addRecent' : 'false',
 'canChangeKeyword' : 'false',
 'includeSuggestions' : 'false',
 'searchId': 'z6XT3v',
}
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

iphone_container = soup.find(attrs={'class': 'D_E'})
card_iphone = iphone_container.find_all('div', {'class': 'D_s_'})
iphone_list = []
id = 0
for data in card_iphone:
   seller = data.find('p').text
   time_post = data.find('div', {'class': 'D_sO'}).text
   img_link = data.find('img').get('src')
   product_name = data.find('img').get('title')
   price = data.find('p', {'class': 'D_g_'}).text

   data_dict = {
         'id': id,
         'seller name': seller,
         'time post': time_post,
         'img link': img_link,
         'product name': product_name,
         'price': price,
    }
   id += 1
   iphone_list.append(data_dict)

try:
    os.mkdir('data_json')
except OSError:
    pass

with open('data_json/carousell.json', 'w+') as f:
    json.dump(iphone_list, f)
    f.close()
print('Data berhasil di simpan di data_json/carousell.json')

try:
    os.mkdir('data_excel')
except FileExistsError:
      pass
df = pd.DataFrame(iphone_list)
df.to_csv(f'data_excel/carousell.csv', index=False)
df.to_excel(f'data_excel/carousell.xlsx', index=False)

print(f'File carousell.csv and carousell.xlsx has been created')




