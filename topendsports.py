import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
url = 'https://www.topendsports.com/sport/list/index.htm'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
sports_list = []
no = 0
li = soup.find_all('li')
for item in li:
    if no < 900:
        print(no, item.text)
    sports_list.append({
        'no': no,
        'sport name': item.text
    })
    no += 1

with open(f'data_json/sports_list_{no - 1}.json', 'w') as f:
    json.dump(sports_list, f)
    f.close()

print("--- %s seconds ---" % (time.time() - start_time))