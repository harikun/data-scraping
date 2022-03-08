from wsgiref import headers
import requests; from bs4 import BeautifulSoup; import pandas as pd; import time;
start_time = time.time()
url = 'https://www.sahamok.net/perusahaan-publik-terbuka-tbk-emiten-bei-bursa-efek-indonesia/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
all_tr = soup.find_all('tr')[1:26]
code_saham = []; no = 0
for data in all_tr:
    no = data.find('td').text
    code = data.find_all('td')[1].text
    company = data.find_all('td')[2].text
    code_saham.append({'no' : no, 'Kode Saham' : code, 'Nama Perusahaan' : company})
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
all_tr = soup.find_all('tr')[27:]
for data in all_tr:
    no = data.find('td').text
    code = data.find_all('td')[1].text
    company = data.find_all('td')[2].text
    code_saham.append({'no' : no, 'Kode Saham' : code, 'Nama Perusahaan' : company})
df = pd.DataFrame(code_saham)
df.to_csv(f'data_csv/sahamok_{no}.csv', index=False)
df.to_excel(f'data_excel/sahamok_{no}.xlsx', index=False)
df.to_json(f'data_json/sahamok_{no}.json', orient='records')
print('--- %s seconds ---' % (time.time() - start_time))

print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')