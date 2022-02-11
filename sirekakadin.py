import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://sireka.kadin-indonesia.com/DaftarSubKlasifikasi//index/NIL/NIL/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')
tr = tbody.find_all('tr')
daftar_sub_klasifikasi = []
no = 1
limit = 0
while limit < 620:
    url = 'http://sireka.kadin-indonesia.com/DaftarSubKlasifikasi//index/NIL/NIL/' + str(limit)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')
    for data in tr:
        no = no
        td = data.find_all('td')
        kode = td[0].text
        sub_klasifikasi = td[1].text.strip()
        print(kode, sub_klasifikasi)
        daftar_sub_klasifikasi.append({
            'no': no,
            'kode': kode,
            'sub_klasifikasi': sub_klasifikasi
        })
        no += 1
    limit += 20

with open(f'data_json/daftar_sub_klasifikasi_{no}.json', 'w') as f:
    json.dump(daftar_sub_klasifikasi, f)
    f.close()

df = pd.DataFrame(daftar_sub_klasifikasi)
df.to_csv(f'data_csv/daftar_sub_klasifikasi_{no}.csv', index=False)

df = pd.DataFrame(daftar_sub_klasifikasi)
df.to_excel(f'data_excel/daftar_sub_klasifikasi_{no}.xlsx', index=False)
print(f'Successfully export {no}  sub klasifikasi to csv, json and excel file')
