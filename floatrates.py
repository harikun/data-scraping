import os
import requests
import pandas as pd

url = 'http://www.floatrates.com/daily/idr.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, headers=headers)
print(res.status_code)
res_json = res.json()

data_rates = []
for data in res_json.values():
    data_dict = {
        'code': data['code'],
        'name': data['name'],
        'inverseRate': data['inverseRate'],
        'date': data['date']
    }
    data_rates.append(data_dict)
print(f'data berhasil di scraping')

try:
    os.mkdir('data_excel')
except:
    pass

df = pd.DataFrame(data_rates)
df.to_excel('data_excel/float_rates.xlsx', index=False)

print('data berhasil di export ke excel')