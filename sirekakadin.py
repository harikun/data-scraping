import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

# url = 'http://sireka.kadin-indonesia.com/DaftarSubKlasifikasi//index/NIL/NIL/'
url2 = 'https://sireka.kadin-indonesia.com/DaftarAsosiasiPerusahaan/index/NIL/NIL/'
res = requests.get(url2)
soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')
tr = tbody.find_all('tr')
daftar_sub_klasifikasi = []
no = 1
limit = 0
# 620
while limit < 80:
    # url = 'http://sireka.kadin-indonesia.com/DaftarSubKlasifikasi//index/NIL/NIL/' + str(limit)
    url2 = 'https://sireka.kadin-indonesia.com/DaftarAsosiasiPerusahaan/index/NIL/NIL/' + str(limit)
    res = requests.get(url2)
    soup = BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')
    for data in tr:
        no = no
        td = data.find_all('td')
        kode = td[0].text
        # sub_klasifikasi = td[1].text.strip()
        nama_asosiasi = td[1].text.strip().replace('<br>', '')
        no_akreditasi = td[2].text.strip()
        tgl_akreditasi = td[3].text.strip()
        print(kode, nama_asosiasi)
        # daftar_sub_klasifikasi.append({
        #     'no': no,
        #     'kode': kode,
        #     'sub_klasifikasi': sub_klasifikasi
        # })
        daftar_sub_klasifikasi.append({
            'no': no,
            'kode': kode,
            'nama_asosiasi': nama_asosiasi,
            'no_akreditasi': no_akreditasi,
            'tgl_akreditasi': tgl_akreditasi
        })
        no += 1
    limit += 20

with open(f'data_json/DaftarAsosiasi_{no - 1 }.json', 'w') as f:
    json.dump(daftar_sub_klasifikasi, f)
    f.close()

df = pd.DataFrame(daftar_sub_klasifikasi)
df.to_csv(f'data_csv/DaftarAsosiasi_{no - 1}.csv', index=False)

df = pd.DataFrame(daftar_sub_klasifikasi)
df.to_excel(f'data_excel/DaftarAsosiasi_{no - 1}.xlsx', index=False)
print(f'Successfully export {no}  sub klasifikasi to csv, json and excel file')

print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')