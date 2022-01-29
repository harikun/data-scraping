import os
import json
import requests
from bs4 import BeautifulSoup

url = 'http://jadwalsholat.pkpu.or.id/?'
params = {
    'id': '48',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
jadwal_sholat = soup.find_all('tr', {'class': 'table_highlight'})
datas = jadwal_sholat[0]
sholat = {}
i = 0
for data in datas:
    if i == 1:
        sholat['subuh'] = data.text
    elif i == 2:
        sholat['dzuhur'] = data.text
    elif i == 3:
        sholat['ashar'] = data.text
    elif i == 4:
        sholat['maghrib'] = data.text
    elif i == 5:
        sholat['isya'] = data.text
    i += 1
# create a json file
try:
   os.mkdir('data_json')
except OSError:
    pass

with open('data_json/pkpu.json', 'w+') as f:
    json.dump(sholat, f)
    f.close()
print('Data berhasil di simpan di data_json/pkpu.json')
